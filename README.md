#+TITLE: Graphs Project Plan
#+AUTHOR: Vaibhav Karve
#+DESCRIPTION: A roadmap for symbolic and combinatorial graph theory using Python.

* 🗺️ Project Roadmap

** Phase 1: Core Blocks
- [ ] BLOCK 1: Graph Input/Output Handler
  - [ ] Implement load from edge list
  - [ ] Implement save to edge list
  - [ ] Convert to/from adjacency matrix
- [ ] BLOCK 2: Basic Graph Generator
  - [ ] Generate complete graphs
  - [ ] Generate cycle graphs
  - [ ] Generate grid graphs
  - [ ] Generate Erdős–Rényi random graphs
- [ ] BLOCK 3: Symbolic Invariant Extractor
  - [ ] Degree sequence
  - [ ] Average degree (symbolic)
  - [ ] Chromatic number bounds
  - [ ] Regularity check

** Phase 2: Analysis and Filtering
- [ ] BLOCK 4: Subgraph Pattern Matcher
  - [ ] Detect triangle/K₃ subgraphs
  - [ ] Match custom subgraph patterns
- [ ] BLOCK 5: Graph Enumerator with Constraints
  - [ ] Enumerate n-node graphs
  - [ ] Filter by forbidden subgraphs
  - [ ] Filter by planarity or degree
- [ ] BLOCK 6: Canonicalization Tool
  - [ ] Convert to canonical labeling
  - [ ] Hash based on invariant structure
- [ ] BLOCK 7: Graph Automorphism Finder
  - [ ] Compute symmetry groups of graphs

** Phase 3: Symbolic and Polynomial Tools
- [ ] BLOCK 8: Symbolic Recurrence & Pattern Finder
  - [ ] Analyze graph families
  - [ ] Extract recurrence relations
- [ ] BLOCK 9: Graph Polynomial Engine
  - [ ] Compute chromatic polynomial
  - [ ] Compute independence polynomial
  - [ ] Support recursive graph classes
- [ ] BLOCK 10: Symbolic Graph Transformation Module
  - [ ] Edge contraction
  - [ ] Line graph transformation
  - [ ] Dual graph (planar only)

** Phase 4: Research Automation
- [ ] BLOCK 11: Invariant-Conjecture Generator
  - [ ] Correlate degree, diameter, chromatic number
  - [ ] Generate symbolic inequalities
- [ ] BLOCK 12: Generating Function Synthesizer
  - [ ] Fit symbolic generating functions to enumerations
  - [ ] Guess rational/exponential forms

* 🔁 Inter-Block Dependencies
- [ ] BLOCK 2 depends on BLOCK 1
- [ ] BLOCK 3 depends on BLOCK 1, BLOCK 2
- [ ] BLOCK 4 depends on BLOCK 2
- [ ] BLOCK 5 depends on BLOCK 2, BLOCK 4
- [ ] BLOCK 6 depends on BLOCK 1
- [ ] BLOCK 7 depends on BLOCK 2
- [ ] BLOCK 8 depends on BLOCK 3, BLOCK 5
- [ ] BLOCK 9 depends on BLOCK 3, BLOCK 5
- [ ] BLOCK 10 depends on BLOCK 3, BLOCK 5
- [ ] BLOCK 11 depends on BLOCK 3, BLOCK 5, BLOCK 6, BLOCK 7
- [ ] BLOCK 12 depends on BLOCK 5, BLOCK 8

* 📈 Research Problems (P1–P8)
- [ ] P1: Symbolic enumeration of graphs by invariant
  - [ ] Use BLOCK 2, 3, 5
  - [ ] Build families by constraints
  - [ ] Group by chromatic number, degree
- [ ] P2: Conjecture generation from invariants
  - [ ] Use BLOCK 2, 3, 11
  - [ ] Find correlations across graph classes
- [ ] P3: Closed-form expressions for graph polynomials
  - [ ] Use BLOCK 2, 3, 9
  - [ ] Analyze recursive graphs symbolically
- [ ] P4: Symbolic recurrences for graph families
  - [ ] Use BLOCK 2, 3, 5, 8
- [ ] P5: Symbolic isomorphism detection
  - [ ] Use BLOCK 1, 3, 6, 7
- [ ] P6: Graphs avoiding subgraphs
  - [ ] Use BLOCK 2, 4, 5
  - [ ] Enumerate and classify triangle-free, K₄-free
- [ ] P7: Discover new graph statistics
  - [ ] Use BLOCK 3, 5, 8, 9
  - [ ] Define, visualize new symbolic invariants
- [ ] P8: Graph transformation and limit behavior
  - [ ] Use BLOCK 2, 4, 10
