Model Creation Supporting Tools
===============================

Model Creation Tools
--------------------

Effective application of EIRA and eGovERA relies on appropriate tooling
to support modelling, collaboration, and reuse. A set of complementary
tools - Archi, coArchi, and the Cartography Tool (CarTool) - provides a
practical environment for developing, managing, and sharing architecture
models aligned with European interoperability standards. Links to access
the tools mentioned in this chapter can be found in annex 8.3.

Archi Modelling Tool
~~~~~~~~~~~~~~~~~~~~

Archi is an open-source ArchiMate® modelling toolkit designed to support
enterprise architects across different levels of expertise. It offers a
free, cross-platform solution that operates on Windows, macOS, and
Linux, making it accessible across diverse organisational environments.
Its functionality supports both structured modelling and early-stage
conceptual work. Several features enhance its usability and modelling
efficiency. The Magic Connector enables automatic creation of valid
relationships between elements, reducing modelling errors and improving
consistency. User-defined properties and custom colour schemes allow
adaptation to organisational standards and improve readability. The
ability to create tailored views and viewpoints supports communication
with different stakeholder groups, ensuring that complex architectures
can be presented in a targeted and understandable way. In addition,
Archi includes tools that support both learning and analysis. The Hints
View provides contextual explanations of modelling elements and
relationships, which is particularly useful for less experienced users.
The Visualiser offers a radial-tree representation of relationships
between elements, enabling architects to explore dependencies and
impacts more effectively. For early design stages, the Sketch View
provides a flexible, informal space for brainstorming, while the Canvas
Modelling Toolkit allows the creation of reusable templates that support
collaborative or pre-design activities. Archi can be download and
installed from its website. Please check chapter 8 for the link to the
official website.

coArchi
~~~~~~~

Extends Archi by enabling shared model development through a
repository-based approach. It supports versioning and distributed
collaboration by integrating with a Git-based repository. This allows
multiple contributors to work on the same model while maintaining
traceability of changes. The workflow typically involves setting up a
repository, cloning it locally, and creating or updating models within
that environment. Changes can be committed locally and later published
to the shared repository. In cases where multiple users modify the same
elements, coArchi provides conflict resolution mechanisms to reconcile
differences. This approach supports both offline work and controlled
synchronisation, which is particularly relevant in distributed or
multi-organisational contexts. Please check chapter 8 for the link to
the official website.

Cartography Tool (Cartool)
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Cartography Tool (CarTool) is a specialised open-source plugin for
the Archi modelling tool. It is designed to operationalise the European
Interoperability Reference Architecture (EIRA) within enterprise
architecture practice, providing first-class support for the EIRA and
eGovERA modelling vocabulary, artefact structures, and viewpoints. As a
plugin, CarTool extends Archi with EIRA-specific capabilities, enabling
architects to create, navigate, and manage models that conform to the
EIRA structure. It introduces direct support for Architecture Building
Blocks (ABBs) which are the abstract, reusable capability elements
defined by EIRA and their corresponding Solution Building Blocks (SBBs),
which represent their concrete instantiation within specific solutions
or Solution Architecture Templates (SATs). The details on installation
and usage of CarTool are provided in detail in the CarTool user guide
are provided in the section 8.4.

*Purpose:*

The primary purpose of CarTool is to serve as the principal modelling
instrument through which EIRA and eGovERA are applied in practice. It
meets the demand from Member States and European Institutions for a tool
with which architects can model solutions in conformance with EIRA as a
standard reference architecture and implement National or
domain-specific Cartographies following the EIRA and eGovERA structure.

*Architectural Challenges solved by Cartool:*

