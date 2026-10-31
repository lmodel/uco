// The site's values and options, in one place. scripts/config.mjs reads this
// file, fills in every option left out, settles each "auto" against the
// repository and checks the required values. `node scripts/config.mjs`
// prints the result. Nothing here runs code, so the pages that show the
// title import it too.
//
// The first five values are required. The rest are optional: leave one out,
// or set it to "auto", and the site shows that part of the repository when
// the repository has it. Set it to null to leave that part out.

// The repository, as owner/name, and the site's address: the owner's GitHub
// Pages domain and the path under it. A user site (the <owner>.github.io
// repository) or a custom domain sets BASE to "".
export const REPO = "lmodel/uco";
export const SITE = "https://lmodel.github.io";
export const BASE = "/uco";

// The site's title, in the header and on every social card, and its
// description, for search engines and as the home page's tagline when
// HOME.tagline is not set.
export const TITLE = "uco";
export const DESCRIPTION = "Unified Cyber Ontology (UCO) 1.5.0 (LinkML)";

// The branch an "Edit page" link opens.
export const BRANCH = "main";

// A custom domain, which the sync writes to public/CNAME, or null for a
// Pages address. The site leaves the domain's DNS to the repository.
export const CUSTOM_DOMAIN = null;

// The logo, as paths from the repository root: a light version, a dark one
// (the light one again when left out) and a favicon (the light logo when it
// is an SVG, else the site's own ladder mark). "auto" takes the Knowledge
// Trust Ladder logo: a knowledge-trust-ladder-logo.svg the repository
// already has, or else the copy in src/assets/. A single path is the light
// version alone. null shows the title as text.
//   export const LOGO = { light: ".assets/logo.svg", dark: ".assets/logo-dark.svg" };
export const LOGO = "auto";

// The folder of figures the README and the docs pages show, served under
// /assets/. "auto" takes .assets/ when there is one.
export const ASSETS = "auto";

// The docs pages: a folder, the sidebar groups its pages sit in (each page
// named by its path under the folder, without .md), and the paths under the
// folder that are not pages of the site, each a file or a folder. With no
// groups, every page sits in one Guides group, by title, with the folder's
// index.md first as its Overview. With groups, the sync stops with an error
// when a group names a missing page or a page has no group, so a new page
// cannot go missing from the sidebar. "auto" takes docs/ when there is one.
// null shows no docs pages.
//   export const DOCS = { dir: "docs", groups: [{ label: "Guides", pages: ["install", "usage"] }], exclude: ["templates-linkml"] };
export const DOCS = { dir: "docs", exclude: ["templates-linkml"] };

