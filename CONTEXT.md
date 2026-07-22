# SourceLoom domain glossary

This file defines the project’s domain language. It deliberately excludes implementation details.

## Research Question

The user’s original information need. A Research Question may require several Claims to answer responsibly.

## Claim

A concrete proposition that can be supported, contradicted or left unresolved. A Claim is narrower than a Research Question.

## Source

The origin that publishes information, such as an official organisation, repository, paper or news outlet. Several Documents can belong to one Source.

## Document

A retrievable unit of content produced by a Source, such as a web page, API response, PDF or repository file.

## Evidence

A specific passage or structured record from a Document that is relevant to a Claim. A citation to a Document is not automatically Evidence.

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

## Report

The output of a Research Run. It contains supported conclusions, citations, Contradictions, unresolved Evidence Gaps and the stopping reason.