CarTool directly addresses the following architectural challenges: (1)
Lack of modelling standardisation as without a structured tool,
modelling of ABBs and SBBs tends to diverge in notation, attribute
completeness, and structural conventions. CarTool enforces EIRA-defined
metadata schemas and artefact conventions, ensuring consistent
architectural expression. (2) Inconsistency across LOST views - EIRA
organises building blocks across Legal, Organisational, Semantic, and
technical views and CarTool enables architects to navigate and populate
these views in a structured manner, ensuring building blocks are
positioned in the correct interoperability layer and that cross-view
dependencies are made explicit. (3) Difficulty in aligning with EIRA as
it simplifies the EIRA complexity by providing in-tool access to EIRA
views, building block documentation, the European Library of
Interoperability Specifications (ELIS), and the European Library of
Architecture Principles (ELAP). (4) Challenges in reuse and governance
as it enables reuse by suggesting existing SBBs when modelling new
solutions, reducing duplication and improving architectural governance.

*Capabilities:*

CarTool provides the following high-level architectural capabilities.
(1) EIRA Viewpoint and Structural Support as it renders the full EIRA
view structure across Legal, Organisational, Semantic,
Technical-Application, and Technical-Infrastructure views, supporting
both analysis and design activities. (2) ABB and SBB Management as it
enables structured management of ABBs and their instantiation as SBBs,
automatically pre-populating required EIRA metadata attributes and
providing auto-completion suggestions from the European Interoperability
Cartography. (3) Interoperability Specification and Architecture
Principles access as it integrates ELIS and ELAP, allowing standards and
architecture principles to be browsed and applied directly within
solution and SAT models.

*Intervention Support:*

Within the eGovERA Model, CarTool provides specific support across the
architecture phases of an intervention (1) Modelling interventions
aligned with EIRA and eGovERA as it supports creation of solution models
and SATs grounded in eGovERA Reference Architecture. (2) Mapping ABBs to
SBBs as it enforces EIRA metadata population and records ABB-to-SBB
traceability, ensuring every solution component is traceable to an
identified capability requirement. (3) Evolution and impact analysis the
automatic update mechanism and Cartography synchronisation capabilities
support management of EIRA version changes such as the tabular query
facility enables architects to identify all solutions and SBBs affected
by a change to a given ABB or interoperability layer. (4) Consistency
across multiple interventions as it enforces a consistent modelling
baseline through EIRA-version control, reducing fragmentation across
parallel intervention models.

Taken together, these tools form an integrated ecosystem that supports
modelling, collaboration, and reuse within the EIRA and eGovERA context.
Their combined use enables more structured and consistent architecture
development. However, their successful adoption depends on
organisational maturity, user capability, and the establishment of clear
governance practices.

Test and Conformance Using Interoperability Test Bed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Overview of the Interoperability Test Bed*

The Interoperability Test Bed is an online, intuitive, and self-service
platform for conformance testing of IT systems and artefacts against
semantic and technical specifications. It is provided by the European
Commission through DG DIGIT and is based on the Generic Interoperability
Test Bed (GITB) standards and software stack, ensuring alignment with
European and international interoperability practices.

The platform is available both as a centrally managed service and as
self-hosted software, allowing organisations to adapt its deployment to
their governance, operational, and infrastructure requirements. Its
adoption spans European institutions, public administrations,
international organisations, academia, and industry, reflecting its role
as a shared interoperability testing capability across ecosystems.

The platform supports both formal conformance testing and lightweight
validation services, enabling its use across different levels of
maturity, from early architecture validation to operational system
testing.

*Purpose and Role in EIRA/eGovERA*

The effective application of EIRA and eGovERA requires not only the
creation of architecture models, but also their systematic validation
against the rules, structures, and interoperability principles defined
by the reference architecture (EIRA). In this context, the
Interoperability Test Bed provides the main testing and validation
environment used to assess the consistency and conformance of artefacts
produced during architecture development.

Within the scope of this Solution Architecture Framework, its primary
role is to support the validation of analysis and design models,
ensuring that the architecture remains aligned with EIRA and eGovERA
guidance before any implementation takes place. This position is
consistent with the lifecycle described in this document, where testing
supports the analysis and design phases through model validation, while
implementation interoperability testing belongs to later phases that are
outside the scope of EIRA and eGovERA.

*Role in Analysis and Design Phases*

