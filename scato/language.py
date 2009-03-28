from scato.tortoise import Tortoise


##################################################


class LanguageException(Exception):

    pass


##################################################


class Token:

    def __init__(self, text, line):
        self.text = text
        self.line = line
        try:
            self.num = float(text)
            self.is_num = True
        except ValueError:
            self.is_num = False
        except TypeError: # for None-terminator
            self.is_num = False


class TokenSequence:

    def __init__(self, text):
        self.words = []
        n = 0
        for l in text.split('\n'):
            n += 1
            i = l.find('#')
            if i >= 0:
                l = l[:i]
            for t in l.split():
                self.words.append(Token(t, n))
        self.words.append(Token(None, n)) # terminator
        self.idx = 0

    def top(self):
        return self.words[self.idx]

    def step(self):
        self.idx += 1

    def next(self):
        v = self.top()
        if v.text is None:
            raise LanguageException('End of program reached, '
                                    'but last statement not complete.')
        self.step()
        return v

    def next_check(self, words):
        v = self.next()
        if not v.text in words:
            if len(words) > 1:
                message = (
                     'Line %d: One of the words %s must be here, '
                     'bun "%s" in fact.') % (
                     v.line,
                     ', '.join(map(lambda x: '"%s"' % x, words)),
                     v.text)
            else:
                message = (
                     'Line %d: The word "%s" must be here, '
                     'bun "%s" in fact.') % (v.line, words[0], v.text)
            raise LanguageException(message)
        return v


##################################################


# STATMENTS


#
# Simple statements
#


class StatementNop:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.status_line = '%d: nop' % self.itself.line

    def __call__(self, ctx):
        ctx.status_line = self.status_line


#
# scale, left, right, width
#


class StatementScale:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.val = tokens.next()
        self.status_line = '%d: %s %s # %%.6g' % (
                            self.itself.line,
                            self.itself.text,
                            self.val.text)

    def __call__(self, ctx):
        v = ctx.vars[self.val]
        ctx.tortoise.scale(v)
        ctx.status_line = self.status_line % v


class StatementRight(StatementScale):

    def __call__(self, ctx):
        v = ctx.vars[self.val]
        ctx.tortoise.rotate(-v)
        ctx.status_line = self.status_line % v


class StatementLeft(StatementScale):

    def __call__(self, ctx):
        v = ctx.vars[self.val]
        ctx.tortoise.rotate(v)
        ctx.status_line = self.status_line % v


class StatementWidth(StatementScale):

    def __call__(self, ctx):
        v = ctx.vars[self.val]
        ctx.tortoise.width(v)
        ctx.status_line = self.status_line % v


#
# draw, jump
#


class StatementDraw:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.dx = tokens.next()
        self.dy = tokens.next()
        self.status_line = '%d: %s %s %s # (%%.6g, %%.6g)' % (
                            self.itself.line,
                            self.itself.text,
                            self.dx.text,
                            self.dy.text)

    def __call__(self, ctx):
        #ctx.draw_flag = True
        dx = ctx.vars[self.dx]
        dy = ctx.vars[self.dy]
        ctx.status_line = self.status_line % (dx, dy)
        ctx.tortoise.draw(dx, dy)


class StatementJump(StatementDraw):

    def __call__(self, ctx):
        dx = ctx.vars[self.dx]
        dy = ctx.vars[self.dy]
        ctx.status_line = self.status_line % (dx, dy)
        ctx.tortoise.jump(ctx.vars[self.dx], ctx.vars[self.dy])


#
# color, bgcolor, mixcolor
#


class StatementColor:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.rgb = []
        self.rgb.append(tokens.next())
        self.rgb.append(tokens.next())
        self.rgb.append(tokens.next())
        self.status_line = '%d: %s %s %s %s # (%%.6g, %%.6g, %%.6g)' % (
                            self.itself.line,
                            self.itself.text,
                            self.rgb[0].text,
                            self.rgb[1].text,
                            self.rgb[2].text)

    def __call__(self, ctx):
        rgb = map(lambda x: ctx.vars[x], self.rgb)
        ctx.tortoise.color(rgb)
        ctx.status_line = self.status_line % tuple(rgb)