// Old addresses under BASE, each redirected to a page of the site, such as
// the addresses a retired mkdocs site gave its pages and a w3id rule still
// names. An entry whose key and value both end in /[...slug] stands for one
// redirect per schema page.
//   export const REDIRECTS = { "/elements": "/schema/", "/elements/[...slug]": "/schema/[...slug]", "/about": "/docs/about/" };
export const REDIRECTS = {
  // The retired mkdocs site of this repository.
  "/elements": "/schema/",
  "/elements/[...slug]": "/schema/[...slug]",
  "/about": "/docs/about/",
  // The sixteen retired uco-* sites served each element of their 2023
  // schemas; the w3id rules send those addresses here, under /elements/.
  // An element whose name the schema keeps has its page through the
  // [...slug] entry. These are the others: a name that changed only in
  // case, a vocabulary the old schemas named ...Enum, an XSD type, a name
  // the old schemas misspelled, and a uco-tool property the old schema
  // marked with an underscore, each to its successor; the rest, with no
  // successor, to the schema index.
  "/elements/_cpeid": "/schema/cpeid/",
  "/elements/_creator": "/schema/creator/",
  "/elements/_endTime": "/schema/",
  "/elements/_index": "/schema/co_index/",
  "/elements/_object": "/schema/",
  "/elements/_references": "/schema/references/",
  "/elements/_startTime": "/schema/",
  "/elements/_swid": "/schema/swid/",
  "/elements/_value": "/schema/",
  "/elements/_version": "/schema/version/",
  "/elements/AccountTypeEnum": "/schema/AccountTypeVocab/",
  "/elements/ActionArgumentNameEnum": "/schema/ActionArgumentNameVocab/",
  "/elements/ActionNameEnum": "/schema/ActionNameVocab/",
  "/elements/ActionRelationshipTypeEnum": "/schema/ActionRelationshipTypeVocab/",
  "/elements/ActionStatusTypeEnum": "/schema/ActionStatusTypeVocab/",
  "/elements/ActionTypeEnum": "/schema/ActionTypeVocab/",
  "/elements/Android": "/schema/",
  "/elements/Base64BinaryType": "/schema/UcoBase64Binary/",
  "/elements/BitnessEnum": "/schema/BitnessVocab/",
  "/elements/BlackBerryPhone": "/schema/BlackberryPhone/",
  "/elements/BooleanType": "/schema/",
  "/elements/ByteType": "/schema/UcoByte/",
  "/elements/CharacterEncodingEnum": "/schema/CharacterEncodingVocab/",
  "/elements/collections": "/schema/",
  "/elements/ContactAddressScopeEnum": "/schema/ContactAddressScopeVocab/",
  "/elements/ContactEmailScopeEnum": "/schema/ContactEmailScopeVocab/",
  "/elements/ContactPhoneEnum": "/schema/",
  "/elements/ContactPhoneScopeEnum": "/schema/ContactPhoneScopeVocab/",
  "/elements/ContactSIPScopeEnum": "/schema/ContactSIPScopeVocab/",
  "/elements/ContactURLScopeEnum": "/schema/ContactURLScopeVocab/",
  "/elements/DecimalType": "/schema/",
  "/elements/DiskTypeEnum": "/schema/DiskTypeVocab/",
  "/elements/DurationType": "/schema/UcoDuration/",
  "/elements/element": "/schema/",
  "/elements/EndiannessTypeEnum": "/schema/EndiannessTypeVocab/",
  "/elements/geoLocationAddress": "/schema/geolocationAddress/",
  "/elements/HashNameEnum": "/schema/HashNameVocab/",
  "/elements/HexBinaryType": "/schema/UcoHexBinary/",
  "/elements/httpMessageBodyLength": "/schema/",
  "/elements/identifier": "/schema/Identifier/",
  "/elements/IriType": "/schema/",
  "/elements/LibraryTypeEnum": "/schema/LibraryTypeVocab/",
  "/elements/Linux": "/schema/",
  "/elements/list": "/schema/List/",
  "/elements/listItem": "/schema/ListItem/",
  "/elements/LiteralType": "/schema/",
  "/elements/MemoryBlockTypeEnum": "/schema/MemoryBlockTypeVocab/",
  "/elements/messageThreadOrderedItems": "/schema/",
  "/elements/messageThreadOriginItems": "/schema/",
  "/elements/messageThreadTerminalItems": "/schema/",
  "/elements/messageThreadUnorderedItems": "/schema/",
  "/elements/mftFileNameRecordChangeTme": "/schema/mftFileNameRecordChangeTime/",
  "/elements/Microsoft": "/schema/",
  "/elements/nativeFormatString": "/schema/NativeFormatString/",
  "/elements/NetworkSocketAddressFamilyEnum": "/schema/NetworkSocketAddressFamily/",
  "/elements/NetworkSocketProtocolFamilyEnum": "/schema/NetworkSocketProtocolFamily/",
  "/elements/NetworkSocketTypeEnum": "/schema/NetworkSocketType/",
  "/elements/NonNegativeIntegerType": "/schema/UcoNonNegativeInteger/",
  "/elements/ObservableObjectRelationshipEnum": "/schema/ObservableObjectRelationshipVocab/",
  "/elements/ObservableObjectStateEnum": "/schema/ObservableObjectStateVocab/",
  "/elements/obSize": "/schema/",
  "/elements/PartitionTypeEnum": "/schema/PartitionTypeVocab/",
  "/elements/PositiveInteger": "/schema/UcoPositiveInteger/",
  "/elements/PositiveIntegerType": "/schema/UcoPositiveInteger/",
  "/elements/ProcessorArchEnum": "/schema/ProcessorArchVocab/",
  "/elements/RecoveredObjectStatusEnum": "/schema/RecoveredObjectStatusVocab/",
  "/elements/referrerURL": "/schema/referrerUrl/",
  "/elements/RegionalRegistry_typeVocab": "/schema/",
  "/elements/RegionalRegistryTypeEnum": "/schema/RegionalRegistryTypeVocab/",
  "/elements/RegistryDatatypeEnum": "/schema/RegistryDatatypeVocab/",
  "/elements/servicStatus": "/schema/serviceStatus/",
  "/elements/Set": "/schema/",
  "/elements/SIMFormEnum": "/schema/SIMFormVocab/",
  "/elements/SIMTypeEnum": "/schema/SIMTypeVocab/",
  "/elements/SIPAaddress": "/schema/SIPAddress/",
  "/elements/StatementType": "/schema/",
  "/elements/StringType": "/schema/",
  "/elements/structuredText": "/schema/StructuredText/",
  "/elements/TaskActionTypeEnum": "/schema/TaskActionTypeVocab/",
  "/elements/TaskFlagEnum": "/schema/TaskFlagVocab/",
  "/elements/TaskPriorityEnum": "/schema/TaskPriorityVocab/",
  "/elements/TaskStatusEnum": "/schema/TaskStatusVocab/",
  "/elements/Thing": "/schema/",
  "/elements/ThreadRunningStatusEnum": "/schema/ThreadRunningStatusVocab/",
  "/elements/TimeStamp": "/schema/Timestamp/",
  "/elements/TimestampPrecisionEnum": "/schema/TimestampPrecisionVocab/",
  "/elements/TrendEnum": "/schema/TrendVocab/",
  "/elements/TriggerFrequencyEnum": "/schema/TriggerFrequencyVocab/",
  "/elements/TriggerFrequencyEunum": "/schema/TriggerFrequencyVocab/",
  "/elements/TriggerTypeEnum": "/schema/TriggerTypeVocab/",
  "/elements/types": "/schema/",
  "/elements/uco-action": "/schema/",
  "/elements/uco-analysis": "/schema/",
  "/elements/uco-configuration": "/schema/",
  "/elements/uco-core": "/schema/",
  "/elements/uco-identity": "/schema/",
  "/elements/uco-marking": "/schema/",
  "/elements/uco-master": "/schema/",
  "/elements/uco-observable": "/schema/",
  "/elements/uco-role": "/schema/",
  "/elements/uco-time": "/schema/",
  "/elements/uco-tool": "/schema/",
  "/elements/uco-types": "/schema/",
  "/elements/uco-victim": "/schema/",
  "/elements/ucolink-location": "/schema/",
  "/elements/ucolink-pattern": "/schema/",
  "/elements/ucolink-vocabulary": "/schema/",
  "/elements/UnixProcessStateEnum": "/schema/UnixProcessStateVocab/",
  "/elements/UnsignedIntegerType": "/schema/UcoUnsignedInt/",
  "/elements/UnsignedShortType": "/schema/UcoUnsignedShort/",
  "/elements/URLTransitionTypeEnum": "/schema/URLTransitionTypeVocab/",
  "/elements/Whois": "/schema/WhoIs/",
  "/elements/WhoisContactTypeEnum": "/schema/WhoisContactTypeVocab/",
  "/elements/WhoisDNSSECTypeEnum": "/schema/WhoisDNSSECTypeVocab/",
  "/elements/WhoisFacet": "/schema/WhoIsFacet/",
  "/elements/WhoisStatusTypeEnum": "/schema/WhoisStatusTypeVocab/",
  "/elements/WindowsDriveTypeEnum": "/schema/WindowsDriveTypeVocab/",
  "/elements/WindowsFileMapping": "/schema/WindowsFilemapping/",
  "/elements/WindowsMailSlot": "/schema/WindowsMailslot/",
  "/elements/WindowsNetworkSecurityModeEnum": "/schema/",
  "/elements/WindowsPEBinaryTypeEnum": "/schema/WindowsPEBinaryType/",
  "/elements/WindowsPEFileHheader": "/schema/WindowsPEFileHeader/",
  "/elements/WindowsRegistrykeyFacet": "/schema/WindowsRegistryKeyFacet/",
  "/elements/WindowsServiceStartTypeEnum": "/schema/WindowsServiceStartType/",
  "/elements/WindowsServiceStatusEnum": "/schema/WindowsServiceStatus/",
  "/elements/WindowsServiceTypeEnum": "/schema/WindowsServiceType/",
  "/elements/WindowsVolumeAttributeEnum": "/schema/WindowsVolumeAttributeVocab/",
  "/elements/WirelessNetworkSecurityModeEnum": "/schema/WirelessNetworkSecurityModeVocab/",
};