Within the eGovERA methodology, the Interoperability Test Bed is
primarily used to validate architecture models rather than executable
systems. During the analysis phase, it supports the validation of
Architecture Building Blocks (ABBs), their representation, properties,
and their relationships across the LOST views. This ensures that
requirements are complete, consistently modelled, and aligned with
EIRA/eGovERA principles.

During the design phase, the Test Bed supports the validation of
Solution Building Blocks (SBBs), including their correct identification
and properties, their relationships with other solution elements, and
their traceability to the ABBs defined in the analysis phase. In this
context, validation ensures that the architecture model is not only
structurally correct, but also coherent and ready for implementation.

The objective of these activities is to confirm that the model is
complete, that all relevant EIRA/eGovERA aspects are covered, and that
traceability between requirements and solutions is preserved. This
reduces the risk of inconsistencies propagating into later stages of the
lifecycle.

*EIRA Validator and Model Conformance*

A central mechanism for validation is the EIRA Validator, provided
within the Interoperability Test Bed. The EIRA Validator enables the
verification of EIRA and eGovERA models against predefined validation
profiles, ensuring that they conform to expected modelling conventions
and architectural rules.

The validation process combines structural and semantic checks.
Structural validation is performed using XML Schema, ensuring that the
model follows the required format and structure. Semantic validation is
performed using Schematron rules, which verify that elements,
relationships, and modelling patterns are used in accordance with EIRA
and eGovERA specifications.

Through this process, the validator ensures that all relevant
interoperability perspectives are addressed, that modelling rules are
consistently applied, and that traceability between requirements and
solution elements is preserved. This contributes to making architecture
models machine-readable, verifiable, and reusable.

*Role in Specification Development and Refinement*

Beyond model validation, the Interoperability Test Bed supports the
development and refinement of interoperability specifications. By
enabling specifications to be tested through executable validation logic
and test scenarios, it allows architects and stakeholders to verify
their clarity, completeness, and applicability.

This capability is particularly relevant in the eGovERA context, where
architectures rely on reusable standards, interoperability enablers, and
shared specifications. The ability to test and refine these
specifications contributes to improving their quality and ensuring that
they can be effectively implemented in practice.

In this way, the Test Bed supports a feedback loop between architecture
definition, specification refinement, and implementation readiness.

*Additional Capabilities and Use Cases*

In addition to its role in architecture validation, the Interoperability
Test Bed provides a broad set of capabilities supporting the lifecycle
of interoperable solutions. These include formal conformance testing,
data validation, integration testing, and testing during solution
development, such as validating APIs, messages, and data exchanges.

The platform can also support public procurement processes by verifying
that proposed solutions comply with defined requirements and
specifications. Furthermore, it enables data quality assurance by
validating that exchanged data is complete, consistent, and correctly
structured.

These capabilities extend the role of the Test Bed beyond architecture
modelling, supporting the transition from design to implementation and
operation while maintaining alignment with interoperability standards.

*Scope within EIRA/eGovERA*

It is important to distinguish between the use of the Interoperability
Test Bed within the scope of eGovERA and its broader use in the
implementation lifecycle.

Within the scope of this framework, the Test Bed is used to validate
analysis and design models, ensuring that Architecture Building Blocks
and Solution Building Blocks are correctly defined, related, and aligned
with EIRA and eGovERA specifications.

Outside this scope, the same platform supports testing of implemented
systems, including API validation, system integration testing, and
operational interoperability testing. These activities become relevant
once solution components have been realised and deployed and therefore
fall outside the architecture-focused scope of this document.

*Support Ecosystem and Lifecycle Integration*

The Interoperability Test Bed is supported by a comprehensive ecosystem
that includes documentation, tutorials, technical support, and regular
updates. This ecosystem enables organisations to adopt and use the
platform effectively across different stages of maturity.

Within the lifecycle defined in this document, the Test Bed plays a dual
role. It acts as a validation environment for architecture artefacts
during the analysis and design phases, and as part of a broader
interoperability testing ecosystem supporting later stages of solution
development.

This ensures continuity from architecture validation to solution
implementation, while maintaining a clear distinction between activities
that fall within the scope of eGovERA and those that belong to
subsequent implementation phases.



