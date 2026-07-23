# SourceLoom domain glossary

This file defines the project’s domain language. It deliberately excludes implementation details.

## Research Question

The user’s original information need. A Research Question may require several Claims to answer responsibly.

## Research Contract

The explicit scope and limits of a Research Run. It records the question’s temporal, jurisdictional and definitional boundaries together with the evidence expectations and hard budgets that govern the run.

## Claim

A concrete proposition that can be supported, contradicted or left unresolved. A Claim is narrower than a Research Question.

## Claim Type

The category that determines how a Claim must be scoped and what kind of Evidence can responsibly support it. Initial examples include current policy, legal, quantitative, scientific, historical and technical capability Claims.

## Evidence Standard

The explicit requirements that Evidence must meet for a Claim. It can constrain source type, directness, freshness, scope and independence without reducing confidence to one opaque score.

## Source

The origin that publishes information, such as an official organisation, repository, paper or news outlet. Several Documents can belong to one Source.

## Source Lineage

The trace from a Document back to the origin of the information it contains. Source Lineage distinguishes independent Evidence from republication, syndication and citation of the same origin.

## Search Result

A candidate reference returned by a Search Provider. Its title, URL or excerpt helps discover a Document but does not itself constitute Evidence.

## Snippet

A short excerpt returned inside a Search Result. It retains its discovery provenance, including provider, query, result rank and discovered URL, but cannot be linked directly to a Claim as Evidence.

## Document

A retrieved unit of content produced by a Source, such as a web page, API response, PDF or repository file. It records the canonical URL and the retrieved content separately from discovery metadata.

## Evidence

A specific passage or structured record from a Document that is relevant to a Claim. Textual Evidence records the exact character range it quotes from the Document. A citation to a Document is not automatically Evidence.

## Evidence Link

A typed relationship between Evidence and a Claim. The initial relationship types are `supports` and `contradicts`.

## Evidence Gap

A Claim that lacks sufficient Evidence for the requested standard of confidence. An Evidence Gap can trigger another Search Wave.

## Contradiction

A state in which credible Evidence supports incompatible versions of the same Claim. A Contradiction is surfaced, not silently resolved by prose.

## Search Provider

A system that returns candidate Documents or references for a Query. Providers do not decide whether the returned material is sufficient Evidence.

## Query

A concrete request sent to a Search Provider in order to address one or more Evidence Gaps.

## Search Wave

A bounded group of Queries planned from the current Evidence Gaps and executed before the research state is reassessed.

## Research Run

The complete trace from one Research Question to a Report, including Queries, Documents, Evidence Links, decisions and stopping reason.

## Stopping Policy

The explicit rules that end a Research Run because evidence requirements were met or a hard limit was reached.

## Stopping Reason

The explicit, serialisable outcome that explains why a Research Run ended. Reaching a budget or timeout never upgrades an unresolved Claim into a conclusion.

## Report

The output of a Research Run. It contains supported conclusions, citations, Contradictions, unresolved Evidence Gaps and the stopping reason.