class StatementBgColor(StatementColor):

    def __call__(self, ctx):
        rgb = map(lambda x: ctx.vars[x], self.rgb)
        ctx.tortoise.fill(rgb)
        ctx.status_line = self.status_line % tuple(rgb)


class StatementMixColor:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.rgb = []
        self.rgb.append(tokens.next())
        self.rgb.append(tokens.next())
        self.rgb.append(tokens.next())
        self.f = tokens.next()
        self.status_line = '%d: %s %s %s %s %s # (%%.6g, %%.6g, %%.6g), %%.6g' % (
                            self.itself.line,
                            self.itself.text,
                            self.rgb[0].text,
                            self.rgb[1].text,
                            self.rgb[2].text,
                            self.f.text)

    def __call__(self, ctx):
        rgb = map(lambda x: ctx.vars[x], self.rgb)
        f = ctx.vars[self.f]
        ctx.tortoise.mix(rgb, f)
        ctx.status_line = self.status_line % tuple(rgb+[f])


#
# set, add, sub, incr, decr, mul, div
#


class StatementSet:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.a = tokens.next()
        if self.a.is_num:
            raise LanguageException((
               'You can not assign value to constant '
               'at line %d') % self.itself.line)
        self.b = tokens.next()
        self.status_line = '%d: set %s %s # %s := %%.6g' % (
                            self.itself.line,
                            self.a.text,
                            self.b.text,
                            self.a.text)

    def __call__(self, ctx):
        v = ctx.vars[self.b]
        ctx.vars[self.a] = v
        ctx.status_line = self.status_line % v


class StatementBinOp:

    def __init__(self, tokens):
        self.itself = tokens.next()
        t = self.itself.text
        self.op = {'add': lambda x, y: x + y,
                   'sub': lambda x, y: x - y,
                   'mul': lambda x, y: x * y,
                   'div': lambda x, y: x / y}[t]
        self.a = tokens.next()
        if self.a.is_num:
            raise LanguageException((
               'You can not apply "%s" to '
               'constant %s at line %d') % (
               self.itself.text, self.a.text, self.itself.line))
        self.b = tokens.next()
        self.status_line = '%d: %s %s %s # %s := %%.6g' % (
                            self.itself.line,
                            t,
                            self.a.text,
                            self.b.text,
                            self.a.text)

    def __call__(self, ctx):
        try:
            v = self.op(ctx.vars[self.a], ctx.vars[self.b])
        except ZeroDivisionError:
            raise LanguageException(
               'Zero division error at line %d' % self.itself.line)
        ctx.vars[self.a] = v
        ctx.status_line = self.status_line % v


class StatementIncr:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.a = tokens.next()
        if self.a.is_num:
            raise LanguageException((
             'Operation %s can not be applay to '
             'numerical value %s at line %d') % (
             self.itself.text, self.a.text, self.itself.line))
        self.status_line = '%d: %s %s # %s := %%.6g' % (
                            self.itself.line,
                            self.itself.text,
                            self.a.text,
                            self.a.text)

    def __call__(self, ctx):
        v = ctx.vars[self.a] + 1
        ctx.vars[self.a] = v
        ctx.status_line = self.status_line % v


class StatementDecr(StatementIncr):

    def __call__(self, ctx):
        v = ctx.vars[self.a] - 1
        ctx.vars[self.a] = v
        ctx.status_line = self.status_line % v


class StatementNeg(StatementIncr):

    def __call__(self, ctx):
        v = - ctx.vars[self.a]
        ctx.vars[self.a] = v
        ctx.status_line = self.status_line % v


#
# Control statements
#


