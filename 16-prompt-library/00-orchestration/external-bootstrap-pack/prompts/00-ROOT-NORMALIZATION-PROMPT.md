# Prompt 00 — Normalize the Repository Root

Paste this into Cursor while the currently cloned repository is open at:

`C:\Development\Workspace\DevotionalRepo\kutumba-family-program\kutumba-family-program`

---

You are performing a one-time repository-root normalization. Do not build any KUTUMBA content yet.

## Current and target paths

Current nested clone:

`C:\Development\Workspace\DevotionalRepo\kutumba-family-program\kutumba-family-program`

Required canonical repository root:

`C:\Development\Workspace\DevotionalRepo\kutumba-family-program`

The goal is to remove the redundant folder level so the `.git` directory and repository files live directly under:

`C:\Development\Workspace\DevotionalRepo\kutumba-family-program`

## Safety rules

1. Inspect both paths before changing anything.
2. Confirm `.git` exists in the current nested clone.
3. Run:
   - `git status --short`
   - `git remote -v`
   - `git branch --show-current`
   - `git rev-parse --show-toplevel`
4. Do not proceed if the current repository has uncommitted work that cannot be preserved.
5. The outer target folder may contain the inner clone folder and harmless operating-system metadata only. Do not overwrite unrelated files.
6. Preserve hidden files, `.git`, remote configuration, branch, timestamps where practical, and all repository content.
7. Do not create another Git repository.
8. Do not delete the source repository until the moved repository has been independently verified.

## Required operation

Create a timestamped safety backup of any unexpected outer-folder files.

Move the complete contents of the inner clone, including `.git`, one level up into:

`C:\Development\Workspace\DevotionalRepo\kutumba-family-program`

Remove the now-empty inner `kutumba-family-program` directory.

Verify using absolute paths:

- `git -C "C:\Development\Workspace\DevotionalRepo\kutumba-family-program" rev-parse --show-toplevel`
- `git -C "C:\Development\Workspace\DevotionalRepo\kutumba-family-program" status --short`
- `git -C "C:\Development\Workspace\DevotionalRepo\kutumba-family-program" remote -v`
- `git -C "C:\Development\Workspace\DevotionalRepo\kutumba-family-program" fsck --no-progress`

Create this report in the final root:

`REPO-ROOT-NORMALIZATION-REPORT.md`

The report must record:

- old path
- new path
- date and time
- branch
- remote URL
- initial Git status
- final Git status
- verification commands and results
- backup path, if any
- any issue encountered

## Important workspace limitation

After the move, the currently open Cursor workspace points to a path that no longer exists. This is expected.

Attempt to open a new Cursor window at:

`C:\Development\Workspace\DevotionalRepo\kutumba-family-program`

Use the available Cursor executable or shell command when it is safely discoverable. Do not guess an executable path destructively.

Then stop. Do not continue the repository build in the stale workspace.

Display exactly:

`ROOT NORMALIZATION COMPLETE — REOPEN C:\Development\Workspace\DevotionalRepo\kutumba-family-program AND RUN PROMPT 01.`

If root normalization cannot be completed safely, make no destructive change. Write a failure report in the current repository and give the precise blocker.
