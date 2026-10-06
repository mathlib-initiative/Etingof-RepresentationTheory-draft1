/-
Copyright (c) 2026 American Mathematical Society. All rights reserved.
-/

import VersoManual

/-!
# Mathematical expressions in native Verso headings

Verso renders inline mathematics in headings, but currently has no plain-string converter for
those nodes when it constructs previews and navigation labels. This converter preserves the
ordinary `$`...`` source notation while giving navigation the underlying TeX string.
-/

namespace IntroductionToRepresentationTheoryVerso.MathHeading

open Lean Verso.Doc.Elab

@[inline_to_string Lean.Doc.Syntax.inline_math]
public meta def inlineMathToString : InlineToString := fun _ stx => do
  let arguments := stx.getArgs
  guard (arguments.size = 2)
  let codeArguments := arguments[1]!.getArgs
  guard (codeArguments.size = 3)
  let stringArguments := codeArguments[1]!.getArgs
  guard (stringArguments.size = 1)
  Syntax.decodeStrLit stringArguments[0]!.getAtomVal

end IntroductionToRepresentationTheoryVerso.MathHeading