class StatementIterateRuner:

    def __init__(self, ctx, limit, body, status_line):
        self.limit = limit
        self.status_line = status_line
        self.count = 0
        self.body = body
        self.parent = ctx.prog
        self.call_body = False

    def __call__(self, ctx):
        if self.call_body:
            self.body(ctx)
            self.call_body = False
        else:
            self.count += 1
            if self.count > self.limit:
                ctx.prog = self.parent
                c = 'end of iterations'
            else:
                self.call_body = True
                c = 'step %g / %g' % (self.count, self.limit)
            ctx.status_line = self.status_line % c


class StatementIterate:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.limit_var = tokens.next()
        self.body = CreateStatement(tokens)
        self.status_line = '%d: iterate %s # %%s' % (
                            self.itself.line, self.limit_var.text)

    def __call__(self, ctx):
        ctx.prog = StatementIterateRuner(ctx,
                                        ctx.vars[self.limit_var],
                                        self.body,
                                        self.status_line)
        ctx.prog(ctx)


class StatementConditionExpression:

    def __init__(self, tokens):
        self.a = tokens.next()
        op = tokens.next_check(('lt', 'gt', 'le', 'ge', 'eq', 'ne')).text
        self.op, self.sig = {'lt': (lambda a, b: a <  b, '<'),
                             'gt': (lambda a, b: a >  b, '>'),
                             'le': (lambda a, b: a <= b, '<='),
                             'ge': (lambda a, b: a >= b, '>='),
                             'eq': (lambda a, b: a == b, '=='),
                             'ne': (lambda a, b: a != b, '!='),
                            }[op]
        self.b = tokens.next()
        self.text = '%s %s %s' % (self.a.text, op, self.b.text)

    def __call__(self, ctx):
        a = ctx.vars[self.a]
        b = ctx.vars[self.b]
        r = self.op(a, b)
        return (r, '%.6g %s %.6g = %s' % (a, self.sig, b, str(r)))


class StatementRepeatRuner:

    def __init__(self, ctx, body, op, status_line):
        self.body = body
        self.op = op
        self.parent = ctx.prog
        self.call_body = True
        self.status_line = status_line

    def __call__(self, ctx):
        if self.call_body:
            self.body(ctx)
            self.call_body = False
        else:
            r, c = self.op(ctx)
            if r:
                self.call_body = True
                rem = ' (continue)'
            else:
                ctx.prog = self.parent
                rem = ' (done)'
            ctx.status_line = self.status_line % c + rem


class StatementRepeat:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.body = CreateStatement(tokens)
        self.itself_until = tokens.next_check(('until',))
        self.op = StatementConditionExpression(tokens)
        self.status_line = '%d-%d: repeat / until %s # %%s' % (
                            self.itself.line,
                            self.itself_until.line,
                            self.op.text)

    def __call__(self, ctx):
        ctx.prog = StatementRepeatRuner(ctx, self.body, self.op, self.status_line)
        ctx.status_line = self.status_line % '(enter to loop)'


class StatementWhileRuner:

    def __init__(self, ctx, body, op, status_line):
        self.body = body
        self.op = op
        self.parent = ctx.prog
        self.status_line = status_line
        self.call_body = False

    def __call__(self, ctx):
        if self.call_body:
            self.body(ctx)
            self.call_body = False
        else:
            r, c = self.op(ctx)
            if r:
                self.call_body = True
                rem = ' (continue)'
            else:
                ctx.prog = self.parent
                rem = ' (done)'
            ctx.status_line = self.status_line % (c + rem)


class StatementWhile:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.op = StatementConditionExpression(tokens)
        self.body = CreateStatement(tokens)
        self.status_line = '%d: while %s # %%s' % (
                            self.itself.line, self.op.text)

    def __call__(self, ctx):
        ctx.prog = StatementWhileRuner(ctx, self.body, self.op, self.status_line)
        ctx.prog(ctx)



class StatementBlockRuner:

    def __init__(self, statements, status_line_end, ctx):
        self.statements = statements
        self.idx = -1
        self.parent = ctx.prog
        self.status_line_end = status_line_end

    def __call__(self, ctx):
        self.idx += 1
        if self.idx < len(self.statements):
            self.statements[self.idx](ctx)
        else:
            ctx.prog = self.parent
            ctx.status_line = self.status_line_end