// A Keep a Changelog file, read as a page per release. "auto" takes
// CHANGELOG.md when it holds a released version.
export const CHANGELOG = "auto";

// The tag a release carries, with {version} for its number. A release page
// links the repository, the docs and the bundle at that tag, and the release
// itself, when git has the tag. A repository whose tags carry no "v" sets
// "{version}". null links nothing.
export const RELEASE_TAG = "v{version}";

// Pages from files outside the docs folder, each at /<slug>/, listed in the
// Guide sidebar after Home under its label. An entry's `retells` names the
// file whose page it retells, and `level` the words for its reading level
// (the label when left out): both pages then offer each other under their
// titles.
//   export const PAGES = [{ slug: "simple", source: "docs/overview.en-simple.md", label: "In short", retells: "docs/overview.md" }];
export const PAGES = [];

// The LinkML schema's pages, which gen-doc writes, under a Schema topic: a
// folder, and the command that writes it, which the sync runs when the
// folder is missing. "auto" takes the first of the root, a linkmo project
// and .linkml/ whose justfile has a gen-doc recipe. null shows no schema.
//   export const SCHEMA = { dir: "docs/elements", build: "just gen-doc" };
export const SCHEMA = "auto";

// The data: a folder of SQLite databases and their Datasette metadata, served
// under /browse/ with a page that opens each in Datasette Lite, and the
// command that writes it. The databases go on the public site, so it is null
// until set. "auto" takes a linkmo project's browse/ folder.
//   export const BROWSE = { dir: "browse", build: "just build-browse" };
export const BROWSE = null;

// The workspace of a domain host, which the knowledge-federation workflow
// serves at workspace/ under the site, and which the graph page offers to
// draw beside the bundle's own graph. "auto" offers it when the repository
// has that workflow; true offers it always, and null never.
export const WORKSPACE = "auto";

// The home page: its source, from the file's `# ` title down ("auto" takes
// the README when it has one, else the bundle's own introduction); the
// tagline under the title (a string, { boldLineOf: <file> } for the first
// line of that file that is bold throughout, or DESCRIPTION when null); and
// the buttons, with site-relative links (Browse the bundle, Architecture when
// the docs have an architecture page, Schema when the site shows the schema,
// Bundle health and Knowledge graph when null).
export const HOME = { source: "auto", tagline: null, actions: null };