class StatementBlock:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.status_line = '%d: begin' % self.itself.line
        self.statements = []
        while True:
            t = tokens.top()
            if t is None:
                raise LanguageException((
                       'Reach end of file, but not '
                       'find "end" for "begin" at line %d') % self.itself.line)
            tt = t.text
            if tt == 'end':
                self.status_line_end = '%d: end' % t.line
                tokens.step()
                break
            self.statements.append(CreateStatement(tokens))

    def __call__(self, ctx):
        ctx.prog = StatementBlockRuner(self.statements, self.status_line_end, ctx)
        ctx.status_line = self.status_line


class StatementProgRuner:

    def __init__(self, statements, ctx):
        self.statements = statements
        self.idx = -1
        self.parent = ctx.prog

    def __call__(self, ctx):
        self.idx += 1
        if self.idx < len(self.statements):
            self.statements[self.idx](ctx)
        else:
            ctx.prog = None


class StatementProg: # meta-statement like block

    def __init__(self, tokens):
        self.statements = []
        while not tokens.top().text is None:
            self.statements.append(CreateStatement(tokens))

    def __call__(self, ctx):
        ctx.prog = StatementProgRuner(self.statements, ctx)
        ctx.prog(ctx)


class StatementIfRuner:

    def __init__(self, ctx, body, status_line):
        self.parent = ctx.prog
        self.body = body
        self.perform = True
        self.status_line = status_line

    def __call__(self, ctx):
        if self.perform:
            self.perform = False
            self.body(ctx)
        else:
            ctx.prog = self.parent
            ctx.status_line = self.status_line % '(done)'


class StatementIf:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.op = StatementConditionExpression(tokens)
        tokens.next_check(('then',))
        self.body = CreateStatement(tokens)
        if tokens.top().text == 'else':
            tokens.step()
            self.ebody = CreateStatement(tokens)
        else:
            self.ebody = None
        self.status_line = '%d if %s # %%s' % (self.itself.line, self.op.text)

    def __call__(self, ctx):
        r, c = self.op(ctx)
        if r:
            ctx.prog = StatementIfRuner(ctx, self.body, self.status_line)
            rem = ' (then)'
        else:
            if not self.ebody is None:
                ctx.prog = StatementIfRuner(ctx, self.ebody, self.status_line)
                rem = ' (else)'
            else:
                rem = ' (else, but nothing to do)'
        ctx.status_line = self.status_line % c + rem


class StatementProcedure:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.a = tokens.next()
        self.body = CreateStatement(tokens)
        self.status_line = '%d: procedure %s # procedure created' % (
                            self.itself.line, self.a.text)


    def __call__(self, ctx):
        ctx.proc[self.a.text] = self.body
        ctx.status_line = self.status_line


class StatementCallRuner:

    def __init__(self, ctx, body, status_line):
        self.body = body
        self.status_line = status_line
        self.parent = ctx.prog
        self.call_body = True

    def __call__(self, ctx):
        if self.call_body:
            self.body(ctx)
            self.call_body = False
        else:
            ctx.prog = self.parent
            ctx.status_line = self.status_line % 'done'


class StatementCall:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.a = tokens.next()
        self.status_line = '%d: call %s # %%s' % (
                            self.itself.line, self.a.text)

    def __call__(self, ctx):
        try:
            p = ctx.proc[self.a.text]
        except KeyError:
            raise LanguageException('Procedure %s, called in %d line, not defined yet.' % (self.a.text, self.a.line))
        ctx.prog = StatementCallRuner(ctx,
                                      p,
                                      self.status_line)
        ctx.status_line = self.status_line % 'call'


#
# Scope statements
#


class StatementSaveRuner:

    def __init__(self, ctx, body, status_line):
        self.body = body
        self.parent = ctx.prog
        self.save_and_run = True
        self.saved_vars = None
        self.status_line = status_line

    def __call__(self, ctx):
        if self.save_and_run:
            self.saved_vars = ctx.vars.copy()
            self.save_and_run = False
            self.body(ctx)
        else:
            ctx.vars.set(self.saved_vars)
            ctx.prog = self.parent
            ctx.status_line = self.status_line % 'restore'


class StatementSave:

    def __init__(self, tokens):
        self.itself = tokens.next()
        self.body = CreateStatement(tokens)
        self.status_line = '%d: %s # %%s' % (self.itself.line, self.itself.text)

    def __call__(self, ctx):
        ctx.prog = StatementSaveRuner(ctx, self.body, self.status_line)
        ctx.status_line = self.status_line % 'save'


class StatementTransformRuner(StatementSaveRuner):

    def __call__(self, ctx):
        if self.save_and_run:
            self.saved_vars = ctx.tortoise.clone()
            self.save_and_run = False
            self.body(ctx)
        else:
            ctx.tortoise = self.saved_vars
            ctx.prog = self.parent
            ctx.status_line = self.status_line % 'restore'


class StatementTransform(StatementSave):

    def __call__(self, ctx):
        ctx.prog = StatementTransformRuner(ctx, self.body, self.status_line)
        ctx.status_line = self.status_line % 'save'


class StatementLocalRuner(StatementSaveRuner):

    def __call__(self, ctx):
        if self.save_and_run:
            self.saved_vars = (ctx.vars.copy(), ctx.tortoise.clone())
            self.save_and_run = False
            self.body(ctx)
        else:
            ctx.vars.set(self.saved_vars[0])
            ctx.tortoise = self.saved_vars[1]
            ctx.prog = self.parent
            ctx.status_line = self.status_line % 'restore'


class StatementLocal(StatementSave):

    def __call__(self, ctx):
        ctx.prog = StatementLocalRuner(ctx, self.body, self.status_line)
        ctx.status_line = self.status_line % 'save'


#
# Statements factory
#


def CreateStatement(tokens):
    t = tokens.top()
    tt = t.text
    if tt is None:
        raise LanguageException('Reach end of file, '
                                'but statement or "end" '
                                'must be here.')
    try:
        c = {'begin':     StatementBlock,
             'iterate':   StatementIterate,
             'repeat':    StatementRepeat,
             'while':     StatementWhile,
             'draw':      StatementDraw,
             'jump':      StatementJump,
             'nop':       StatementNop,
             'scale':     StatementScale,
             'right':     StatementRight,
             'left':      StatementLeft,
             'width':     StatementWidth,
             'color':     StatementColor,
             'bgcolor':   StatementBgColor,
             'mixcolor':  StatementMixColor,
             'set':       StatementSet,
             'add':       StatementBinOp,
             'sub':       StatementBinOp,
             'mul':       StatementBinOp,
             'div':       StatementBinOp,
             'incr':      StatementIncr,
             'decr':      StatementDecr,
             'neg':       StatementNeg,
             'if':        StatementIf,
             'procedure': StatementProcedure,
             'call':      StatementCall,
             'local':     StatementLocal,
             'save':      StatementSave,
             'transform': StatementTransform,
            }[tt]
    except KeyError:
        raise LanguageException(
            'Unknown statement %s at line %d' % (tt, t.line))
    return c(tokens)


##################################################


class Variables:

    def __init__(self):
        self.space = {}

    def __setitem__(self, key, val):
        self.space[key.text] = val

    def __getitem__(self, key):
        if key.is_num:
            return key.num
        try:
            return self.space[key.text]
        except KeyError:
            raise LanguageException('Variable %s use before set in line %d' % (key.text, key.line))

    def set(self, vars):
        self.space = vars

    def copy(self):
        return self.space.copy()


##################################################


class Context:

    def __init__(self, draw_area):
        self.tortoise = Tortoise(draw_area)
        self.drop_state(None)

    def drop_state(self, prog):
        self.vars = Variables()
        self.proc = {}
        self.tortoise.vanish()
        self.prog = prog
