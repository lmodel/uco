# Auto generated from uco.yaml by pythongen.py version: 0.0.1
# Schema: uco
#
# id: https://w3id.org/lmodel/uco
# description: A LinkML rendering of the Unified Cyber Ontology (UCO) 1.5.0: one module per UCO namespace and one for the Collections Ontology terms UCO uses, with every class, property and vocabulary keeping its UCO IRI.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Datetime, Decimal, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URI, URIorCURIE, XSDDateTime

metamodel_version = "1.12.0"
version = "1.5.0"

# Namespaces
COLL = CurieNamespace('coll', 'http://purl.org/co/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
UCO_ACTION = CurieNamespace('uco-action', 'https://ontology.unifiedcyberontology.org/uco/action/')
UCO_ANALYSIS = CurieNamespace('uco-analysis', 'https://ontology.unifiedcyberontology.org/uco/analysis/')
UCO_CONFIGURATION = CurieNamespace('uco-configuration', 'https://ontology.unifiedcyberontology.org/uco/configuration/')
UCO_CORE = CurieNamespace('uco-core', 'https://ontology.unifiedcyberontology.org/uco/core/')
UCO_IDENTITY = CurieNamespace('uco-identity', 'https://ontology.unifiedcyberontology.org/uco/identity/')
UCO_LOCATION = CurieNamespace('uco-location', 'https://ontology.unifiedcyberontology.org/uco/location/')
UCO_MARKING = CurieNamespace('uco-marking', 'https://ontology.unifiedcyberontology.org/uco/marking/')
UCO_OBSERVABLE = CurieNamespace('uco-observable', 'https://ontology.unifiedcyberontology.org/uco/observable/')
UCO_PATTERN = CurieNamespace('uco-pattern', 'https://ontology.unifiedcyberontology.org/uco/pattern/')
UCO_ROLE = CurieNamespace('uco-role', 'https://ontology.unifiedcyberontology.org/uco/role/')
UCO_TIME = CurieNamespace('uco-time', 'https://ontology.unifiedcyberontology.org/uco/time/')
UCO_TOOL = CurieNamespace('uco-tool', 'https://ontology.unifiedcyberontology.org/uco/tool/')
UCO_TYPES = CurieNamespace('uco-types', 'https://ontology.unifiedcyberontology.org/uco/types/')
UCO_VICTIM = CurieNamespace('uco-victim', 'https://ontology.unifiedcyberontology.org/uco/victim/')
UCO_VOCABULARY = CurieNamespace('uco-vocabulary', 'https://ontology.unifiedcyberontology.org/uco/vocabulary/')
UCO_LINKML = CurieNamespace('uco_linkml', 'https://w3id.org/lmodel/uco/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = UCO_LINKML


# Types
class UcoBase64Binary(String):
    """ XSD's base64Binary: binary data in the Base64 alphabet, padded with =. """
    type_class_uri = XSD["base64Binary"]
    type_class_curie = "xsd:base64Binary"
    type_name = "uco_base64_binary"
    type_model_uri = UCO_LINKML.UcoBase64Binary


class UcoByte(Integer):
    """ XSD's byte: an integer from -128 to 127. """
    type_class_uri = XSD["byte"]
    type_class_curie = "xsd:byte"
    type_name = "uco_byte"
    type_model_uri = UCO_LINKML.UcoByte


class UcoDuration(String):
    """ XSD's duration: a length of time such as P1DT2H, in ISO 8601's form. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "uco_duration"
    type_model_uri = UCO_LINKML.UcoDuration


class UcoHexBinary(String):
    """ XSD's hexBinary: binary data as pairs of hexadecimal digits. """
    type_class_uri = XSD["hexBinary"]
    type_class_curie = "xsd:hexBinary"
    type_name = "uco_hex_binary"
    type_model_uri = UCO_LINKML.UcoHexBinary


class UcoNonNegativeInteger(Integer):
    """ XSD's nonNegativeInteger: an integer of zero or more. """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "uco_non_negative_integer"
    type_model_uri = UCO_LINKML.UcoNonNegativeInteger


class UcoPositiveInteger(Integer):
    """ XSD's positiveInteger: an integer of one or more. """
    type_class_uri = XSD["positiveInteger"]
    type_class_curie = "xsd:positiveInteger"
    type_name = "uco_positive_integer"
    type_model_uri = UCO_LINKML.UcoPositiveInteger


class UcoUnsignedInt(Integer):
    """ XSD's unsignedInt: an integer from 0 to 4294967295. """
    type_class_uri = XSD["unsignedInt"]
    type_class_curie = "xsd:unsignedInt"
    type_name = "uco_unsigned_int"
    type_model_uri = UCO_LINKML.UcoUnsignedInt


class UcoUnsignedShort(Integer):
    """ XSD's unsignedShort: an integer from 0 to 65535. """
    type_class_uri = XSD["unsignedShort"]
    type_class_curie = "xsd:unsignedShort"
    type_name = "uco_unsigned_short"
    type_model_uri = UCO_LINKML.UcoUnsignedShort


class Time(String):
    """ UCO 1.5.0 declares the datatype uco-time:Time without a definition. """
    type_class_uri = UCO_TIME["Time"]
    type_class_curie = "uco-time:Time"
    type_name = "Time"
    type_model_uri = UCO_LINKML.Time


class TimeRange(String):
    """ UCO 1.5.0 declares the datatype uco-time:TimeRange without a definition. """
    type_class_uri = UCO_TIME["TimeRange"]
    type_class_curie = "uco-time:TimeRange"
    type_name = "TimeRange"
    type_model_uri = UCO_LINKML.TimeRange


class Timestamp(String):
    """ UCO 1.5.0 declares the datatype uco-time:Timestamp without a definition. """
    type_class_uri = UCO_TIME["Timestamp"]
    type_class_curie = "uco-time:Timestamp"
    type_name = "Timestamp"
    type_model_uri = UCO_LINKML.Timestamp


class Identifier(String):
    """ An identifier is a string conformant to the specified UUID-based format for UCO object identifiers. """
    type_class_uri = UCO_TYPES["Identifier"]
    type_class_curie = "uco-types:Identifier"
    type_name = "Identifier"
    type_model_uri = UCO_LINKML.Identifier


class NativeFormatString(String):
    """ Specifies data in its native format of some external language. The data may be encoded in Base64 per [RFC4648]. Data encoded in Base64 must be denoted as such using the encoded property. """
    type_class_uri = UCO_TYPES["NativeFormatString"]
    type_class_curie = "uco-types:NativeFormatString"
    type_name = "NativeFormatString"
    type_model_uri = UCO_LINKML.NativeFormatString


class StructuredText(String):
    """ Expresses string-based data in some information structuring format (e.g., HTML5). """
    type_class_uri = UCO_TYPES["StructuredText"]
    type_class_curie = "uco-types:StructuredText"
    type_name = "StructuredText"
    type_model_uri = UCO_LINKML.StructuredText


# Class references
class UcoObjectId(URIorCURIE):
    pass


class AssertionId(UcoObjectId):
    pass


class AnnotationId(AssertionId):
    pass


class AttributedNameId(UcoObjectId):
    pass


class CompilationId(UcoObjectId):
    pass


class ContextualCompilationId(CompilationId):
    pass


class ControlledVocabularyId(UcoObjectId):
    pass


class EnclosingCompilationId(CompilationId):
    pass


class BundleId(EnclosingCompilationId):
    pass


class EventId(UcoObjectId):
    pass


class GroupingId(ContextualCompilationId):
    pass


class IdentityAbstractionId(UcoObjectId):
    pass


class ItemId(UcoObjectId):
    pass


class MarkingDefinitionAbstractionId(UcoObjectId):
    pass


class ModusOperandiId(UcoObjectId):
    pass


class RelationshipId(UcoObjectId):
    pass


class UcoTypeId(URIorCURIE):
    pass


class ConfigurationId(UcoObjectId):
    pass


class LocationId(UcoObjectId):
    pass


class IdentityId(IdentityAbstractionId):
    pass


class OrganizationId(IdentityId):
    pass


class PersonId(IdentityId):
    pass


class MarkingDefinitionId(MarkingDefinitionAbstractionId):
    pass


class PatternId(UcoObjectId):
    pass


class LogicalPatternId(PatternId):
    pass


class RoleId(UcoObjectId):
    pass


class BenevolentRoleId(RoleId):
    pass


class MaliciousRoleId(RoleId):
    pass


class NeutralRoleId(RoleId):
    pass


class ToolId(UcoObjectId):
    pass


class AnalyticToolId(ToolId):
    pass


class ConfiguredToolId(ToolId):
    pass


class DefensiveToolId(ToolId):
    pass


class MaliciousToolId(ToolId):
    pass


class VictimId(NeutralRoleId):
    pass


class VictimTargetingId(VictimId):
    pass


class ThreadId(URIorCURIE):
    pass


class ThreadItemId(URIorCURIE):
    pass


class ActionId(UcoObjectId):
    pass


class ActionLifecycleId(ActionId):
    pass


class ActionPatternId(ActionId):
    pass


class TechniqueId(UcoTypeId):
    pass


class AnalysisId(ActionId):
    pass


class AnalyticResultId(AssertionId):
    pass


class ObservableId(UcoObjectId):
    pass


class ObservableActionId(ObservableId):
    pass


class ObservableObjectId(ObservableId):
    pass


class APIId(ObservableObjectId):
    pass


class ARPCacheId(ObservableObjectId):
    pass


class ARPCacheEntryId(ObservableObjectId):
    pass


class AccountId(ObservableObjectId):
    pass


class AddressId(ObservableObjectId):
    pass


class AlternateDataStreamId(ObservableObjectId):
    pass


class ApplicationId(ObservableObjectId):
    pass


class AudioId(ObservableObjectId):
    pass


class AutonomousSystemId(ObservableObjectId):
    pass


class BotConfigurationId(ObservableObjectId):
    pass


class BrowserBookmarkId(ObservableObjectId):
    pass


class BrowserCookieId(ObservableObjectId):
    pass


class CalendarId(ObservableObjectId):
    pass


class CalendarEntryId(ObservableObjectId):
    pass


class CallId(ObservableObjectId):
    pass


class CapturedTelecommunicationsInformationId(ObservableObjectId):
    pass


class CellSiteId(ObservableObjectId):
    pass


class CodeId(ObservableObjectId):
    pass


class ComputerSpecificationId(ObservableObjectId):
    pass


class ContactId(ObservableObjectId):
    pass


class ContactListId(ObservableObjectId):
    pass


class ContentDataId(ObservableObjectId):
    pass


class CookieHistoryId(ObservableObjectId):
    pass


class CredentialId(ObservableObjectId):
    pass


class CredentialDumpId(ObservableObjectId):
    pass


class DNSCacheId(ObservableObjectId):
    pass


class DNSRecordId(ObservableObjectId):
    pass


class DeviceId(ObservableObjectId):
    pass


class AdaptorId(DeviceId):
    pass


class AndroidDeviceId(DeviceId):
    pass


class AppleDeviceId(DeviceId):
    pass


class ApplianceId(DeviceId):
    pass


class ComputerId(DeviceId):
    pass


class DigitalAccountId(AccountId):
    pass


class ApplicationAccountId(DigitalAccountId):
    pass


class DigitalAddressId(AddressId):
    pass


class DigitalCameraId(DeviceId):
    pass


class DigitalSignatureInfoId(ObservableObjectId):
    pass


class DiskId(ObservableObjectId):
    pass


class DiskPartitionId(ObservableObjectId):
    pass


class DomainNameId(ObservableObjectId):
    pass


class EmailAccountId(DigitalAccountId):
    pass


class EmailAddressId(DigitalAddressId):
    pass


class EmbeddedDeviceId(DeviceId):
    pass


class EventLogId(ObservableObjectId):
    pass


class EventRecordId(ObservableObjectId):
    pass


class FileSystemId(ObservableObjectId):
    pass


class FileSystemObjectId(ObservableObjectId):
    pass


class BlockDeviceNodeId(FileSystemObjectId):
    pass


class CharacterDeviceNodeId(FileSystemObjectId):
    pass


class DirectoryId(FileSystemObjectId):
    pass


class FileId(FileSystemObjectId):
    pass


class ArchiveFileId(FileId):
    pass


class GUIId(ObservableObjectId):
    pass


class GamingConsoleId(DeviceId):
    pass


class GenericObservableObjectId(ObservableObjectId):
    pass


class GeoLocationEntryId(ObservableObjectId):
    pass


class GeoLocationLogId(ObservableObjectId):
    pass


class GeoLocationTrackId(ObservableObjectId):
    pass


class HostnameId(ObservableObjectId):
    pass


class IPAddressId(DigitalAddressId):
    pass


class IPNetmaskId(ObservableObjectId):
    pass


class IPv4AddressId(IPAddressId):
    pass


class IPv6AddressId(IPAddressId):
    pass


class ImageId(ObservableObjectId):
    pass


class InstantMessagingAddressId(DigitalAddressId):
    pass


class JunctionId(FileSystemObjectId):
    pass


class LaptopId(ComputerId):
    pass


class LibraryId(ObservableObjectId):
    pass


class MACAddressId(DigitalAddressId):
    pass


class BluetoothAddressId(MACAddressId):
    pass


class MemoryId(ObservableObjectId):
    pass


class MessageId(ObservableObjectId):
    pass


class EmailMessageId(MessageId):
    pass


class ForumPostId(MessageId):
    pass


class ForumPrivateMessageId(MessageId):
    pass


class MessageThreadId(ObservableObjectId):
    pass


class MobileAccountId(DigitalAccountId):
    pass


class MobileDeviceId(DeviceId):
    pass


class DroneId(MobileDeviceId):
    pass


class MobilePhoneId(MobileDeviceId):
    pass


class MutexId(ObservableObjectId):
    pass


class NTFSFileId(FileId):
    pass


class NamedPipeId(FileSystemObjectId):
    pass


class NetworkApplianceId(ApplianceId):
    pass


class NetworkConnectionId(ObservableObjectId):
    pass


class HTTPConnectionId(NetworkConnectionId):
    pass


class ICMPConnectionId(NetworkConnectionId):
    pass


class NetworkFlowId(ObservableObjectId):
    pass


class NetworkInterfaceId(ObservableObjectId):
    pass


class NetworkProtocolId(ObservableObjectId):
    pass


class NetworkRouteId(ObservableObjectId):
    pass


class NetworkSubnetId(ObservableObjectId):
    pass


class NoteId(ObservableObjectId):
    pass


class ObservablePatternId(ObservableId):
    pass


class ObservableRelationshipId(ObservableId):
    pass


class ObservationId(ActionId):
    pass


class OnlineServiceId(ObservableObjectId):
    pass


class OperatingSystemId(ObservableObjectId):
    pass


class PDFFileId(FileId):
    pass


class PaymentCardId(ObservableObjectId):
    pass


class PhoneAccountId(DigitalAccountId):
    pass


class PipeId(ObservableObjectId):
    pass


class PostId(MessageId):
    pass


class ProcessId(ObservableObjectId):
    pass


class ProcessThreadId(ObservableObjectId):
    pass


class ProfileId(ObservableObjectId):
    pass


class ProtocolConverterId(DeviceId):
    pass


class RasterPictureId(FileId):
    pass


class RecoveredObjectId(ObservableObjectId):
    pass


class ReparsePointId(FileSystemObjectId):
    pass


class SIMCardId(DeviceId):
    pass


class SIPAddressId(DigitalAddressId):
    pass


class SMSMessageId(MessageId):
    pass


class SQLiteBlobId(ObservableObjectId):
    pass


class SecurityApplianceId(ApplianceId):
    pass


class SemaphoreId(ObservableObjectId):
    pass


class ServerId(ComputerId):
    pass


class ShopListingId(ObservableObjectId):
    pass


class SmartDeviceId(DeviceId):
    pass


class SmartPhoneId(MobilePhoneId):
    pass


class AndroidPhoneId(SmartPhoneId):
    pass


class BlackberryPhoneId(SmartPhoneId):
    pass


class IPhoneId(SmartPhoneId):
    pass


class SnapshotId(FileSystemObjectId):
    pass


class SocketId(FileSystemObjectId):
    pass


class SocketAddressId(AddressId):
    pass


class SoftwareId(ObservableObjectId):
    pass


class ConfiguredSoftwareId(SoftwareId):
    pass


class StorageMediumId(DeviceId):
    pass


class SymbolicLinkId(FileSystemObjectId):
    pass


class TCPConnectionId(NetworkConnectionId):
    pass


class TableFieldId(ObservableObjectId):
    pass


class TabletId(ComputerId):
    pass


class TweetId(MessageId):
    pass


class UNIXAccountId(DigitalAccountId):
    pass


class UNIXFileId(FileId):
    pass


class UNIXProcessId(ProcessId):
    pass


class URLId(ObservableObjectId):
    pass


class URLHistoryId(ObservableObjectId):
    pass


class URLVisitId(ObservableObjectId):
    pass


class UserAccountId(DigitalAccountId):
    pass


class UserSessionId(ObservableObjectId):
    pass


class VolumeId(ObservableObjectId):
    pass


class WearableDeviceId(SmartDeviceId):
    pass


class WebPageId(ObservableObjectId):
    pass


class WhoIsId(ObservableObjectId):
    pass


class WifiAddressId(MACAddressId):
    pass


class WikiId(ObservableObjectId):
    pass


class WikiArticleId(ObservableObjectId):
    pass


class WindowsAccountId(DigitalAccountId):
    pass


class WindowsActiveDirectoryAccountId(DigitalAccountId):
    pass


class WindowsComputerSpecificationId(ObservableObjectId):
    pass


class WindowsCriticalSectionId(ObservableObjectId):
    pass


class WindowsEventId(ObservableObjectId):
    pass


class WindowsFilemappingId(ObservableObjectId):
    pass


class WindowsHandleId(ObservableObjectId):
    pass


class WindowsHookId(ObservableObjectId):
    pass


class WindowsMailslotId(ObservableObjectId):
    pass


class WindowsNetworkShareId(ObservableObjectId):
    pass


class WindowsPEBinaryFileId(FileId):
    pass


class WindowsPrefetchId(ObservableObjectId):
    pass


class WindowsProcessId(ProcessId):
    pass


class WindowsRegistryHiveId(ObservableObjectId):
    pass


class WindowsRegistryKeyId(ObservableObjectId):
    pass


class WindowsServiceId(ObservableObjectId):
    pass


class WindowsSystemRestoreId(ObservableObjectId):
    pass


class WindowsTaskId(ObservableObjectId):
    pass


class WindowsThreadId(ProcessThreadId):
    pass


class WindowsWaitableTimeId(ObservableObjectId):
    pass


class WirelessNetworkConnectionId(NetworkConnectionId):
    pass


class WriteBlockerId(DeviceId):
    pass


class X509CertificateId(ObservableObjectId):
    pass


class X509V3CertificateId(ObservableObjectId):
    pass


@dataclass(repr=False)
class UcoDocument(YAMLRoot):
    """
    A document of UCO data, as a JSON-LD file of UCO holds one graph.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_LINKML["UcoDocument"]
    class_class_curie: ClassVar[str] = "uco_linkml:UcoDocument"
    class_name: ClassVar[str] = "UcoDocument"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UcoDocument

    graph: Optional[Union[Union[dict, "UcoThing"], list[Union[dict, "UcoThing"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.graph, list):
            self.graph = [self.graph] if self.graph is not None else []
        self.graph = [v if isinstance(v, UcoThing) else UcoThing(**as_dict(v)) for v in self.graph]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bag(YAMLRoot):
    """
    A collection that may hold one element more than once, in no order.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COLL["Bag"]
    class_class_curie: ClassVar[str] = "coll:Bag"
    class_name: ClassVar[str] = "Bag"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Bag

    co_size: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.co_size is not None and not isinstance(self.co_size, int):
            self.co_size = int(self.co_size)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoItem(YAMLRoot):
    """
    An entry of a collection, which wraps one element of the collection's content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COLL["Item"]
    class_class_curie: ClassVar[str] = "coll:Item"
    class_name: ClassVar[str] = "CoItem"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CoItem

    itemContent: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.itemContent is not None and not isinstance(self.itemContent, str):
            self.itemContent = str(self.itemContent)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class List(YAMLRoot):
    """
    A collection whose items come in order, one after another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COLL["List"]
    class_class_curie: ClassVar[str] = "coll:List"
    class_name: ClassVar[str] = "List"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.List

    firstItem: Optional[Union[dict, "ListItem"]] = None
    item: Optional[Union[Union[dict, "ListItem"], list[Union[dict, "ListItem"]]]] = empty_list()
    lastItem: Optional[Union[dict, "ListItem"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.firstItem is not None and not isinstance(self.firstItem, ListItem):
            self.firstItem = ListItem(**as_dict(self.firstItem))

        if not isinstance(self.item, list):
            self.item = [self.item] if self.item is not None else []
        self.item = [v if isinstance(v, ListItem) else ListItem(**as_dict(v)) for v in self.item]

        if self.lastItem is not None and not isinstance(self.lastItem, ListItem):
            self.lastItem = ListItem(**as_dict(self.lastItem))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListItem(CoItem):
    """
    An item of a list, which has a place in the list's order.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COLL["ListItem"]
    class_class_curie: ClassVar[str] = "coll:ListItem"
    class_name: ClassVar[str] = "ListItem"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ListItem

    followedBy: Optional[Union[Union[dict, CoItem], list[Union[dict, CoItem]]]] = empty_list()
    index: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.followedBy, list):
            self.followedBy = [self.followedBy] if self.followedBy is not None else []
        self.followedBy = [v if isinstance(v, CoItem) else CoItem(**as_dict(v)) for v in self.followedBy]

        if self.index is not None and not isinstance(self.index, int):
            self.index = int(self.index)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UcoThing(YAMLRoot):
    """
    UcoThing is the top-level class for individuals within UCO.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["UcoThing"]
    class_class_curie: ClassVar[str] = "uco-core:UcoThing"
    class_name: ClassVar[str] = "UcoThing"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UcoThing

    type: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



class UcoInherentCharacterizationThing(UcoThing):
    """
    A UCO inherent characterization thing is a grouping of characteristics unique to a particular inherent aspect of a
    UCO domain object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["UcoInherentCharacterizationThing"]
    class_class_curie: ClassVar[str] = "uco-core:UcoInherentCharacterizationThing"
    class_name: ClassVar[str] = "UcoInherentCharacterizationThing"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UcoInherentCharacterizationThing


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Dictionary(UcoInherentCharacterizationThing):
    """
    A dictionary is list of (term/key, value) pairs with each term/key having an expectation to exist no more than
    once. types:Dictionary alone does not validate this expectation, but validation is available. For use cases where
    this expectation must be validated, the subclass types:ProperDictionary should be used instead of
    types:Dictionary. For instances where this expectation has been found to be violated, the subclass
    types:ImproperDictionary should be used instead of types:Dictionary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TYPES["Dictionary"]
    class_class_curie: ClassVar[str] = "uco-types:Dictionary"
    class_name: ClassVar[str] = "Dictionary"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Dictionary

    entry: Optional[Union[Union[dict, "DictionaryEntry"], list[Union[dict, "DictionaryEntry"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="entry", slot_type=DictionaryEntry, key_name="key", keyed=False)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DictionaryEntry(UcoInherentCharacterizationThing):
    """
    A dictionary entry is a single (term/key, value) pair.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TYPES["DictionaryEntry"]
    class_class_curie: ClassVar[str] = "uco-types:DictionaryEntry"
    class_name: ClassVar[str] = "DictionaryEntry"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DictionaryEntry

    key: str = None
    types_value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, str):
            self.key = str(self.key)

        if self._is_empty(self.types_value):
            self.MissingRequiredField("types_value")
        if not isinstance(self.types_value, str):
            self.types_value = str(self.types_value)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ExternalReference(UcoInherentCharacterizationThing):
    """
    Characteristics of a reference to a resource outside of the UCO.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["ExternalReference"]
    class_class_curie: ClassVar[str] = "uco-core:ExternalReference"
    class_name: ClassVar[str] = "ExternalReference"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ExternalReference

    definingContext: Optional[str] = None
    externalIdentifier: Optional[str] = None
    referenceURL: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.definingContext is not None and not isinstance(self.definingContext, str):
            self.definingContext = str(self.definingContext)

        if self.externalIdentifier is not None and not isinstance(self.externalIdentifier, str):
            self.externalIdentifier = str(self.externalIdentifier)

        if self.referenceURL is not None and not isinstance(self.referenceURL, URI):
            self.referenceURL = URI(self.referenceURL)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class Facet(UcoInherentCharacterizationThing):
    """
    A facet is a grouping of characteristics singularly unique to a particular inherent aspect of a UCO domain object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["Facet"]
    class_class_curie: ClassVar[str] = "uco-core:Facet"
    class_name: ClassVar[str] = "Facet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Facet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ConfidenceFacet(Facet):
    """
    A confidence is a grouping of characteristics unique to an asserted level of certainty in the accuracy of some
    information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["ConfidenceFacet"]
    class_class_curie: ClassVar[str] = "uco-core:ConfidenceFacet"
    class_name: ClassVar[str] = "ConfidenceFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ConfidenceFacet

    confidence: Union[int, UcoNonNegativeInteger] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.confidence):
            self.MissingRequiredField("confidence")
        if not isinstance(self.confidence, UcoNonNegativeInteger):
            self.confidence = UcoNonNegativeInteger(self.confidence)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UcoObject(UcoThing):
    """
    A UCO object is a representation of a fundamental concept either directly inherent to the cyber domain or
    indirectly related to the cyber domain and necessary for contextually characterizing cyber domain concepts and
    relationships. Within the Unified Cyber Ontology (UCO) structure this is the base class acting as a consistent,
    unifying and interoperable foundation for all explicit and inter-relatable content objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["UcoObject"]
    class_class_curie: ClassVar[str] = "uco-core:UcoObject"
    class_name: ClassVar[str] = "UcoObject"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UcoObject

    id: Union[str, UcoObjectId] = None
    createdBy: Optional[Union[str, IdentityAbstractionId]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    externalReference: Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]] = empty_list()
    hasFacet: Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    objectMarking: Optional[Union[Union[str, MarkingDefinitionAbstractionId], list[Union[str, MarkingDefinitionAbstractionId]]]] = empty_list()
    objectStatus: Optional[Union[str, "ObjectStatusVocab"]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UcoObjectId):
            self.id = UcoObjectId(self.id)

        if self.createdBy is not None and not isinstance(self.createdBy, IdentityAbstractionId):
            self.createdBy = IdentityAbstractionId(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, ExternalReference) else ExternalReference(**as_dict(v)) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, Facet) else Facet(**as_dict(v)) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstractionId) else MarkingDefinitionAbstractionId(v) for v in self.objectMarking]

        if self.objectStatus is not None and not isinstance(self.objectStatus, ObjectStatusVocab):
            self.objectStatus = ObjectStatusVocab(self.objectStatus)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Assertion(UcoObject):
    """
    An assertion is a statement declared to be true.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["Assertion"]
    class_class_curie: ClassVar[str] = "uco-core:Assertion"
    class_name: ClassVar[str] = "Assertion"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Assertion

    id: Union[str, AssertionId] = None
    statement: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssertionId):
            self.id = AssertionId(self.id)

        if not isinstance(self.statement, list):
            self.statement = [self.statement] if self.statement is not None else []
        self.statement = [v if isinstance(v, str) else str(v) for v in self.statement]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Annotation(Assertion):
    """
    An annotation is an assertion made in relation to one or more objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["Annotation"]
    class_class_curie: ClassVar[str] = "uco-core:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Annotation

    id: Union[str, AnnotationId] = None
    object: Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnnotationId):
            self.id = AnnotationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.object]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AttributedName(UcoObject):
    """
    An attributed name is a name of an entity issued by some attributed naming authority.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["AttributedName"]
    class_class_curie: ClassVar[str] = "uco-core:AttributedName"
    class_name: ClassVar[str] = "AttributedName"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AttributedName

    id: Union[str, AttributedNameId] = None
    namingAuthority: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AttributedNameId):
            self.id = AttributedNameId(self.id)

        if self.namingAuthority is not None and not isinstance(self.namingAuthority, str):
            self.namingAuthority = str(self.namingAuthority)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Compilation(UcoObject):
    """
    A compilation is a grouping of things.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["Compilation"]
    class_class_curie: ClassVar[str] = "uco-core:Compilation"
    class_name: ClassVar[str] = "Compilation"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Compilation

    id: Union[str, CompilationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompilationId):
            self.id = CompilationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContextualCompilation(Compilation):
    """
    A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed
    on a given day, all accounts associated with a given person).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["ContextualCompilation"]
    class_class_curie: ClassVar[str] = "uco-core:ContextualCompilation"
    class_name: ClassVar[str] = "ContextualCompilation"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContextualCompilation

    id: Union[str, ContextualCompilationId] = None
    object: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContextualCompilationId):
            self.id = ContextualCompilationId(self.id)

        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.object]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ControlledVocabulary(UcoObject):
    """
    A controlled vocabulary is an explicitly constrained set of string values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["ControlledVocabulary"]
    class_class_curie: ClassVar[str] = "uco-core:ControlledVocabulary"
    class_name: ClassVar[str] = "ControlledVocabulary"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ControlledVocabulary

    id: Union[str, ControlledVocabularyId] = None
    value: str = None
    constrainingVocabularyName: Optional[str] = None
    constrainingVocabularyReference: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlledVocabularyId):
            self.id = ControlledVocabularyId(self.id)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.constrainingVocabularyName is not None and not isinstance(self.constrainingVocabularyName, str):
            self.constrainingVocabularyName = str(self.constrainingVocabularyName)

        if self.constrainingVocabularyReference is not None and not isinstance(self.constrainingVocabularyReference, URI):
            self.constrainingVocabularyReference = URI(self.constrainingVocabularyReference)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EnclosingCompilation(Compilation):
    """
    An enclosing compilation is a container for a grouping of things.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["EnclosingCompilation"]
    class_class_curie: ClassVar[str] = "uco-core:EnclosingCompilation"
    class_name: ClassVar[str] = "EnclosingCompilation"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EnclosingCompilation

    id: Union[str, EnclosingCompilationId] = None
    object: Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnclosingCompilationId):
            self.id = EnclosingCompilationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.object]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Bundle(EnclosingCompilation):
    """
    A bundle is a container for a grouping of UCO content with no presumption of shared context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["Bundle"]
    class_class_curie: ClassVar[str] = "uco-core:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Bundle

    id: Union[str, BundleId] = None
    object: Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BundleId):
            self.id = BundleId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Event(UcoObject):
    """
    An Event is a noteworthy occurrence (something that happens or might happen).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["Event"]
    class_class_curie: ClassVar[str] = "uco-core:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Event

    id: Union[str, EventId] = None
    endTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    eventAttribute: Optional[Union[Union[dict, Dictionary], list[Union[dict, Dictionary]]]] = empty_list()
    eventContext: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    eventType: Optional[Union[str, list[str]]] = empty_list()
    startTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        if not isinstance(self.endTime, list):
            self.endTime = [self.endTime] if self.endTime is not None else []
        self.endTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.endTime]

        if not isinstance(self.eventAttribute, list):
            self.eventAttribute = [self.eventAttribute] if self.eventAttribute is not None else []
        self.eventAttribute = [v if isinstance(v, Dictionary) else Dictionary(**as_dict(v)) for v in self.eventAttribute]

        if not isinstance(self.eventContext, list):
            self.eventContext = [self.eventContext] if self.eventContext is not None else []
        self.eventContext = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.eventContext]

        if not isinstance(self.eventType, list):
            self.eventType = [self.eventType] if self.eventType is not None else []
        self.eventType = [v if isinstance(v, str) else str(v) for v in self.eventType]

        if not isinstance(self.startTime, list):
            self.startTime = [self.startTime] if self.startTime is not None else []
        self.startTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.startTime]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Grouping(ContextualCompilation):
    """
    A grouping is a compilation of referenced UCO content with a shared context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["Grouping"]
    class_class_curie: ClassVar[str] = "uco-core:Grouping"
    class_name: ClassVar[str] = "Grouping"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Grouping

    id: Union[str, GroupingId] = None
    context: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GroupingId):
            self.id = GroupingId(self.id)

        if not isinstance(self.context, list):
            self.context = [self.context] if self.context is not None else []
        self.context = [v if isinstance(v, str) else str(v) for v in self.context]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class IdentityAbstraction(UcoObject):
    """
    An identity abstraction is a grouping of identifying characteristics unique to an individual or organization. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the identity:Identity class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["IdentityAbstraction"]
    class_class_curie: ClassVar[str] = "uco-core:IdentityAbstraction"
    class_name: ClassVar[str] = "IdentityAbstraction"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IdentityAbstraction

    id: Union[str, IdentityAbstractionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentityAbstractionId):
            self.id = IdentityAbstractionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Item(UcoObject):
    """
    An item is a distinct article or unit.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["Item"]
    class_class_curie: ClassVar[str] = "uco-core:Item"
    class_name: ClassVar[str] = "Item"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Item

    id: Union[str, ItemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ItemId):
            self.id = ItemId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MarkingDefinitionAbstraction(UcoObject):
    """
    A marking definition abstraction is a grouping of characteristics unique to the expression of a specific data
    marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the marking:MarkingDefinition class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["MarkingDefinitionAbstraction"]
    class_class_curie: ClassVar[str] = "uco-core:MarkingDefinitionAbstraction"
    class_name: ClassVar[str] = "MarkingDefinitionAbstraction"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MarkingDefinitionAbstraction

    id: Union[str, MarkingDefinitionAbstractionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MarkingDefinitionAbstractionId):
            self.id = MarkingDefinitionAbstractionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ModusOperandi(UcoObject):
    """
    A modus operandi is a particular method of operation (how a particular entity behaves or the resources they use).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["ModusOperandi"]
    class_class_curie: ClassVar[str] = "uco-core:ModusOperandi"
    class_name: ClassVar[str] = "ModusOperandi"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ModusOperandi

    id: Union[str, ModusOperandiId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModusOperandiId):
            self.id = ModusOperandiId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Relationship(UcoObject):
    """
    A relationship is a grouping of characteristics unique to an assertion that one or more objects are related to
    another object in some way.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["Relationship"]
    class_class_curie: ClassVar[str] = "uco-core:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Relationship

    id: Union[str, RelationshipId] = None
    isDirectional: Union[bool, Bool] = None
    source: Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]] = None
    target: Union[str, UcoObjectId] = None
    endTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    kindOfRelationship: Optional[str] = None
    startTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipId):
            self.id = RelationshipId(self.id)

        if self._is_empty(self.isDirectional):
            self.MissingRequiredField("isDirectional")
        if not isinstance(self.isDirectional, Bool):
            self.isDirectional = Bool(self.isDirectional)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.source]

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, UcoObjectId):
            self.target = UcoObjectId(self.target)

        if not isinstance(self.endTime, list):
            self.endTime = [self.endTime] if self.endTime is not None else []
        self.endTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.endTime]

        if self.kindOfRelationship is not None and not isinstance(self.kindOfRelationship, str):
            self.kindOfRelationship = str(self.kindOfRelationship)

        if not isinstance(self.startTime, list):
            self.startTime = [self.startTime] if self.startTime is not None else []
        self.startTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.startTime]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UcoType(YAMLRoot):
    """
    UcoType is the top-level class for metaclasses within UCO. An instance of core:UcoType is also an instance of
    owl:Class, and is or specializes core:UcoThing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CORE["UcoType"]
    class_class_curie: ClassVar[str] = "uco-core:UcoType"
    class_name: ClassVar[str] = "UcoType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UcoType

    id: Union[str, UcoTypeId] = None
    type: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UcoTypeId):
            self.id = UcoTypeId(self.id)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class Configuration(UcoObject):
    """
    A configuration is a grouping of characteristics unique to a set of parameters or initial settings for the use of
    a tool, application, software, or other cyber object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CONFIGURATION["Configuration"]
    class_class_curie: ClassVar[str] = "uco-configuration:Configuration"
    class_name: ClassVar[str] = "Configuration"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Configuration

    id: Union[str, ConfigurationId] = None
    configurationEntry: Optional[Union[Union[dict, "ConfigurationEntry"], list[Union[dict, "ConfigurationEntry"]]]] = empty_list()
    dependencies: Optional[Union[Union[dict, "Dependency"], list[Union[dict, "Dependency"]]]] = empty_list()
    usageContextAssumptions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConfigurationId):
            self.id = ConfigurationId(self.id)

        if not isinstance(self.configurationEntry, list):
            self.configurationEntry = [self.configurationEntry] if self.configurationEntry is not None else []
        self.configurationEntry = [v if isinstance(v, ConfigurationEntry) else ConfigurationEntry(**as_dict(v)) for v in self.configurationEntry]

        if not isinstance(self.dependencies, list):
            self.dependencies = [self.dependencies] if self.dependencies is not None else []
        self.dependencies = [v if isinstance(v, Dependency) else Dependency(**as_dict(v)) for v in self.dependencies]

        if not isinstance(self.usageContextAssumptions, list):
            self.usageContextAssumptions = [self.usageContextAssumptions] if self.usageContextAssumptions is not None else []
        self.usageContextAssumptions = [v if isinstance(v, str) else str(v) for v in self.usageContextAssumptions]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ConfigurationEntry(UcoInherentCharacterizationThing):
    """
    A configuration entry is a grouping of characteristics unique to a particular parameter or initial setting for the
    use of a tool, application, software, or other cyber object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CONFIGURATION["ConfigurationEntry"]
    class_class_curie: ClassVar[str] = "uco-configuration:ConfigurationEntry"
    class_name: ClassVar[str] = "ConfigurationEntry"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ConfigurationEntry

    itemDescription: Optional[str] = None
    itemName: Optional[str] = None
    itemObject: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    itemType: Optional[str] = None
    itemValue: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.itemDescription is not None and not isinstance(self.itemDescription, str):
            self.itemDescription = str(self.itemDescription)

        if self.itemName is not None and not isinstance(self.itemName, str):
            self.itemName = str(self.itemName)

        if not isinstance(self.itemObject, list):
            self.itemObject = [self.itemObject] if self.itemObject is not None else []
        self.itemObject = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.itemObject]

        if self.itemType is not None and not isinstance(self.itemType, str):
            self.itemType = str(self.itemType)

        if not isinstance(self.itemValue, list):
            self.itemValue = [self.itemValue] if self.itemValue is not None else []
        self.itemValue = [v if isinstance(v, str) else str(v) for v in self.itemValue]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Dependency(UcoInherentCharacterizationThing):
    """
    A dependency is a grouping of characteristics unique to something that a tool or other software relies on to
    function as intended.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_CONFIGURATION["Dependency"]
    class_class_curie: ClassVar[str] = "uco-configuration:Dependency"
    class_name: ClassVar[str] = "Dependency"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Dependency

    dependencyDescription: Optional[str] = None
    dependencyType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.dependencyDescription is not None and not isinstance(self.dependencyDescription, str):
            self.dependencyDescription = str(self.dependencyDescription)

        if self.dependencyType is not None and not isinstance(self.dependencyType, str):
            self.dependencyType = str(self.dependencyType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GPSCoordinatesFacet(Facet):
    """
    A GPS coordinates facet is a grouping of characteristics unique to the expression of quantified dilution of
    precision (DOP) for an asserted set of geolocation coordinates typically associated with satellite navigation such
    as the Global Positioning System (GPS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_LOCATION["GPSCoordinatesFacet"]
    class_class_curie: ClassVar[str] = "uco-location:GPSCoordinatesFacet"
    class_name: ClassVar[str] = "GPSCoordinatesFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GPSCoordinatesFacet

    hdop: Optional[Decimal] = None
    pdop: Optional[Decimal] = None
    tdop: Optional[Decimal] = None
    vdop: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.hdop is not None and not isinstance(self.hdop, Decimal):
            self.hdop = Decimal(self.hdop)

        if self.pdop is not None and not isinstance(self.pdop, Decimal):
            self.pdop = Decimal(self.pdop)

        if self.tdop is not None and not isinstance(self.tdop, Decimal):
            self.tdop = Decimal(self.tdop)

        if self.vdop is not None and not isinstance(self.vdop, Decimal):
            self.vdop = Decimal(self.vdop)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class LatLongCoordinatesFacet(Facet):
    """
    A lat long coordinates facet is a grouping of characteristics unique to the expression of a geolocation as the
    intersection of specific latitude, longitude, and altitude values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_LOCATION["LatLongCoordinatesFacet"]
    class_class_curie: ClassVar[str] = "uco-location:LatLongCoordinatesFacet"
    class_name: ClassVar[str] = "LatLongCoordinatesFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.LatLongCoordinatesFacet

    altitude: Optional[Decimal] = None
    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.altitude is not None and not isinstance(self.altitude, Decimal):
            self.altitude = Decimal(self.altitude)

        if self.latitude is not None and not isinstance(self.latitude, Decimal):
            self.latitude = Decimal(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, Decimal):
            self.longitude = Decimal(self.longitude)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Location(UcoObject):
    """
    A location is a geospatial place, site, or position.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_LOCATION["Location"]
    class_class_curie: ClassVar[str] = "uco-location:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Location

    id: Union[str, LocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocationId):
            self.id = LocationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SimpleAddressFacet(Facet):
    """
    A simple address facet is a grouping of characteristics unique to a geolocation expressed as an administrative
    address.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_LOCATION["SimpleAddressFacet"]
    class_class_curie: ClassVar[str] = "uco-location:SimpleAddressFacet"
    class_name: ClassVar[str] = "SimpleAddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SimpleAddressFacet

    addressType: Optional[str] = None
    country: Optional[str] = None
    locality: Optional[str] = None
    postalCode: Optional[str] = None
    region: Optional[str] = None
    street: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.addressType is not None and not isinstance(self.addressType, str):
            self.addressType = str(self.addressType)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        if self.locality is not None and not isinstance(self.locality, str):
            self.locality = str(self.locality)

        if self.postalCode is not None and not isinstance(self.postalCode, str):
            self.postalCode = str(self.postalCode)

        if self.region is not None and not isinstance(self.region, str):
            self.region = str(self.region)

        if self.street is not None and not isinstance(self.street, str):
            self.street = str(self.street)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Identity(IdentityAbstraction):
    """
    An identity is a grouping of identifying characteristics unique to an individual or organization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["Identity"]
    class_class_curie: ClassVar[str] = "uco-identity:Identity"
    class_name: ClassVar[str] = "Identity"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Identity

    id: Union[str, IdentityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentityId):
            self.id = IdentityId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class IdentityFacet(Facet):
    """
    An identity facet is a grouping of characteristics unique to a particular aspect of an identity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["IdentityFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:IdentityFacet"
    class_name: ClassVar[str] = "IdentityFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IdentityFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AddressFacet(IdentityFacet):
    """
    An address facet is a grouping of characteristics unique to an administrative identifier for a geolocation
    associated with a specific identity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["AddressFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:AddressFacet"
    class_name: ClassVar[str] = "AddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AddressFacet

    address: Optional[Union[str, LocationId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.address is not None and not isinstance(self.address, LocationId):
            self.address = LocationId(self.address)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class AffiliationFacet(IdentityFacet):
    """
    An affiliation is a grouping of characteristics unique to the established affiliations of an entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["AffiliationFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:AffiliationFacet"
    class_name: ClassVar[str] = "AffiliationFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AffiliationFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BirthInformationFacet(IdentityFacet):
    """
    Birth information is a grouping of characteristics unique to information pertaining to the birth of an entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["BirthInformationFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:BirthInformationFacet"
    class_name: ClassVar[str] = "BirthInformationFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BirthInformationFacet

    birthdate: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.birthdate is not None and not isinstance(self.birthdate, XSDDateTime):
            self.birthdate = XSDDateTime(self.birthdate)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class CountryOfResidenceFacet(IdentityFacet):
    """
    Country of residence is a grouping of characteristics unique to information related to the country, or countries,
    where an entity resides.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["CountryOfResidenceFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:CountryOfResidenceFacet"
    class_name: ClassVar[str] = "CountryOfResidenceFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CountryOfResidenceFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class EventsFacet(IdentityFacet):
    """
    Events is a grouping of characteristics unique to information related to specific relevant things that happen in
    the lifetime of an entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["EventsFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:EventsFacet"
    class_name: ClassVar[str] = "EventsFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EventsFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class IdentifierFacet(IdentityFacet):
    """
    Identifier is a grouping of characteristics unique to information that uniquely and specifically identities an
    entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["IdentifierFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:IdentifierFacet"
    class_name: ClassVar[str] = "IdentifierFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IdentifierFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class LanguagesFacet(IdentityFacet):
    """
    Languages is a grouping of characteristics unique to specific syntactically and grammatically standardized forms
    of communication (human or computer) in which an entity has proficiency (comprehends, speaks, reads, or writes).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["LanguagesFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:LanguagesFacet"
    class_name: ClassVar[str] = "LanguagesFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.LanguagesFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class NationalityFacet(IdentityFacet):
    """
    Nationality is a grouping of characteristics unique to the condition of an entity belonging to a particular nation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["NationalityFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:NationalityFacet"
    class_name: ClassVar[str] = "NationalityFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NationalityFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class OccupationFacet(IdentityFacet):
    """
    Occupation is a grouping of characteristics unique to the job or profession of an entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["OccupationFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:OccupationFacet"
    class_name: ClassVar[str] = "OccupationFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.OccupationFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Organization(Identity):
    """
    An organization is a grouping of identifying characteristics unique to a group of people who work together in an
    organized way for a shared purpose. [based on https://dictionary.cambridge.org/us/dictionary/english/organization]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["Organization"]
    class_class_curie: ClassVar[str] = "uco-identity:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Organization

    id: Union[str, OrganizationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class OrganizationDetailsFacet(IdentityFacet):
    """
    Organization details is a grouping of characteristics unique to an identity representing an administrative and
    functional structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["OrganizationDetailsFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:OrganizationDetailsFacet"
    class_name: ClassVar[str] = "OrganizationDetailsFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.OrganizationDetailsFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Person(Identity):
    """
    A person is a grouping of identifying characteristics unique to a human being regarded as an individual. [based on
    https://www.lexico.com/en/definition/person]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["Person"]
    class_class_curie: ClassVar[str] = "uco-identity:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Person

    id: Union[str, PersonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class PersonalDetailsFacet(IdentityFacet):
    """
    Personal details is a grouping of characteristics unique to an identity representing an individual person.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["PersonalDetailsFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:PersonalDetailsFacet"
    class_name: ClassVar[str] = "PersonalDetailsFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.PersonalDetailsFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class PhysicalInfoFacet(IdentityFacet):
    """
    Physical info is a grouping of characteristics unique to the outwardly observable nature of an individual person.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["PhysicalInfoFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:PhysicalInfoFacet"
    class_name: ClassVar[str] = "PhysicalInfoFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.PhysicalInfoFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class QualificationFacet(IdentityFacet):
    """
    Qualification is a grouping of characteristics unique to particular skills, capabilities or their related
    achievements (educational, professional, etc.) of an entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["QualificationFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:QualificationFacet"
    class_name: ClassVar[str] = "QualificationFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.QualificationFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class RelatedIdentityFacet(IdentityFacet):
    """
    <Needs fleshed out from CIQ>
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["RelatedIdentityFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:RelatedIdentityFacet"
    class_name: ClassVar[str] = "RelatedIdentityFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.RelatedIdentityFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SimpleNameFacet(IdentityFacet):
    """
    A simple name facet is a grouping of characteristics unique to the personal name (e.g., Dr. John Smith Jr.) held
    by an identity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["SimpleNameFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:SimpleNameFacet"
    class_name: ClassVar[str] = "SimpleNameFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SimpleNameFacet

    familyName: Optional[Union[str, list[str]]] = empty_list()
    givenName: Optional[Union[str, list[str]]] = empty_list()
    honorificPrefix: Optional[Union[str, list[str]]] = empty_list()
    honorificSuffix: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.familyName, list):
            self.familyName = [self.familyName] if self.familyName is not None else []
        self.familyName = [v if isinstance(v, str) else str(v) for v in self.familyName]

        if not isinstance(self.givenName, list):
            self.givenName = [self.givenName] if self.givenName is not None else []
        self.givenName = [v if isinstance(v, str) else str(v) for v in self.givenName]

        if not isinstance(self.honorificPrefix, list):
            self.honorificPrefix = [self.honorificPrefix] if self.honorificPrefix is not None else []
        self.honorificPrefix = [v if isinstance(v, str) else str(v) for v in self.honorificPrefix]

        if not isinstance(self.honorificSuffix, list):
            self.honorificSuffix = [self.honorificSuffix] if self.honorificSuffix is not None else []
        self.honorificSuffix = [v if isinstance(v, str) else str(v) for v in self.honorificSuffix]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class VisaFacet(IdentityFacet):
    """
    Visa is a grouping of characteristics unique to information related to a person's ability to enter, leave, or stay
    for a specified period of time in a country.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_IDENTITY["VisaFacet"]
    class_class_curie: ClassVar[str] = "uco-identity:VisaFacet"
    class_name: ClassVar[str] = "VisaFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.VisaFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GranularMarking(UcoInherentCharacterizationThing):
    """
    A granular marking is a grouping of characteristics unique to specification of marking definitions (restrictions,
    permissions, and other guidance for how data can be used and shared) that apply to particular portions of a
    particular UCO object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_MARKING["GranularMarking"]
    class_class_curie: ClassVar[str] = "uco-marking:GranularMarking"
    class_name: ClassVar[str] = "GranularMarking"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GranularMarking

    contentSelectors: Optional[Union[str, list[str]]] = empty_list()
    marking: Optional[Union[Union[str, MarkingDefinitionId], list[Union[str, MarkingDefinitionId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.contentSelectors, list):
            self.contentSelectors = [self.contentSelectors] if self.contentSelectors is not None else []
        self.contentSelectors = [v if isinstance(v, str) else str(v) for v in self.contentSelectors]

        if not isinstance(self.marking, list):
            self.marking = [self.marking] if self.marking is not None else []
        self.marking = [v if isinstance(v, MarkingDefinitionId) else MarkingDefinitionId(v) for v in self.marking]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MarkingDefinition(MarkingDefinitionAbstraction):
    """
    A marking definition is a grouping of characteristics unique to the expression of a specific data marking
    conveying restrictions, permissions, and other guidance for how marked data can be used and shared.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_MARKING["MarkingDefinition"]
    class_class_curie: ClassVar[str] = "uco-marking:MarkingDefinition"
    class_name: ClassVar[str] = "MarkingDefinition"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MarkingDefinition

    id: Union[str, MarkingDefinitionId] = None
    definitionType: str = None
    definition: Optional[Union[Union[dict, "MarkingModel"], list[Union[dict, "MarkingModel"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MarkingDefinitionId):
            self.id = MarkingDefinitionId(self.id)

        if self._is_empty(self.definitionType):
            self.MissingRequiredField("definitionType")
        if not isinstance(self.definitionType, str):
            self.definitionType = str(self.definitionType)

        if not isinstance(self.definition, list):
            self.definition = [self.definition] if self.definition is not None else []
        self.definition = [v if isinstance(v, MarkingModel) else MarkingModel(**as_dict(v)) for v in self.definition]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class MarkingModel(UcoInherentCharacterizationThing):
    """
    A marking model is a grouping of characteristics unique to the expression of a particular form of data marking
    definitions (restrictions, permissions, and other guidance for how data can be used and shared).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_MARKING["MarkingModel"]
    class_class_curie: ClassVar[str] = "uco-marking:MarkingModel"
    class_name: ClassVar[str] = "MarkingModel"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MarkingModel


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class LicenseMarking(MarkingModel):
    """
    A license marking is a grouping of characteristics unique to the expression of data marking definitions
    (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of license
    restrictions that apply to the data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_MARKING["LicenseMarking"]
    class_class_curie: ClassVar[str] = "uco-marking:LicenseMarking"
    class_name: ClassVar[str] = "LicenseMarking"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.LicenseMarking

    license: str = None
    definitionType: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, str):
            self.license = str(self.license)

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ReleaseToMarking(MarkingModel):
    """
    A release-to marking is a grouping of characteristics unique to the expression of data marking definitions
    (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of
    authorized persons and/or organizations to which to the associated content may be released. The existence of the
    Release-To marking restricts access to ONLY those identities explicitly listed, regardless of whether another data
    marking exists that allows sharing with other members of the community.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_MARKING["ReleaseToMarking"]
    class_class_curie: ClassVar[str] = "uco-marking:ReleaseToMarking"
    class_name: ClassVar[str] = "ReleaseToMarking"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ReleaseToMarking

    authorizedIdentities: Union[str, list[str]] = None
    definitionType: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.authorizedIdentities):
            self.MissingRequiredField("authorizedIdentities")
        if not isinstance(self.authorizedIdentities, list):
            self.authorizedIdentities = [self.authorizedIdentities] if self.authorizedIdentities is not None else []
        self.authorizedIdentities = [v if isinstance(v, str) else str(v) for v in self.authorizedIdentities]

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class StatementMarking(MarkingModel):
    """
    A statement marking is a grouping of characteristics unique to the expression of data marking definitions
    (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual
    marking statement, (e.g., copyright) whose semantic meaning should apply to the associated content. Statement
    markings are generally not machine-readable. An example of this would be a simple marking to apply copyright
    information, such as 'Copyright 2014 Acme Inc.'.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_MARKING["StatementMarking"]
    class_class_curie: ClassVar[str] = "uco-marking:StatementMarking"
    class_name: ClassVar[str] = "StatementMarking"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.StatementMarking

    marking_statement: str = None
    definitionType: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.marking_statement):
            self.MissingRequiredField("marking_statement")
        if not isinstance(self.marking_statement, str):
            self.marking_statement = str(self.marking_statement)

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class TermsOfUseMarking(MarkingModel):
    """
    A terms of use marking is a grouping of characteristics unique to the expression of data marking definitions
    (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual
    statement specifying the Terms of Use (that is, the conditions under which the content may be shared, applied, or
    otherwise used) of the marked content. An example of this would be used to communicate a simple statement, such as
    'Acme Inc. is not responsible for the content of this file'.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_MARKING["TermsOfUseMarking"]
    class_class_curie: ClassVar[str] = "uco-marking:TermsOfUseMarking"
    class_name: ClassVar[str] = "TermsOfUseMarking"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.TermsOfUseMarking

    termsOfUse: str = None
    definitionType: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.termsOfUse):
            self.MissingRequiredField("termsOfUse")
        if not isinstance(self.termsOfUse, str):
            self.termsOfUse = str(self.termsOfUse)

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Pattern(UcoObject):
    """
    A pattern is a combination of properties, acts, tendencies, etc., forming a consistent or characteristic
    arrangement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_PATTERN["Pattern"]
    class_class_curie: ClassVar[str] = "uco-pattern:Pattern"
    class_name: ClassVar[str] = "Pattern"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Pattern

    id: Union[str, PatternId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PatternId):
            self.id = PatternId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class LogicalPattern(Pattern):
    """
    A logical pattern is a grouping of characteristics unique to an informational pattern expressed via a structured
    pattern expression following the rules of logic.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_PATTERN["LogicalPattern"]
    class_class_curie: ClassVar[str] = "uco-pattern:LogicalPattern"
    class_name: ClassVar[str] = "LogicalPattern"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.LogicalPattern

    id: Union[str, LogicalPatternId] = None
    patternExpression: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LogicalPatternId):
            self.id = LogicalPatternId(self.id)

        if self.patternExpression is not None and not isinstance(self.patternExpression, str):
            self.patternExpression = str(self.patternExpression)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class PatternExpression(UcoInherentCharacterizationThing):
    """
    A pattern expression is a grouping of characteristics unique to an explicit logical expression defining a pattern
    (e.g., regular expression, SQL Select expression, etc.).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_PATTERN["PatternExpression"]
    class_class_curie: ClassVar[str] = "uco-pattern:PatternExpression"
    class_name: ClassVar[str] = "PatternExpression"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.PatternExpression


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Role(UcoObject):
    """
    A role is a usual or customary function based on contextual perspective.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ROLE["Role"]
    class_class_curie: ClassVar[str] = "uco-role:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Role

    id: Union[str, RoleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RoleId):
            self.id = RoleId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BenevolentRole(Role):
    """
    A benevolent role is a role with positive and/or beneficial intent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ROLE["BenevolentRole"]
    class_class_curie: ClassVar[str] = "uco-role:BenevolentRole"
    class_name: ClassVar[str] = "BenevolentRole"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BenevolentRole

    id: Union[str, BenevolentRoleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenevolentRoleId):
            self.id = BenevolentRoleId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MaliciousRole(Role):
    """
    A malicious role is a role with malevolent intent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ROLE["MaliciousRole"]
    class_class_curie: ClassVar[str] = "uco-role:MaliciousRole"
    class_name: ClassVar[str] = "MaliciousRole"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MaliciousRole

    id: Union[str, MaliciousRoleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaliciousRoleId):
            self.id = MaliciousRoleId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NeutralRole(Role):
    """
    A neutral role is a role with impartial intent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ROLE["NeutralRole"]
    class_class_curie: ClassVar[str] = "uco-role:NeutralRole"
    class_name: ClassVar[str] = "NeutralRole"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NeutralRole

    id: Union[str, NeutralRoleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NeutralRoleId):
            self.id = NeutralRoleId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BuildFacet(Facet):
    """
    A build facet is a grouping of characteristics unique to a particular version of a software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TOOL["BuildFacet"]
    class_class_curie: ClassVar[str] = "uco-tool:BuildFacet"
    class_name: ClassVar[str] = "BuildFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BuildFacet

    buildInformation: Optional[Union[dict, "BuildInformationType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.buildInformation is not None and not isinstance(self.buildInformation, BuildInformationType):
            self.buildInformation = BuildInformationType(**as_dict(self.buildInformation))

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BuildInformationType(UcoInherentCharacterizationThing):
    """
    A build information type is a grouping of characteristics that describe how a particular version of software was
    converted from source code to executable code.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TOOL["BuildInformationType"]
    class_class_curie: ClassVar[str] = "uco-tool:BuildInformationType"
    class_name: ClassVar[str] = "BuildInformationType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BuildInformationType

    buildConfiguration: Optional[Union[str, ConfigurationId]] = None
    buildID: Optional[str] = None
    buildLabel: Optional[str] = None
    buildOutputLog: Optional[str] = None
    buildProject: Optional[str] = None
    buildScript: Optional[str] = None
    buildUtility: Optional[Union[dict, "BuildUtilityType"]] = None
    buildVersion: Optional[str] = None
    compilationDate: Optional[Union[str, XSDDateTime]] = None
    compilers: Optional[Union[Union[dict, "CompilerType"], list[Union[dict, "CompilerType"]]]] = empty_list()
    libraries: Optional[Union[Union[dict, "LibraryType"], list[Union[dict, "LibraryType"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.buildConfiguration is not None and not isinstance(self.buildConfiguration, ConfigurationId):
            self.buildConfiguration = ConfigurationId(self.buildConfiguration)

        if self.buildID is not None and not isinstance(self.buildID, str):
            self.buildID = str(self.buildID)

        if self.buildLabel is not None and not isinstance(self.buildLabel, str):
            self.buildLabel = str(self.buildLabel)

        if self.buildOutputLog is not None and not isinstance(self.buildOutputLog, str):
            self.buildOutputLog = str(self.buildOutputLog)

        if self.buildProject is not None and not isinstance(self.buildProject, str):
            self.buildProject = str(self.buildProject)

        if self.buildScript is not None and not isinstance(self.buildScript, str):
            self.buildScript = str(self.buildScript)

        if self.buildUtility is not None and not isinstance(self.buildUtility, BuildUtilityType):
            self.buildUtility = BuildUtilityType(**as_dict(self.buildUtility))

        if self.buildVersion is not None and not isinstance(self.buildVersion, str):
            self.buildVersion = str(self.buildVersion)

        if self.compilationDate is not None and not isinstance(self.compilationDate, XSDDateTime):
            self.compilationDate = XSDDateTime(self.compilationDate)

        if not isinstance(self.compilers, list):
            self.compilers = [self.compilers] if self.compilers is not None else []
        self.compilers = [v if isinstance(v, CompilerType) else CompilerType(**as_dict(v)) for v in self.compilers]

        if not isinstance(self.libraries, list):
            self.libraries = [self.libraries] if self.libraries is not None else []
        self.libraries = [v if isinstance(v, LibraryType) else LibraryType(**as_dict(v)) for v in self.libraries]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BuildUtilityType(UcoInherentCharacterizationThing):
    """
    A build utility type characterizes the tool used to convert from source code to executable code for a particular
    version of software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TOOL["BuildUtilityType"]
    class_class_curie: ClassVar[str] = "uco-tool:BuildUtilityType"
    class_name: ClassVar[str] = "BuildUtilityType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BuildUtilityType

    buildUtilityName: Optional[str] = None
    cpeid: Optional[str] = None
    swid: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.buildUtilityName is not None and not isinstance(self.buildUtilityName, str):
            self.buildUtilityName = str(self.buildUtilityName)

        if self.cpeid is not None and not isinstance(self.cpeid, str):
            self.cpeid = str(self.cpeid)

        if self.swid is not None and not isinstance(self.swid, str):
            self.swid = str(self.swid)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CompilerType(UcoInherentCharacterizationThing):
    """
    A compiler type is a grouping of characteristics unique to a specific program that translates computer code
    written in one programming language (the source language) into another language (the target language). Typically a
    program that translates source code from a high-level programming language to a lower-level language (e.g.,
    assembly language, object code, or machine code) to create an executable program. [based on
    https://en.wikipedia.org/wiki/Compiler]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TOOL["CompilerType"]
    class_class_curie: ClassVar[str] = "uco-tool:CompilerType"
    class_name: ClassVar[str] = "CompilerType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CompilerType

    compilerInformalDescription: Optional[str] = None
    cpeid: Optional[str] = None
    swid: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.compilerInformalDescription is not None and not isinstance(self.compilerInformalDescription, str):
            self.compilerInformalDescription = str(self.compilerInformalDescription)

        if self.cpeid is not None and not isinstance(self.cpeid, str):
            self.cpeid = str(self.cpeid)

        if self.swid is not None and not isinstance(self.swid, str):
            self.swid = str(self.swid)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class LibraryType(UcoInherentCharacterizationThing):
    """
    A library type is a grouping of characteristics unique to a collection of resources incorporated into the build of
    a software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TOOL["LibraryType"]
    class_class_curie: ClassVar[str] = "uco-tool:LibraryType"
    class_name: ClassVar[str] = "LibraryType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.LibraryType

    libraryName: Optional[str] = None
    libraryVersion: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.libraryName is not None and not isinstance(self.libraryName, str):
            self.libraryName = str(self.libraryName)

        if self.libraryVersion is not None and not isinstance(self.libraryVersion, str):
            self.libraryVersion = str(self.libraryVersion)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Tool(UcoObject):
    """
    A tool is an element of hardware and/or software utilized to carry out a particular function.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TOOL["Tool"]
    class_class_curie: ClassVar[str] = "uco-tool:Tool"
    class_name: ClassVar[str] = "Tool"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Tool

    id: Union[str, ToolId] = None
    creator: Optional[Union[str, IdentityId]] = None
    references: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    servicePack: Optional[str] = None
    toolType: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ToolId):
            self.id = ToolId(self.id)

        if self.creator is not None and not isinstance(self.creator, IdentityId):
            self.creator = IdentityId(self.creator)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, URI) else URI(v) for v in self.references]

        if self.servicePack is not None and not isinstance(self.servicePack, str):
            self.servicePack = str(self.servicePack)

        if self.toolType is not None and not isinstance(self.toolType, str):
            self.toolType = str(self.toolType)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AnalyticTool(Tool):
    """
    An analytic tool is an artifact of hardware and/or software utilized to accomplish a task or purpose of
    explanation, interpretation or logical reasoning.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TOOL["AnalyticTool"]
    class_class_curie: ClassVar[str] = "uco-tool:AnalyticTool"
    class_name: ClassVar[str] = "AnalyticTool"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AnalyticTool

    id: Union[str, AnalyticToolId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalyticToolId):
            self.id = AnalyticToolId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ConfiguredTool(Tool):
    """
    A ConfiguredTool is a Tool that is known to be configured to run in a more specified manner than some unconfigured
    or less-configured Tool.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TOOL["ConfiguredTool"]
    class_class_curie: ClassVar[str] = "uco-tool:ConfiguredTool"
    class_name: ClassVar[str] = "ConfiguredTool"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ConfiguredTool

    id: Union[str, ConfiguredToolId] = None
    isConfigurationOf: Optional[Union[str, ToolId]] = None
    usesConfiguration: Optional[Union[str, ConfigurationId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConfiguredToolId):
            self.id = ConfiguredToolId(self.id)

        if self.isConfigurationOf is not None and not isinstance(self.isConfigurationOf, ToolId):
            self.isConfigurationOf = ToolId(self.isConfigurationOf)

        if self.usesConfiguration is not None and not isinstance(self.usesConfiguration, ConfigurationId):
            self.usesConfiguration = ConfigurationId(self.usesConfiguration)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DefensiveTool(Tool):
    """
    A defensive tool is an artifact of hardware and/or software utilized to accomplish a task or purpose of guarding.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TOOL["DefensiveTool"]
    class_class_curie: ClassVar[str] = "uco-tool:DefensiveTool"
    class_name: ClassVar[str] = "DefensiveTool"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DefensiveTool

    id: Union[str, DefensiveToolId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DefensiveToolId):
            self.id = DefensiveToolId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MaliciousTool(Tool):
    """
    A malicious tool is an artifact of hardware and/or software utilized to accomplish a malevolent task or purpose.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TOOL["MaliciousTool"]
    class_class_curie: ClassVar[str] = "uco-tool:MaliciousTool"
    class_name: ClassVar[str] = "MaliciousTool"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MaliciousTool

    id: Union[str, MaliciousToolId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaliciousToolId):
            self.id = MaliciousToolId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Victim(NeutralRole):
    """
    A victim is a role played by a person or organization that is/was the target of some malicious action.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_VICTIM["Victim"]
    class_class_curie: ClassVar[str] = "uco-victim:Victim"
    class_name: ClassVar[str] = "Victim"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Victim

    id: Union[str, VictimId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VictimId):
            self.id = VictimId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class VictimTargeting(Victim):
    """
    A victim targeting is a grouping of characteristics unique to people or organizations that are the target of some
    malicious activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_VICTIM["VictimTargeting"]
    class_class_curie: ClassVar[str] = "uco-victim:VictimTargeting"
    class_name: ClassVar[str] = "VictimTargeting"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.VictimTargeting

    id: Union[str, VictimTargetingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VictimTargetingId):
            self.id = VictimTargetingId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ControlledDictionary(Dictionary):
    """
    A controlled dictionary is a list of (term/key, value) pairs where each term/key exists no more than once and is
    constrained to an explicitly defined set of values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TYPES["ControlledDictionary"]
    class_class_curie: ClassVar[str] = "uco-types:ControlledDictionary"
    class_name: ClassVar[str] = "ControlledDictionary"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ControlledDictionary

    entry: Optional[Union[Union[dict, "ControlledDictionaryEntry"], list[Union[dict, "ControlledDictionaryEntry"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="entry", slot_type=ControlledDictionaryEntry, key_name="key", keyed=False)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ControlledDictionaryEntry(DictionaryEntry):
    """
    A controlled dictionary entry is a single (term/key, value) pair where the term/key is constrained to an
    explicitly defined set of values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TYPES["ControlledDictionaryEntry"]
    class_class_curie: ClassVar[str] = "uco-types:ControlledDictionaryEntry"
    class_name: ClassVar[str] = "ControlledDictionaryEntry"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ControlledDictionaryEntry

    key: str = None
    types_value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Hash(UcoInherentCharacterizationThing):
    """
    A hash is a grouping of characteristics unique to the result of applying a mathematical algorithm that maps data
    of arbitrary size to a bit string (the 'hash') and is a one-way function, that is, a function which is practically
    infeasible to invert. This is commonly used for integrity checking of data. [based on
    https://en.wikipedia.org/wiki/Cryptographic_hash_function]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TYPES["Hash"]
    class_class_curie: ClassVar[str] = "uco-types:Hash"
    class_name: ClassVar[str] = "Hash"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Hash

    hashMethod: Union[str, "HashNameVocab"] = None
    hashValue: Union[str, UcoHexBinary] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.hashMethod):
            self.MissingRequiredField("hashMethod")
        if not isinstance(self.hashMethod, (HashNameVocab, str)):
            value = self.hashMethod
            for _coerce in (lambda: HashNameVocab(value), lambda: str(value)):
                try:
                    self.hashMethod = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[HashNameVocab, str] could be constructed from {value!r} for slot hashMethod")

        if self._is_empty(self.hashValue):
            self.MissingRequiredField("hashValue")
        if not isinstance(self.hashValue, UcoHexBinary):
            self.hashValue = UcoHexBinary(self.hashValue)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ImproperDictionary(Dictionary):
    """
    UCO 1.5.0 declares the class uco-types:ImproperDictionary without a definition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TYPES["ImproperDictionary"]
    class_class_curie: ClassVar[str] = "uco-types:ImproperDictionary"
    class_name: ClassVar[str] = "ImproperDictionary"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ImproperDictionary

    repeatsKey: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.repeatsKey, list):
            self.repeatsKey = [self.repeatsKey] if self.repeatsKey is not None else []
        self.repeatsKey = [v if isinstance(v, str) else str(v) for v in self.repeatsKey]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class ProperDictionary(Dictionary):
    """
    A proper dictionary is list of (term/key, value) pairs with each term/key existing no more than once.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TYPES["ProperDictionary"]
    class_class_curie: ClassVar[str] = "uco-types:ProperDictionary"
    class_name: ClassVar[str] = "ProperDictionary"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ProperDictionary


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Thread(UcoThing):
    """
    A semi-ordered array of items, that can be present in multiple copies. Implementation of a UCO Thread is similar
    to a Collections Ontology List, except a Thread may fork and merge - that is, one of its members may have two or
    more direct successors, and two or more direct predecessors.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TYPES["Thread"]
    class_class_curie: ClassVar[str] = "uco-types:Thread"
    class_name: ClassVar[str] = "Thread"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Thread

    id: Union[str, ThreadId] = None
    item: Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]] = empty_list()
    threadOriginItem: Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]] = empty_list()
    threadTerminalItem: Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]] = empty_list()
    co_size: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThreadId):
            self.id = ThreadId(self.id)

        if not isinstance(self.item, list):
            self.item = [self.item] if self.item is not None else []
        self.item = [v if isinstance(v, ThreadItemId) else ThreadItemId(v) for v in self.item]

        if not isinstance(self.threadOriginItem, list):
            self.threadOriginItem = [self.threadOriginItem] if self.threadOriginItem is not None else []
        self.threadOriginItem = [v if isinstance(v, ThreadItemId) else ThreadItemId(v) for v in self.threadOriginItem]

        if not isinstance(self.threadTerminalItem, list):
            self.threadTerminalItem = [self.threadTerminalItem] if self.threadTerminalItem is not None else []
        self.threadTerminalItem = [v if isinstance(v, ThreadItemId) else ThreadItemId(v) for v in self.threadTerminalItem]

        if self.co_size is not None and not isinstance(self.co_size, int):
            self.co_size = int(self.co_size)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ThreadItem(UcoThing):
    """
    A ThreadItem is a member of a thread.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_TYPES["ThreadItem"]
    class_class_curie: ClassVar[str] = "uco-types:ThreadItem"
    class_name: ClassVar[str] = "ThreadItem"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ThreadItem

    id: Union[str, ThreadItemId] = None
    itemContent: Optional[Union[str, UcoObjectId]] = None
    threadNextItem: Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]] = empty_list()
    threadPredecessor: Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]] = empty_list()
    threadPreviousItem: Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]] = empty_list()
    threadSuccessor: Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThreadItemId):
            self.id = ThreadItemId(self.id)

        if self.itemContent is not None and not isinstance(self.itemContent, UcoObjectId):
            self.itemContent = UcoObjectId(self.itemContent)

        if not isinstance(self.threadNextItem, list):
            self.threadNextItem = [self.threadNextItem] if self.threadNextItem is not None else []
        self.threadNextItem = [v if isinstance(v, ThreadItemId) else ThreadItemId(v) for v in self.threadNextItem]

        if not isinstance(self.threadPredecessor, list):
            self.threadPredecessor = [self.threadPredecessor] if self.threadPredecessor is not None else []
        self.threadPredecessor = [v if isinstance(v, ThreadItemId) else ThreadItemId(v) for v in self.threadPredecessor]

        if not isinstance(self.threadPreviousItem, list):
            self.threadPreviousItem = [self.threadPreviousItem] if self.threadPreviousItem is not None else []
        self.threadPreviousItem = [v if isinstance(v, ThreadItemId) else ThreadItemId(v) for v in self.threadPreviousItem]

        if not isinstance(self.threadSuccessor, list):
            self.threadSuccessor = [self.threadSuccessor] if self.threadSuccessor is not None else []
        self.threadSuccessor = [v if isinstance(v, ThreadItemId) else ThreadItemId(v) for v in self.threadSuccessor]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Action(UcoObject):
    """
    An action is something that may be done or performed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ACTION["Action"]
    class_class_curie: ClassVar[str] = "uco-action:Action"
    class_name: ClassVar[str] = "Action"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Action

    id: Union[str, ActionId] = None
    actionCount: Optional[Union[int, UcoNonNegativeInteger]] = None
    actionStatus: Optional[Union[str, "ActionStatusTypeVocab"]] = None
    action_endTime: Optional[Union[str, XSDDateTime]] = None
    action_object: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    action_startTime: Optional[Union[str, XSDDateTime]] = None
    environment: Optional[Union[str, UcoObjectId]] = None
    error: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    instrument: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    location: Optional[Union[Union[str, LocationId], list[Union[str, LocationId]]]] = empty_list()
    participant: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    performer: Optional[Union[str, UcoObjectId]] = None
    result: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    subaction: Optional[Union[Union[str, ActionId], list[Union[str, ActionId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActionId):
            self.id = ActionId(self.id)

        if self.actionCount is not None and not isinstance(self.actionCount, UcoNonNegativeInteger):
            self.actionCount = UcoNonNegativeInteger(self.actionCount)

        if self.actionStatus is not None and not isinstance(self.actionStatus, (ActionStatusTypeVocab, str)):
            value = self.actionStatus
            for _coerce in (lambda: ActionStatusTypeVocab(value), lambda: str(value)):
                try:
                    self.actionStatus = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[ActionStatusTypeVocab, str] could be constructed from {value!r} for slot actionStatus")

        if self.action_endTime is not None and not isinstance(self.action_endTime, XSDDateTime):
            self.action_endTime = XSDDateTime(self.action_endTime)

        if not isinstance(self.action_object, list):
            self.action_object = [self.action_object] if self.action_object is not None else []
        self.action_object = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.action_object]

        if self.action_startTime is not None and not isinstance(self.action_startTime, XSDDateTime):
            self.action_startTime = XSDDateTime(self.action_startTime)

        if self.environment is not None and not isinstance(self.environment, UcoObjectId):
            self.environment = UcoObjectId(self.environment)

        if not isinstance(self.error, list):
            self.error = [self.error] if self.error is not None else []
        self.error = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.error]

        if not isinstance(self.instrument, list):
            self.instrument = [self.instrument] if self.instrument is not None else []
        self.instrument = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.instrument]

        if not isinstance(self.location, list):
            self.location = [self.location] if self.location is not None else []
        self.location = [v if isinstance(v, LocationId) else LocationId(v) for v in self.location]

        if not isinstance(self.participant, list):
            self.participant = [self.participant] if self.participant is not None else []
        self.participant = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.participant]

        if self.performer is not None and not isinstance(self.performer, UcoObjectId):
            self.performer = UcoObjectId(self.performer)

        if not isinstance(self.result, list):
            self.result = [self.result] if self.result is not None else []
        self.result = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.result]

        if not isinstance(self.subaction, list):
            self.subaction = [self.subaction] if self.subaction is not None else []
        self.subaction = [v if isinstance(v, ActionId) else ActionId(v) for v in self.subaction]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ActionArgumentFacet(Facet):
    """
    An action argument facet is a grouping of characteristics unique to a single parameter of an action.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ACTION["ActionArgumentFacet"]
    class_class_curie: ClassVar[str] = "uco-action:ActionArgumentFacet"
    class_name: ClassVar[str] = "ActionArgumentFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ActionArgumentFacet

    action_value: str = None
    argumentName: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.action_value):
            self.MissingRequiredField("action_value")
        if not isinstance(self.action_value, str):
            self.action_value = str(self.action_value)

        if self._is_empty(self.argumentName):
            self.MissingRequiredField("argumentName")
        if not isinstance(self.argumentName, str):
            self.argumentName = str(self.argumentName)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ActionEstimationFacet(Facet):
    """
    An action estimation facet is a grouping of characteristics unique to decision-focused approximation aspects for
    an action that may potentially be performed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ACTION["ActionEstimationFacet"]
    class_class_curie: ClassVar[str] = "uco-action:ActionEstimationFacet"
    class_name: ClassVar[str] = "ActionEstimationFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ActionEstimationFacet

    estimatedCost: Optional[str] = None
    estimatedEfficacy: Optional[str] = None
    estimatedImpact: Optional[str] = None
    objective: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.estimatedCost is not None and not isinstance(self.estimatedCost, str):
            self.estimatedCost = str(self.estimatedCost)

        if self.estimatedEfficacy is not None and not isinstance(self.estimatedEfficacy, str):
            self.estimatedEfficacy = str(self.estimatedEfficacy)

        if self.estimatedImpact is not None and not isinstance(self.estimatedImpact, str):
            self.estimatedImpact = str(self.estimatedImpact)

        if self.objective is not None and not isinstance(self.objective, str):
            self.objective = str(self.objective)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ActionFrequencyFacet(Facet):
    """
    An action frequency facet is a grouping of characteristics unique to the frequency of occurrence for an action.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ACTION["ActionFrequencyFacet"]
    class_class_curie: ClassVar[str] = "uco-action:ActionFrequencyFacet"
    class_name: ClassVar[str] = "ActionFrequencyFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ActionFrequencyFacet

    rate: Decimal = None
    scale: str = None
    trend: Union[str, "TrendVocab"] = None
    units: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.rate):
            self.MissingRequiredField("rate")
        if not isinstance(self.rate, Decimal):
            self.rate = Decimal(self.rate)

        if self._is_empty(self.scale):
            self.MissingRequiredField("scale")
        if not isinstance(self.scale, str):
            self.scale = str(self.scale)

        if self._is_empty(self.trend):
            self.MissingRequiredField("trend")
        if not isinstance(self.trend, (TrendVocab, str)):
            value = self.trend
            for _coerce in (lambda: TrendVocab(value), lambda: str(value)):
                try:
                    self.trend = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[TrendVocab, str] could be constructed from {value!r} for slot trend")

        if self._is_empty(self.units):
            self.MissingRequiredField("units")
        if not isinstance(self.units, str):
            self.units = str(self.units)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ActionLifecycle(Action):
    """
    An action lifecycle is an action pattern consisting of an ordered set of multiple actions or subordinate action
    lifecycles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ACTION["ActionLifecycle"]
    class_class_curie: ClassVar[str] = "uco-action:ActionLifecycle"
    class_name: ClassVar[str] = "ActionLifecycle"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ActionLifecycle

    id: Union[str, ActionLifecycleId] = None
    phase: Union[Union[dict, "ArrayOfAction"], list[Union[dict, "ArrayOfAction"]]] = None
    actionCount: Optional[Union[int, UcoNonNegativeInteger]] = None
    actionStatus: Optional[Union[str, "ActionStatusTypeVocab"]] = None
    action_endTime: Optional[Union[str, XSDDateTime]] = None
    action_startTime: Optional[Union[str, XSDDateTime]] = None
    error: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActionLifecycleId):
            self.id = ActionLifecycleId(self.id)

        if self._is_empty(self.phase):
            self.MissingRequiredField("phase")
        if not isinstance(self.phase, list):
            self.phase = [self.phase] if self.phase is not None else []
        self.phase = [v if isinstance(v, ArrayOfAction) else ArrayOfAction(**as_dict(v)) for v in self.phase]

        if self.actionCount is not None and not isinstance(self.actionCount, UcoNonNegativeInteger):
            self.actionCount = UcoNonNegativeInteger(self.actionCount)

        if self.actionStatus is not None and not isinstance(self.actionStatus, (ActionStatusTypeVocab, str)):
            value = self.actionStatus
            for _coerce in (lambda: ActionStatusTypeVocab(value), lambda: str(value)):
                try:
                    self.actionStatus = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[ActionStatusTypeVocab, str] could be constructed from {value!r} for slot actionStatus")

        if self.action_endTime is not None and not isinstance(self.action_endTime, XSDDateTime):
            self.action_endTime = XSDDateTime(self.action_endTime)

        if self.action_startTime is not None and not isinstance(self.action_startTime, XSDDateTime):
            self.action_startTime = XSDDateTime(self.action_startTime)

        if not isinstance(self.error, list):
            self.error = [self.error] if self.error is not None else []
        self.error = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.error]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ActionPattern(Action):
    """
    An action pattern is a grouping of characteristics unique to a combination of actions forming a consistent or
    characteristic arrangement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ACTION["ActionPattern"]
    class_class_curie: ClassVar[str] = "uco-action:ActionPattern"
    class_name: ClassVar[str] = "ActionPattern"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ActionPattern

    id: Union[str, ActionPatternId] = None
    type: Optional[Union[str, URIorCURIE]] = None
    createdBy: Optional[Union[str, IdentityAbstractionId]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    externalReference: Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]] = empty_list()
    hasFacet: Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    objectMarking: Optional[Union[Union[str, MarkingDefinitionAbstractionId], list[Union[str, MarkingDefinitionAbstractionId]]]] = empty_list()
    objectStatus: Optional[Union[str, "ObjectStatusVocab"]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActionPatternId):
            self.id = ActionPatternId(self.id)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.createdBy is not None and not isinstance(self.createdBy, IdentityAbstractionId):
            self.createdBy = IdentityAbstractionId(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, ExternalReference) else ExternalReference(**as_dict(v)) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, Facet) else Facet(**as_dict(v)) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstractionId) else MarkingDefinitionAbstractionId(v) for v in self.objectMarking]

        if self.objectStatus is not None and not isinstance(self.objectStatus, ObjectStatusVocab):
            self.objectStatus = ObjectStatusVocab(self.objectStatus)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ArrayOfAction(UcoInherentCharacterizationThing):
    """
    An array of action is an ordered list of references to things that may be done or performed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ACTION["ArrayOfAction"]
    class_class_curie: ClassVar[str] = "uco-action:ArrayOfAction"
    class_name: ClassVar[str] = "ArrayOfAction"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ArrayOfAction

    action: Union[Union[str, ActionId], list[Union[str, ActionId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, list):
            self.action = [self.action] if self.action is not None else []
        self.action = [v if isinstance(v, ActionId) else ActionId(v) for v in self.action]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Technique(UcoType):
    """
    A technique is a class of actions joined by some common characteristics. The class uco-action:Technique is a
    metaclass. A Technique instance is an owl:Class that is a subclass of uco-action:Action.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ACTION["Technique"]
    class_class_curie: ClassVar[str] = "uco-action:Technique"
    class_name: ClassVar[str] = "Technique"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Technique

    id: Union[str, TechniqueId] = None
    techniqueID: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TechniqueId):
            self.id = TechniqueId(self.id)

        if not isinstance(self.techniqueID, list):
            self.techniqueID = [self.techniqueID] if self.techniqueID is not None else []
        self.techniqueID = [v if isinstance(v, str) else str(v) for v in self.techniqueID]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Analysis(Action):
    """
    An analysis is an action of detailed examination of something in order to understand its nature, context or
    essential features.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ANALYSIS["Analysis"]
    class_class_curie: ClassVar[str] = "uco-analysis:Analysis"
    class_name: ClassVar[str] = "Analysis"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Analysis

    id: Union[str, AnalysisId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisId):
            self.id = AnalysisId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AnalyticResult(Assertion):
    """
    An analytic result is a characterization of the understanding resulting from an analysis action.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ANALYSIS["AnalyticResult"]
    class_class_curie: ClassVar[str] = "uco-analysis:AnalyticResult"
    class_name: ClassVar[str] = "AnalyticResult"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AnalyticResult

    id: Union[str, AnalyticResultId] = None
    originatingAnalysis: Optional[Union[str, AnalysisId]] = None
    resultContent: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalyticResultId):
            self.id = AnalyticResultId(self.id)

        if self.originatingAnalysis is not None and not isinstance(self.originatingAnalysis, AnalysisId):
            self.originatingAnalysis = AnalysisId(self.originatingAnalysis)

        if not isinstance(self.resultContent, list):
            self.resultContent = [self.resultContent] if self.resultContent is not None else []
        self.resultContent = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.resultContent]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class AnalyticResultFacet(Facet):
    """
    An analytic result facet is a grouping of characteristics unique to the results of an analysis action.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ANALYSIS["AnalyticResultFacet"]
    class_class_curie: ClassVar[str] = "uco-analysis:AnalyticResultFacet"
    class_name: ClassVar[str] = "AnalyticResultFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AnalyticResultFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ArtifactClassification(UcoInherentCharacterizationThing):
    """
    An artifact classification is a single specific assertion that a particular class of a classification taxonomy
    applies to something.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ANALYSIS["ArtifactClassification"]
    class_class_curie: ClassVar[str] = "uco-analysis:ArtifactClassification"
    class_name: ClassVar[str] = "ArtifactClassification"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ArtifactClassification

    class_: Union[str, list[str]] = None
    classificationConfidence: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.class_):
            self.MissingRequiredField("class_")
        if not isinstance(self.class_, list):
            self.class_ = [self.class_] if self.class_ is not None else []
        self.class_ = [v if isinstance(v, str) else str(v) for v in self.class_]

        if self.classificationConfidence is not None and not isinstance(self.classificationConfidence, Decimal):
            self.classificationConfidence = Decimal(self.classificationConfidence)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ArtifactClassificationResultFacet(AnalyticResultFacet):
    """
    An artifact classification result facet is a grouping of characteristics unique to the results of an artifact
    classification analysis action.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_ANALYSIS["ArtifactClassificationResultFacet"]
    class_class_curie: ClassVar[str] = "uco-analysis:ArtifactClassificationResultFacet"
    class_name: ClassVar[str] = "ArtifactClassificationResultFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ArtifactClassificationResultFacet

    classification: Optional[Union[Union[dict, ArtifactClassification], list[Union[dict, ArtifactClassification]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="classification", slot_type=ArtifactClassification, key_name="class", keyed=False)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AccountAuthenticationFacet(Facet):
    """
    An account authentication facet is a grouping of characteristics unique to the mechanism of accessing an account.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AccountAuthenticationFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:AccountAuthenticationFacet"
    class_name: ClassVar[str] = "AccountAuthenticationFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AccountAuthenticationFacet

    password: Optional[str] = None
    passwordLastChanged: Optional[Union[str, XSDDateTime]] = None
    passwordType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.password is not None and not isinstance(self.password, str):
            self.password = str(self.password)

        if self.passwordLastChanged is not None and not isinstance(self.passwordLastChanged, XSDDateTime):
            self.passwordLastChanged = XSDDateTime(self.passwordLastChanged)

        if self.passwordType is not None and not isinstance(self.passwordType, str):
            self.passwordType = str(self.passwordType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AccountFacet(Facet):
    """
    An account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control
    the provision of some capability or service.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AccountFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:AccountFacet"
    class_name: ClassVar[str] = "AccountFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AccountFacet

    accountIdentifier: Optional[str] = None
    accountIssuer: Optional[Union[str, UcoObjectId]] = None
    accountType: Optional[Union[str, "AccountTypeVocab"]] = None
    expirationTime: Optional[Union[str, XSDDateTime]] = None
    isActive: Optional[Union[bool, Bool]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    observable_modifiedTime: Optional[Union[str, XSDDateTime]] = None
    owner: Optional[Union[str, UcoObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.accountIdentifier is not None and not isinstance(self.accountIdentifier, str):
            self.accountIdentifier = str(self.accountIdentifier)

        if self.accountIssuer is not None and not isinstance(self.accountIssuer, UcoObjectId):
            self.accountIssuer = UcoObjectId(self.accountIssuer)

        if self.accountType is not None and not isinstance(self.accountType, (AccountTypeVocab, str)):
            value = self.accountType
            for _coerce in (lambda: AccountTypeVocab(value), lambda: str(value)):
                try:
                    self.accountType = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[AccountTypeVocab, str] could be constructed from {value!r} for slot accountType")

        if self.expirationTime is not None and not isinstance(self.expirationTime, XSDDateTime):
            self.expirationTime = XSDDateTime(self.expirationTime)

        if self.isActive is not None and not isinstance(self.isActive, Bool):
            self.isActive = Bool(self.isActive)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.observable_modifiedTime is not None and not isinstance(self.observable_modifiedTime, XSDDateTime):
            self.observable_modifiedTime = XSDDateTime(self.observable_modifiedTime)

        if self.owner is not None and not isinstance(self.owner, UcoObjectId):
            self.owner = UcoObjectId(self.owner)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AlternateDataStreamFacet(Facet):
    """
    An alternate data stream facet is a grouping of characteristics unique to data content stored within an NTFS file
    that is independent of the standard content stream of the file and is hidden from access by default NTFS file
    viewing mechanisms.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AlternateDataStreamFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:AlternateDataStreamFacet"
    class_name: ClassVar[str] = "AlternateDataStreamFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AlternateDataStreamFacet

    hashes: Optional[Union[dict, Hash]] = None
    name: Optional[str] = None
    size: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.hashes is not None and not isinstance(self.hashes, Hash):
            self.hashes = Hash(**as_dict(self.hashes))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AndroidDeviceFacet(Facet):
    """
    An Android device facet is a grouping of characteristics unique to an Android device. [based on
    https://en.wikipedia.org/wiki/Android_(operating_system)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AndroidDeviceFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:AndroidDeviceFacet"
    class_name: ClassVar[str] = "AndroidDeviceFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AndroidDeviceFacet

    androidFingerprint: Optional[str] = None
    androidID: Optional[Union[str, UcoHexBinary]] = None
    androidVersion: Optional[str] = None
    isADBRootEnabled: Optional[Union[bool, Bool]] = None
    isSURootEnabled: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.androidFingerprint is not None and not isinstance(self.androidFingerprint, str):
            self.androidFingerprint = str(self.androidFingerprint)

        if self.androidID is not None and not isinstance(self.androidID, UcoHexBinary):
            self.androidID = UcoHexBinary(self.androidID)

        if self.androidVersion is not None and not isinstance(self.androidVersion, str):
            self.androidVersion = str(self.androidVersion)

        if self.isADBRootEnabled is not None and not isinstance(self.isADBRootEnabled, Bool):
            self.isADBRootEnabled = Bool(self.isADBRootEnabled)

        if self.isSURootEnabled is not None and not isinstance(self.isSURootEnabled, Bool):
            self.isSURootEnabled = Bool(self.isSURootEnabled)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AntennaFacet(Facet):
    """
    An antenna alignment facet contains the metadata surrounding the cell tower's antenna position.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AntennaFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:AntennaFacet"
    class_name: ClassVar[str] = "AntennaFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AntennaFacet

    antennaHeight: Optional[Decimal] = None
    azimuth: Optional[Decimal] = None
    elevation: Optional[Decimal] = None
    horizontalBeamWidth: Optional[Decimal] = None
    signalStrength: Optional[Decimal] = None
    skew: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.antennaHeight is not None and not isinstance(self.antennaHeight, Decimal):
            self.antennaHeight = Decimal(self.antennaHeight)

        if self.azimuth is not None and not isinstance(self.azimuth, Decimal):
            self.azimuth = Decimal(self.azimuth)

        if self.elevation is not None and not isinstance(self.elevation, Decimal):
            self.elevation = Decimal(self.elevation)

        if self.horizontalBeamWidth is not None and not isinstance(self.horizontalBeamWidth, Decimal):
            self.horizontalBeamWidth = Decimal(self.horizontalBeamWidth)

        if self.signalStrength is not None and not isinstance(self.signalStrength, Decimal):
            self.signalStrength = Decimal(self.signalStrength)

        if self.skew is not None and not isinstance(self.skew, Decimal):
            self.skew = Decimal(self.skew)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ApplicationAccountFacet(Facet):
    """
    An application account facet is a grouping of characteristics unique to an account within a particular software
    program designed for end users.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ApplicationAccountFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ApplicationAccountFacet"
    class_name: ClassVar[str] = "ApplicationAccountFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ApplicationAccountFacet

    application: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ApplicationFacet(Facet):
    """
    An application facet is a grouping of characteristics unique to a particular software program designed for end
    users.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ApplicationFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ApplicationFacet"
    class_name: ClassVar[str] = "ApplicationFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ApplicationFacet

    applicationIdentifier: Optional[str] = None
    installedVersionHistory: Optional[Union[Union[dict, "ApplicationVersion"], list[Union[dict, "ApplicationVersion"]]]] = empty_list()
    numberOfLaunches: Optional[int] = None
    observable_version: Optional[str] = None
    operatingSystem: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.applicationIdentifier is not None and not isinstance(self.applicationIdentifier, str):
            self.applicationIdentifier = str(self.applicationIdentifier)

        if not isinstance(self.installedVersionHistory, list):
            self.installedVersionHistory = [self.installedVersionHistory] if self.installedVersionHistory is not None else []
        self.installedVersionHistory = [v if isinstance(v, ApplicationVersion) else ApplicationVersion(**as_dict(v)) for v in self.installedVersionHistory]

        if self.numberOfLaunches is not None and not isinstance(self.numberOfLaunches, int):
            self.numberOfLaunches = int(self.numberOfLaunches)

        if self.observable_version is not None and not isinstance(self.observable_version, str):
            self.observable_version = str(self.observable_version)

        if self.operatingSystem is not None and not isinstance(self.operatingSystem, ObservableObjectId):
            self.operatingSystem = ObservableObjectId(self.operatingSystem)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ApplicationVersion(UcoInherentCharacterizationThing):
    """
    An application version is a grouping of characteristics unique to a particular software program version.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ApplicationVersion"]
    class_class_curie: ClassVar[str] = "uco-observable:ApplicationVersion"
    class_name: ClassVar[str] = "ApplicationVersion"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ApplicationVersion

    installDate: Optional[Union[str, XSDDateTime]] = None
    observable_version: Optional[str] = None
    uninstallDate: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.installDate is not None and not isinstance(self.installDate, XSDDateTime):
            self.installDate = XSDDateTime(self.installDate)

        if self.observable_version is not None and not isinstance(self.observable_version, str):
            self.observable_version = str(self.observable_version)

        if self.uninstallDate is not None and not isinstance(self.uninstallDate, XSDDateTime):
            self.uninstallDate = XSDDateTime(self.uninstallDate)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ArchiveFileFacet(Facet):
    """
    An archive file facet is a grouping of characteristics unique to a file that is composed of one or more computer
    files along with metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ArchiveFileFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ArchiveFileFacet"
    class_name: ClassVar[str] = "ArchiveFileFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ArchiveFileFacet

    archiveType: Optional[str] = None
    comment: Optional[str] = None
    observable_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.archiveType is not None and not isinstance(self.archiveType, str):
            self.archiveType = str(self.archiveType)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if self.observable_version is not None and not isinstance(self.observable_version, str):
            self.observable_version = str(self.observable_version)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AudioFacet(Facet):
    """
    An audio facet is a grouping of characteristics unique to a digital representation of sound.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AudioFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:AudioFacet"
    class_name: ClassVar[str] = "AudioFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AudioFacet

    audioType: Optional[str] = None
    bitRate: Optional[int] = None
    duration: Optional[int] = None
    format: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.audioType is not None and not isinstance(self.audioType, str):
            self.audioType = str(self.audioType)

        if self.bitRate is not None and not isinstance(self.bitRate, int):
            self.bitRate = int(self.bitRate)

        if self.duration is not None and not isinstance(self.duration, int):
            self.duration = int(self.duration)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AutonomousSystemFacet(Facet):
    """
    An autonomous system facet is a grouping of characteristics unique to a collection of connected Internet Protocol
    (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative
    entity or domain that presents a common, clearly defined routing policy to the Internet. [based on
    https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AutonomousSystemFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:AutonomousSystemFacet"
    class_name: ClassVar[str] = "AutonomousSystemFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AutonomousSystemFacet

    asHandle: Optional[str] = None
    number: Optional[int] = None
    regionalInternetRegistry: Optional[Union[str, "RegionalRegistryTypeVocab"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.asHandle is not None and not isinstance(self.asHandle, str):
            self.asHandle = str(self.asHandle)

        if self.number is not None and not isinstance(self.number, int):
            self.number = int(self.number)

        if self.regionalInternetRegistry is not None and not isinstance(self.regionalInternetRegistry, (RegionalRegistryTypeVocab, str)):
            value = self.regionalInternetRegistry
            for _coerce in (lambda: RegionalRegistryTypeVocab(value), lambda: str(value)):
                try:
                    self.regionalInternetRegistry = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[RegionalRegistryTypeVocab, str] could be constructed from {value!r} for slot regionalInternetRegistry")

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BrowserBookmarkFacet(Facet):
    """
    A browser bookmark facet is a grouping of characteristics unique to a saved shortcut that directs a WWW (World
    Wide Web) browser software program to a particular WWW accessible resource. [based on
    https://techterms.com/definition/bookmark]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["BrowserBookmarkFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:BrowserBookmarkFacet"
    class_name: ClassVar[str] = "BrowserBookmarkFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BrowserBookmarkFacet

    accessedTime: Optional[Union[str, XSDDateTime]] = None
    application: Optional[Union[str, ObservableObjectId]] = None
    bookmarkPath: Optional[str] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    observable_modifiedTime: Optional[Union[str, XSDDateTime]] = None
    urlTargeted: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    visitCount: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.accessedTime is not None and not isinstance(self.accessedTime, XSDDateTime):
            self.accessedTime = XSDDateTime(self.accessedTime)

        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if self.bookmarkPath is not None and not isinstance(self.bookmarkPath, str):
            self.bookmarkPath = str(self.bookmarkPath)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.observable_modifiedTime is not None and not isinstance(self.observable_modifiedTime, XSDDateTime):
            self.observable_modifiedTime = XSDDateTime(self.observable_modifiedTime)

        if not isinstance(self.urlTargeted, list):
            self.urlTargeted = [self.urlTargeted] if self.urlTargeted is not None else []
        self.urlTargeted = [v if isinstance(v, URI) else URI(v) for v in self.urlTargeted]

        if self.visitCount is not None and not isinstance(self.visitCount, int):
            self.visitCount = int(self.visitCount)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BrowserCookieFacet(Facet):
    """
    A browser cookie facet is a grouping of characteristics unique to a piece of data sent from a website and stored
    on the user's computer by the user's web browser while the user is browsing. [based on
    https://en.wikipedia.org/wiki/HTTP_cookie]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["BrowserCookieFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:BrowserCookieFacet"
    class_name: ClassVar[str] = "BrowserCookieFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BrowserCookieFacet

    accessedTime: Optional[Union[str, XSDDateTime]] = None
    application: Optional[Union[str, ObservableObjectId]] = None
    cookieDomain: Optional[Union[str, ObservableObjectId]] = None
    cookieName: Optional[str] = None
    cookiePath: Optional[str] = None
    expirationTime: Optional[Union[str, XSDDateTime]] = None
    isSecure: Optional[Union[bool, Bool]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.accessedTime is not None and not isinstance(self.accessedTime, XSDDateTime):
            self.accessedTime = XSDDateTime(self.accessedTime)

        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if self.cookieDomain is not None and not isinstance(self.cookieDomain, ObservableObjectId):
            self.cookieDomain = ObservableObjectId(self.cookieDomain)

        if self.cookieName is not None and not isinstance(self.cookieName, str):
            self.cookieName = str(self.cookieName)

        if self.cookiePath is not None and not isinstance(self.cookiePath, str):
            self.cookiePath = str(self.cookiePath)

        if self.expirationTime is not None and not isinstance(self.expirationTime, XSDDateTime):
            self.expirationTime = XSDDateTime(self.expirationTime)

        if self.isSecure is not None and not isinstance(self.isSecure, Bool):
            self.isSecure = Bool(self.isSecure)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CalendarEntryFacet(Facet):
    """
    A calendar entry facet is a grouping of characteristics unique to an appointment, meeting, or event within a
    collection of appointments, meetings, and events.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CalendarEntryFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:CalendarEntryFacet"
    class_name: ClassVar[str] = "CalendarEntryFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CalendarEntryFacet

    application: Optional[Union[str, ObservableObjectId]] = None
    attendant: Optional[Union[Union[str, IdentityId], list[Union[str, IdentityId]]]] = empty_list()
    duration: Optional[int] = None
    eventStatus: Optional[str] = None
    isPrivate: Optional[Union[bool, Bool]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    observable_endTime: Optional[Union[str, XSDDateTime]] = None
    observable_eventType: Optional[str] = None
    observable_location: Optional[Union[str, LocationId]] = None
    observable_modifiedTime: Optional[Union[str, XSDDateTime]] = None
    observable_startTime: Optional[Union[str, XSDDateTime]] = None
    owner: Optional[Union[str, UcoObjectId]] = None
    recurrence: Optional[str] = None
    remindTime: Optional[Union[str, XSDDateTime]] = None
    subject: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if not isinstance(self.attendant, list):
            self.attendant = [self.attendant] if self.attendant is not None else []
        self.attendant = [v if isinstance(v, IdentityId) else IdentityId(v) for v in self.attendant]

        if self.duration is not None and not isinstance(self.duration, int):
            self.duration = int(self.duration)

        if self.eventStatus is not None and not isinstance(self.eventStatus, str):
            self.eventStatus = str(self.eventStatus)

        if self.isPrivate is not None and not isinstance(self.isPrivate, Bool):
            self.isPrivate = Bool(self.isPrivate)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.observable_endTime is not None and not isinstance(self.observable_endTime, XSDDateTime):
            self.observable_endTime = XSDDateTime(self.observable_endTime)

        if self.observable_eventType is not None and not isinstance(self.observable_eventType, str):
            self.observable_eventType = str(self.observable_eventType)

        if self.observable_location is not None and not isinstance(self.observable_location, LocationId):
            self.observable_location = LocationId(self.observable_location)

        if self.observable_modifiedTime is not None and not isinstance(self.observable_modifiedTime, XSDDateTime):
            self.observable_modifiedTime = XSDDateTime(self.observable_modifiedTime)

        if self.observable_startTime is not None and not isinstance(self.observable_startTime, XSDDateTime):
            self.observable_startTime = XSDDateTime(self.observable_startTime)

        if self.owner is not None and not isinstance(self.owner, UcoObjectId):
            self.owner = UcoObjectId(self.owner)

        if self.recurrence is not None and not isinstance(self.recurrence, str):
            self.recurrence = str(self.recurrence)

        if self.remindTime is not None and not isinstance(self.remindTime, XSDDateTime):
            self.remindTime = XSDDateTime(self.remindTime)

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CalendarFacet(Facet):
    """
    A calendar facet is a grouping of characteristics unique to a collection of appointments, meetings, and events.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CalendarFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:CalendarFacet"
    class_name: ClassVar[str] = "CalendarFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CalendarFacet

    application: Optional[Union[str, ObservableObjectId]] = None
    owner: Optional[Union[str, UcoObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if self.owner is not None and not isinstance(self.owner, UcoObjectId):
            self.owner = UcoObjectId(self.owner)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CallFacet(Facet):
    """
    A call facet is a grouping of characteristics unique to a connection as part of a realtime cyber communication
    between one or more parties.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CallFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:CallFacet"
    class_name: ClassVar[str] = "CallFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CallFacet

    application: Optional[Union[str, ObservableObjectId]] = None
    callType: Optional[str] = None
    duration: Optional[int] = None
    from_: Optional[Union[str, ObservableObjectId]] = None
    observable_endTime: Optional[Union[str, XSDDateTime]] = None
    observable_participant: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    observable_startTime: Optional[Union[str, XSDDateTime]] = None
    to: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if self.callType is not None and not isinstance(self.callType, str):
            self.callType = str(self.callType)

        if self.duration is not None and not isinstance(self.duration, int):
            self.duration = int(self.duration)

        if self.from_ is not None and not isinstance(self.from_, ObservableObjectId):
            self.from_ = ObservableObjectId(self.from_)

        if self.observable_endTime is not None and not isinstance(self.observable_endTime, XSDDateTime):
            self.observable_endTime = XSDDateTime(self.observable_endTime)

        if not isinstance(self.observable_participant, list):
            self.observable_participant = [self.observable_participant] if self.observable_participant is not None else []
        self.observable_participant = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.observable_participant]

        if self.observable_startTime is not None and not isinstance(self.observable_startTime, XSDDateTime):
            self.observable_startTime = XSDDateTime(self.observable_startTime)

        if not isinstance(self.to, list):
            self.to = [self.to] if self.to is not None else []
        self.to = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.to]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CapturedTelecommunicationsInformationFacet(Facet):
    """
    A captured telecommunications information facet represents certain information within captured or intercepted
    telecommunications data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CapturedTelecommunicationsInformationFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:CapturedTelecommunicationsInformationFacet"
    class_name: ClassVar[str] = "CapturedTelecommunicationsInformationFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CapturedTelecommunicationsInformationFacet

    captureCellSite: Union[str, CellSiteId] = None
    interceptedCallState: Optional[str] = None
    observable_endTime: Optional[Union[str, XSDDateTime]] = None
    observable_startTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.captureCellSite):
            self.MissingRequiredField("captureCellSite")
        if not isinstance(self.captureCellSite, CellSiteId):
            self.captureCellSite = CellSiteId(self.captureCellSite)

        if self.interceptedCallState is not None and not isinstance(self.interceptedCallState, str):
            self.interceptedCallState = str(self.interceptedCallState)

        if self.observable_endTime is not None and not isinstance(self.observable_endTime, XSDDateTime):
            self.observable_endTime = XSDDateTime(self.observable_endTime)

        if self.observable_startTime is not None and not isinstance(self.observable_startTime, XSDDateTime):
            self.observable_startTime = XSDDateTime(self.observable_startTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CellSiteFacet(Facet):
    """
    A cell site facet contains the metadata surrounding the cell site.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CellSiteFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:CellSiteFacet"
    class_name: ClassVar[str] = "CellSiteFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CellSiteFacet

    cellSiteCountryCode: Optional[str] = None
    cellSiteIdentifier: Optional[str] = None
    cellSiteLocationAreaCode: Optional[str] = None
    cellSiteNetworkCode: Optional[str] = None
    cellSiteType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cellSiteCountryCode is not None and not isinstance(self.cellSiteCountryCode, str):
            self.cellSiteCountryCode = str(self.cellSiteCountryCode)

        if self.cellSiteIdentifier is not None and not isinstance(self.cellSiteIdentifier, str):
            self.cellSiteIdentifier = str(self.cellSiteIdentifier)

        if self.cellSiteLocationAreaCode is not None and not isinstance(self.cellSiteLocationAreaCode, str):
            self.cellSiteLocationAreaCode = str(self.cellSiteLocationAreaCode)

        if self.cellSiteNetworkCode is not None and not isinstance(self.cellSiteNetworkCode, str):
            self.cellSiteNetworkCode = str(self.cellSiteNetworkCode)

        if self.cellSiteType is not None and not isinstance(self.cellSiteType, str):
            self.cellSiteType = str(self.cellSiteType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CompressedStreamFacet(Facet):
    """
    A compressed stream facet is a grouping of characteristics unique to the application of a size-reduction process
    to a body of data content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CompressedStreamFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:CompressedStreamFacet"
    class_name: ClassVar[str] = "CompressedStreamFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CompressedStreamFacet

    compressionMethod: Optional[str] = None
    compressionRatio: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.compressionMethod is not None and not isinstance(self.compressionMethod, str):
            self.compressionMethod = str(self.compressionMethod)

        if self.compressionRatio is not None and not isinstance(self.compressionRatio, Decimal):
            self.compressionRatio = Decimal(self.compressionRatio)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ComputerSpecificationFacet(Facet):
    """
    A computer specificaiton facet is a grouping of characteristics unique to the hardware and software of a
    programmable electronic device that can store, retrieve, and process data. [based on
    merriam-webster.com/dictionary/computer]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ComputerSpecificationFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ComputerSpecificationFacet"
    class_name: ClassVar[str] = "ComputerSpecificationFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ComputerSpecificationFacet

    availableRam: Optional[int] = None
    biosDate: Optional[Union[str, XSDDateTime]] = None
    biosManufacturer: Optional[str] = None
    biosReleaseDate: Optional[Union[str, XSDDateTime]] = None
    biosSerialNumber: Optional[str] = None
    biosVersion: Optional[str] = None
    cpu: Optional[str] = None
    cpuFamily: Optional[str] = None
    currentSystemDate: Optional[Union[str, XSDDateTime]] = None
    gpu: Optional[str] = None
    gpuFamily: Optional[str] = None
    hostname: Optional[str] = None
    localTime: Optional[Union[str, XSDDateTime]] = None
    networkInterface: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    processorArchitecture: Optional[str] = None
    systemTime: Optional[Union[str, XSDDateTime]] = None
    timezoneDST: Optional[str] = None
    timezoneStandard: Optional[str] = None
    totalRam: Optional[int] = None
    uptime: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.availableRam is not None and not isinstance(self.availableRam, int):
            self.availableRam = int(self.availableRam)

        if self.biosDate is not None and not isinstance(self.biosDate, XSDDateTime):
            self.biosDate = XSDDateTime(self.biosDate)

        if self.biosManufacturer is not None and not isinstance(self.biosManufacturer, str):
            self.biosManufacturer = str(self.biosManufacturer)

        if self.biosReleaseDate is not None and not isinstance(self.biosReleaseDate, XSDDateTime):
            self.biosReleaseDate = XSDDateTime(self.biosReleaseDate)

        if self.biosSerialNumber is not None and not isinstance(self.biosSerialNumber, str):
            self.biosSerialNumber = str(self.biosSerialNumber)

        if self.biosVersion is not None and not isinstance(self.biosVersion, str):
            self.biosVersion = str(self.biosVersion)

        if self.cpu is not None and not isinstance(self.cpu, str):
            self.cpu = str(self.cpu)

        if self.cpuFamily is not None and not isinstance(self.cpuFamily, str):
            self.cpuFamily = str(self.cpuFamily)

        if self.currentSystemDate is not None and not isinstance(self.currentSystemDate, XSDDateTime):
            self.currentSystemDate = XSDDateTime(self.currentSystemDate)

        if self.gpu is not None and not isinstance(self.gpu, str):
            self.gpu = str(self.gpu)

        if self.gpuFamily is not None and not isinstance(self.gpuFamily, str):
            self.gpuFamily = str(self.gpuFamily)

        if self.hostname is not None and not isinstance(self.hostname, str):
            self.hostname = str(self.hostname)

        if self.localTime is not None and not isinstance(self.localTime, XSDDateTime):
            self.localTime = XSDDateTime(self.localTime)

        if not isinstance(self.networkInterface, list):
            self.networkInterface = [self.networkInterface] if self.networkInterface is not None else []
        self.networkInterface = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.networkInterface]

        if self.processorArchitecture is not None and not isinstance(self.processorArchitecture, str):
            self.processorArchitecture = str(self.processorArchitecture)

        if self.systemTime is not None and not isinstance(self.systemTime, XSDDateTime):
            self.systemTime = XSDDateTime(self.systemTime)

        if self.timezoneDST is not None and not isinstance(self.timezoneDST, str):
            self.timezoneDST = str(self.timezoneDST)

        if self.timezoneStandard is not None and not isinstance(self.timezoneStandard, str):
            self.timezoneStandard = str(self.timezoneStandard)

        if self.totalRam is not None and not isinstance(self.totalRam, int):
            self.totalRam = int(self.totalRam)

        if self.uptime is not None and not isinstance(self.uptime, str):
            self.uptime = str(self.uptime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContactAddress(UcoInherentCharacterizationThing):
    """
    A contact address is a grouping of characteristics unique to a geolocation address of a contact entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContactAddress"]
    class_class_curie: ClassVar[str] = "uco-observable:ContactAddress"
    class_name: ClassVar[str] = "ContactAddress"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContactAddress

    contactAddressScope: Optional[Union[str, "ContactAddressScopeVocab"]] = None
    geolocationAddress: Optional[Union[str, LocationId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contactAddressScope is not None and not isinstance(self.contactAddressScope, (ContactAddressScopeVocab, str)):
            value = self.contactAddressScope
            for _coerce in (lambda: ContactAddressScopeVocab(value), lambda: str(value)):
                try:
                    self.contactAddressScope = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[ContactAddressScopeVocab, str] could be constructed from {value!r} for slot contactAddressScope")

        if self.geolocationAddress is not None and not isinstance(self.geolocationAddress, LocationId):
            self.geolocationAddress = LocationId(self.geolocationAddress)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContactAffiliation(UcoInherentCharacterizationThing):
    """
    A contact affiliation is a grouping of characteristics unique to details of an organizational affiliation for a
    single contact entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContactAffiliation"]
    class_class_curie: ClassVar[str] = "uco-observable:ContactAffiliation"
    class_name: ClassVar[str] = "ContactAffiliation"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContactAffiliation

    contactEmail: Optional[Union[Union[dict, "ContactEmail"], list[Union[dict, "ContactEmail"]]]] = empty_list()
    contactMessaging: Optional[Union[Union[dict, "ContactMessaging"], list[Union[dict, "ContactMessaging"]]]] = empty_list()
    contactOrganization: Optional[Union[str, OrganizationId]] = None
    contactPhone: Optional[Union[Union[dict, "ContactPhone"], list[Union[dict, "ContactPhone"]]]] = empty_list()
    contactProfile: Optional[Union[Union[dict, "ContactProfile"], list[Union[dict, "ContactProfile"]]]] = empty_list()
    contactURL: Optional[Union[Union[dict, "ContactURL"], list[Union[dict, "ContactURL"]]]] = empty_list()
    organizationDepartment: Optional[str] = None
    organizationLocation: Optional[Union[Union[dict, ContactAddress], list[Union[dict, ContactAddress]]]] = empty_list()
    organizationPosition: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.contactEmail, list):
            self.contactEmail = [self.contactEmail] if self.contactEmail is not None else []
        self.contactEmail = [v if isinstance(v, ContactEmail) else ContactEmail(**as_dict(v)) for v in self.contactEmail]

        if not isinstance(self.contactMessaging, list):
            self.contactMessaging = [self.contactMessaging] if self.contactMessaging is not None else []
        self.contactMessaging = [v if isinstance(v, ContactMessaging) else ContactMessaging(**as_dict(v)) for v in self.contactMessaging]

        if self.contactOrganization is not None and not isinstance(self.contactOrganization, OrganizationId):
            self.contactOrganization = OrganizationId(self.contactOrganization)

        if not isinstance(self.contactPhone, list):
            self.contactPhone = [self.contactPhone] if self.contactPhone is not None else []
        self.contactPhone = [v if isinstance(v, ContactPhone) else ContactPhone(**as_dict(v)) for v in self.contactPhone]

        if not isinstance(self.contactProfile, list):
            self.contactProfile = [self.contactProfile] if self.contactProfile is not None else []
        self.contactProfile = [v if isinstance(v, ContactProfile) else ContactProfile(**as_dict(v)) for v in self.contactProfile]

        if not isinstance(self.contactURL, list):
            self.contactURL = [self.contactURL] if self.contactURL is not None else []
        self.contactURL = [v if isinstance(v, ContactURL) else ContactURL(**as_dict(v)) for v in self.contactURL]

        if self.organizationDepartment is not None and not isinstance(self.organizationDepartment, str):
            self.organizationDepartment = str(self.organizationDepartment)

        if not isinstance(self.organizationLocation, list):
            self.organizationLocation = [self.organizationLocation] if self.organizationLocation is not None else []
        self.organizationLocation = [v if isinstance(v, ContactAddress) else ContactAddress(**as_dict(v)) for v in self.organizationLocation]

        if self.organizationPosition is not None and not isinstance(self.organizationPosition, str):
            self.organizationPosition = str(self.organizationPosition)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContactEmail(UcoInherentCharacterizationThing):
    """
    A contact email is a grouping of characteristics unique to details for contacting a contact entity by email.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContactEmail"]
    class_class_curie: ClassVar[str] = "uco-observable:ContactEmail"
    class_name: ClassVar[str] = "ContactEmail"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContactEmail

    contactEmailScope: Optional[Union[str, "ContactEmailScopeVocab"]] = None
    emailAddress: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contactEmailScope is not None and not isinstance(self.contactEmailScope, (ContactEmailScopeVocab, str)):
            value = self.contactEmailScope
            for _coerce in (lambda: ContactEmailScopeVocab(value), lambda: str(value)):
                try:
                    self.contactEmailScope = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[ContactEmailScopeVocab, str] could be constructed from {value!r} for slot contactEmailScope")

        if self.emailAddress is not None and not isinstance(self.emailAddress, ObservableObjectId):
            self.emailAddress = ObservableObjectId(self.emailAddress)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContactFacet(Facet):
    """
    A contact facet is a grouping of characteristics unique to a set of identification and communication related
    details for a single entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContactFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ContactFacet"
    class_name: ClassVar[str] = "ContactFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContactFacet

    birthdate: Optional[Union[str, XSDDateTime]] = None
    contactAddress: Optional[Union[Union[dict, ContactAddress], list[Union[dict, ContactAddress]]]] = empty_list()
    contactAffiliation: Optional[Union[Union[dict, ContactAffiliation], list[Union[dict, ContactAffiliation]]]] = empty_list()
    contactEmail: Optional[Union[Union[dict, ContactEmail], list[Union[dict, ContactEmail]]]] = empty_list()
    contactGroup: Optional[Union[str, list[str]]] = empty_list()
    contactID: Optional[str] = None
    contactMessaging: Optional[Union[Union[dict, "ContactMessaging"], list[Union[dict, "ContactMessaging"]]]] = empty_list()
    contactNote: Optional[Union[str, list[str]]] = empty_list()
    contactPhone: Optional[Union[Union[dict, "ContactPhone"], list[Union[dict, "ContactPhone"]]]] = empty_list()
    contactProfile: Optional[Union[Union[dict, "ContactProfile"], list[Union[dict, "ContactProfile"]]]] = empty_list()
    contactSIP: Optional[Union[Union[dict, "ContactSIP"], list[Union[dict, "ContactSIP"]]]] = empty_list()
    contactURL: Optional[Union[Union[dict, "ContactURL"], list[Union[dict, "ContactURL"]]]] = empty_list()
    displayName: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    lastTimeContacted: Optional[Union[str, XSDDateTime]] = None
    middleName: Optional[str] = None
    namePhonetic: Optional[str] = None
    namePrefix: Optional[str] = None
    nameSuffix: Optional[str] = None
    nickname: Optional[Union[str, list[str]]] = empty_list()
    numberTimesContacted: Optional[int] = None
    sourceApplication: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.birthdate is not None and not isinstance(self.birthdate, XSDDateTime):
            self.birthdate = XSDDateTime(self.birthdate)

        if not isinstance(self.contactAddress, list):
            self.contactAddress = [self.contactAddress] if self.contactAddress is not None else []
        self.contactAddress = [v if isinstance(v, ContactAddress) else ContactAddress(**as_dict(v)) for v in self.contactAddress]

        if not isinstance(self.contactAffiliation, list):
            self.contactAffiliation = [self.contactAffiliation] if self.contactAffiliation is not None else []
        self.contactAffiliation = [v if isinstance(v, ContactAffiliation) else ContactAffiliation(**as_dict(v)) for v in self.contactAffiliation]

        if not isinstance(self.contactEmail, list):
            self.contactEmail = [self.contactEmail] if self.contactEmail is not None else []
        self.contactEmail = [v if isinstance(v, ContactEmail) else ContactEmail(**as_dict(v)) for v in self.contactEmail]

        if not isinstance(self.contactGroup, list):
            self.contactGroup = [self.contactGroup] if self.contactGroup is not None else []
        self.contactGroup = [v if isinstance(v, str) else str(v) for v in self.contactGroup]

        if self.contactID is not None and not isinstance(self.contactID, str):
            self.contactID = str(self.contactID)

        if not isinstance(self.contactMessaging, list):
            self.contactMessaging = [self.contactMessaging] if self.contactMessaging is not None else []
        self.contactMessaging = [v if isinstance(v, ContactMessaging) else ContactMessaging(**as_dict(v)) for v in self.contactMessaging]

        if not isinstance(self.contactNote, list):
            self.contactNote = [self.contactNote] if self.contactNote is not None else []
        self.contactNote = [v if isinstance(v, str) else str(v) for v in self.contactNote]

        if not isinstance(self.contactPhone, list):
            self.contactPhone = [self.contactPhone] if self.contactPhone is not None else []
        self.contactPhone = [v if isinstance(v, ContactPhone) else ContactPhone(**as_dict(v)) for v in self.contactPhone]

        if not isinstance(self.contactProfile, list):
            self.contactProfile = [self.contactProfile] if self.contactProfile is not None else []
        self.contactProfile = [v if isinstance(v, ContactProfile) else ContactProfile(**as_dict(v)) for v in self.contactProfile]

        if not isinstance(self.contactSIP, list):
            self.contactSIP = [self.contactSIP] if self.contactSIP is not None else []
        self.contactSIP = [v if isinstance(v, ContactSIP) else ContactSIP(**as_dict(v)) for v in self.contactSIP]

        if not isinstance(self.contactURL, list):
            self.contactURL = [self.contactURL] if self.contactURL is not None else []
        self.contactURL = [v if isinstance(v, ContactURL) else ContactURL(**as_dict(v)) for v in self.contactURL]

        if self.displayName is not None and not isinstance(self.displayName, str):
            self.displayName = str(self.displayName)

        if self.firstName is not None and not isinstance(self.firstName, str):
            self.firstName = str(self.firstName)

        if self.lastName is not None and not isinstance(self.lastName, str):
            self.lastName = str(self.lastName)

        if self.lastTimeContacted is not None and not isinstance(self.lastTimeContacted, XSDDateTime):
            self.lastTimeContacted = XSDDateTime(self.lastTimeContacted)

        if self.middleName is not None and not isinstance(self.middleName, str):
            self.middleName = str(self.middleName)

        if self.namePhonetic is not None and not isinstance(self.namePhonetic, str):
            self.namePhonetic = str(self.namePhonetic)

        if self.namePrefix is not None and not isinstance(self.namePrefix, str):
            self.namePrefix = str(self.namePrefix)

        if self.nameSuffix is not None and not isinstance(self.nameSuffix, str):
            self.nameSuffix = str(self.nameSuffix)

        if not isinstance(self.nickname, list):
            self.nickname = [self.nickname] if self.nickname is not None else []
        self.nickname = [v if isinstance(v, str) else str(v) for v in self.nickname]

        if self.numberTimesContacted is not None and not isinstance(self.numberTimesContacted, int):
            self.numberTimesContacted = int(self.numberTimesContacted)

        if self.sourceApplication is not None and not isinstance(self.sourceApplication, ObservableObjectId):
            self.sourceApplication = ObservableObjectId(self.sourceApplication)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContactListFacet(Facet):
    """
    A contact list facet is a grouping of characteristics unique to a set of multiple individual contacts such as that
    found in a digital address book.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContactListFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ContactListFacet"
    class_name: ClassVar[str] = "ContactListFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContactListFacet

    contact: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    sourceApplication: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.contact, list):
            self.contact = [self.contact] if self.contact is not None else []
        self.contact = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.contact]

        if self.sourceApplication is not None and not isinstance(self.sourceApplication, ObservableObjectId):
            self.sourceApplication = ObservableObjectId(self.sourceApplication)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContactMessaging(UcoInherentCharacterizationThing):
    """
    A contact messaging is a grouping of characteristics unique to details for contacting a contact entity by digital
    messaging.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContactMessaging"]
    class_class_curie: ClassVar[str] = "uco-observable:ContactMessaging"
    class_name: ClassVar[str] = "ContactMessaging"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContactMessaging

    contactMessagingPlatform: Optional[Union[str, ObservableObjectId]] = None
    messagingAddress: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contactMessagingPlatform is not None and not isinstance(self.contactMessagingPlatform, ObservableObjectId):
            self.contactMessagingPlatform = ObservableObjectId(self.contactMessagingPlatform)

        if self.messagingAddress is not None and not isinstance(self.messagingAddress, ObservableObjectId):
            self.messagingAddress = ObservableObjectId(self.messagingAddress)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContactPhone(UcoInherentCharacterizationThing):
    """
    A contact phone is a grouping of characteristics unique to details for contacting a contact entity by telephone.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContactPhone"]
    class_class_curie: ClassVar[str] = "uco-observable:ContactPhone"
    class_name: ClassVar[str] = "ContactPhone"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContactPhone

    contactPhoneNumber: Optional[Union[str, ObservableObjectId]] = None
    contactPhoneScope: Optional[Union[str, "ContactPhoneScopeVocab"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contactPhoneNumber is not None and not isinstance(self.contactPhoneNumber, ObservableObjectId):
            self.contactPhoneNumber = ObservableObjectId(self.contactPhoneNumber)

        if self.contactPhoneScope is not None and not isinstance(self.contactPhoneScope, (ContactPhoneScopeVocab, str)):
            value = self.contactPhoneScope
            for _coerce in (lambda: ContactPhoneScopeVocab(value), lambda: str(value)):
                try:
                    self.contactPhoneScope = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[ContactPhoneScopeVocab, str] could be constructed from {value!r} for slot contactPhoneScope")

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContactProfile(UcoInherentCharacterizationThing):
    """
    A contact profile is a grouping of characteristics unique to details for contacting a contact entity by online
    service.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContactProfile"]
    class_class_curie: ClassVar[str] = "uco-observable:ContactProfile"
    class_name: ClassVar[str] = "ContactProfile"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContactProfile

    contactProfilePlatform: Optional[Union[str, ObservableObjectId]] = None
    profile: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contactProfilePlatform is not None and not isinstance(self.contactProfilePlatform, ObservableObjectId):
            self.contactProfilePlatform = ObservableObjectId(self.contactProfilePlatform)

        if self.profile is not None and not isinstance(self.profile, ObservableObjectId):
            self.profile = ObservableObjectId(self.profile)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContactSIP(UcoInherentCharacterizationThing):
    """
    A contact SIP is a grouping of characteristics unique to details for contacting a contact entity by Session
    Initiation Protocol (SIP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContactSIP"]
    class_class_curie: ClassVar[str] = "uco-observable:ContactSIP"
    class_name: ClassVar[str] = "ContactSIP"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContactSIP

    contactSIPScope: Optional[Union[str, "ContactSIPScopeVocab"]] = None
    sipAddress: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contactSIPScope is not None and not isinstance(self.contactSIPScope, (ContactSIPScopeVocab, str)):
            value = self.contactSIPScope
            for _coerce in (lambda: ContactSIPScopeVocab(value), lambda: str(value)):
                try:
                    self.contactSIPScope = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[ContactSIPScopeVocab, str] could be constructed from {value!r} for slot contactSIPScope")

        if self.sipAddress is not None and not isinstance(self.sipAddress, ObservableObjectId):
            self.sipAddress = ObservableObjectId(self.sipAddress)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContactURL(UcoInherentCharacterizationThing):
    """
    A contact URL is a grouping of characteristics unique to details for contacting a contact entity by Uniform
    Resource Locator (URL).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContactURL"]
    class_class_curie: ClassVar[str] = "uco-observable:ContactURL"
    class_name: ClassVar[str] = "ContactURL"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContactURL

    contactURLScope: Optional[Union[str, "ContactURLScopeVocab"]] = None
    url: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contactURLScope is not None and not isinstance(self.contactURLScope, (ContactURLScopeVocab, str)):
            value = self.contactURLScope
            for _coerce in (lambda: ContactURLScopeVocab(value), lambda: str(value)):
                try:
                    self.contactURLScope = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[ContactURLScopeVocab, str] could be constructed from {value!r} for slot contactURLScope")

        if self.url is not None and not isinstance(self.url, ObservableObjectId):
            self.url = ObservableObjectId(self.url)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContentDataFacet(Facet):
    """
    A content data facet is a grouping of characteristics unique to a block of digital data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContentDataFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ContentDataFacet"
    class_name: ClassVar[str] = "ContentDataFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContentDataFacet

    byteOrder: Optional[Union[str, "EndiannessTypeVocab"]] = None
    dataPayload: Optional[str] = None
    dataPayloadReferenceURL: Optional[Union[str, ObservableObjectId]] = None
    entropy: Optional[Decimal] = None
    hash: Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]] = empty_list()
    isEncrypted: Optional[Union[bool, Bool]] = None
    magicNumber: Optional[str] = None
    mimeClass: Optional[str] = None
    mimeType: Optional[Union[str, list[str]]] = empty_list()
    sizeInBytes: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.byteOrder is not None and not isinstance(self.byteOrder, (EndiannessTypeVocab, str)):
            value = self.byteOrder
            for _coerce in (lambda: EndiannessTypeVocab(value), lambda: str(value)):
                try:
                    self.byteOrder = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[EndiannessTypeVocab, str] could be constructed from {value!r} for slot byteOrder")

        if self.dataPayload is not None and not isinstance(self.dataPayload, str):
            self.dataPayload = str(self.dataPayload)

        if self.dataPayloadReferenceURL is not None and not isinstance(self.dataPayloadReferenceURL, ObservableObjectId):
            self.dataPayloadReferenceURL = ObservableObjectId(self.dataPayloadReferenceURL)

        if self.entropy is not None and not isinstance(self.entropy, Decimal):
            self.entropy = Decimal(self.entropy)

        self._normalize_inlined_as_list(slot_name="hash", slot_type=Hash, key_name="hashMethod", keyed=False)

        if self.isEncrypted is not None and not isinstance(self.isEncrypted, Bool):
            self.isEncrypted = Bool(self.isEncrypted)

        if self.magicNumber is not None and not isinstance(self.magicNumber, str):
            self.magicNumber = str(self.magicNumber)

        if self.mimeClass is not None and not isinstance(self.mimeClass, str):
            self.mimeClass = str(self.mimeClass)

        if not isinstance(self.mimeType, list):
            self.mimeType = [self.mimeType] if self.mimeType is not None else []
        self.mimeType = [v if isinstance(v, str) else str(v) for v in self.mimeType]

        if self.sizeInBytes is not None and not isinstance(self.sizeInBytes, int):
            self.sizeInBytes = int(self.sizeInBytes)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DataRangeFacet(Facet):
    """
    A data range facet is a grouping of characteristics unique to a particular contiguous scope within a block of
    digital data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DataRangeFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:DataRangeFacet"
    class_name: ClassVar[str] = "DataRangeFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DataRangeFacet

    rangeOffset: Optional[int] = None
    rangeOffsetType: Optional[str] = None
    rangeSize: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.rangeOffset is not None and not isinstance(self.rangeOffset, int):
            self.rangeOffset = int(self.rangeOffset)

        if self.rangeOffsetType is not None and not isinstance(self.rangeOffsetType, str):
            self.rangeOffsetType = str(self.rangeOffsetType)

        if self.rangeSize is not None and not isinstance(self.rangeSize, int):
            self.rangeSize = int(self.rangeSize)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class DefinedEffectFacet(Facet):
    """
    A defined effect facet is a grouping of characteristics unique to the effect of an observable action in relation
    to one or more observable objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DefinedEffectFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:DefinedEffectFacet"
    class_name: ClassVar[str] = "DefinedEffectFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DefinedEffectFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DeviceFacet(Facet):
    """
    A device facet is a grouping of characteristics unique to a piece of equipment or a mechanism designed to serve a
    special purpose or perform a special function. [based on https://www.merriam-webster.com/dictionary/device]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DeviceFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:DeviceFacet"
    class_name: ClassVar[str] = "DeviceFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DeviceFacet

    deviceType: Optional[str] = None
    manufacturer: Optional[Union[str, IdentityId]] = None
    model: Optional[str] = None
    observable_cpeid: Optional[str] = None
    serialNumber: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.deviceType is not None and not isinstance(self.deviceType, str):
            self.deviceType = str(self.deviceType)

        if self.manufacturer is not None and not isinstance(self.manufacturer, IdentityId):
            self.manufacturer = IdentityId(self.manufacturer)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        if self.observable_cpeid is not None and not isinstance(self.observable_cpeid, str):
            self.observable_cpeid = str(self.observable_cpeid)

        if self.serialNumber is not None and not isinstance(self.serialNumber, str):
            self.serialNumber = str(self.serialNumber)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DigitalAccountFacet(Facet):
    """
    A digital account facet is a grouping of characteristics unique to an arrangement with an entity to enable and
    control the provision of some capability or service within the digital domain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DigitalAccountFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:DigitalAccountFacet"
    class_name: ClassVar[str] = "DigitalAccountFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DigitalAccountFacet

    accountLogin: Optional[Union[str, list[str]]] = empty_list()
    displayName: Optional[str] = None
    firstLoginTime: Optional[Union[str, XSDDateTime]] = None
    isDisabled: Optional[Union[bool, Bool]] = None
    lastLoginTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.accountLogin, list):
            self.accountLogin = [self.accountLogin] if self.accountLogin is not None else []
        self.accountLogin = [v if isinstance(v, str) else str(v) for v in self.accountLogin]

        if self.displayName is not None and not isinstance(self.displayName, str):
            self.displayName = str(self.displayName)

        if self.firstLoginTime is not None and not isinstance(self.firstLoginTime, XSDDateTime):
            self.firstLoginTime = XSDDateTime(self.firstLoginTime)

        if self.isDisabled is not None and not isinstance(self.isDisabled, Bool):
            self.isDisabled = Bool(self.isDisabled)

        if self.lastLoginTime is not None and not isinstance(self.lastLoginTime, XSDDateTime):
            self.lastLoginTime = XSDDateTime(self.lastLoginTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DigitalAddressFacet(Facet):
    """
    A digital address facet is a grouping of characteristics unique to an identifier assigned to enable routing and
    management of digital communication.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DigitalAddressFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:DigitalAddressFacet"
    class_name: ClassVar[str] = "DigitalAddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DigitalAddressFacet

    addressValue: Optional[str] = None
    displayName: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.addressValue is not None and not isinstance(self.addressValue, str):
            self.addressValue = str(self.addressValue)

        if self.displayName is not None and not isinstance(self.displayName, str):
            self.displayName = str(self.displayName)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DigitalSignatureInfoFacet(Facet):
    """
    A digital signature info facet is a grouping of characteristics unique to a value calculated via a mathematical
    scheme for demonstrating the authenticity of an electronic message or document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DigitalSignatureInfoFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:DigitalSignatureInfoFacet"
    class_name: ClassVar[str] = "DigitalSignatureInfoFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DigitalSignatureInfoFacet

    certificateIssuer: Optional[Union[str, IdentityId]] = None
    certificateSubject: Optional[Union[str, UcoObjectId]] = None
    signatureDescription: Optional[str] = None
    signatureExists: Optional[Union[bool, Bool]] = None
    signatureVerified: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.certificateIssuer is not None and not isinstance(self.certificateIssuer, IdentityId):
            self.certificateIssuer = IdentityId(self.certificateIssuer)

        if self.certificateSubject is not None and not isinstance(self.certificateSubject, UcoObjectId):
            self.certificateSubject = UcoObjectId(self.certificateSubject)

        if self.signatureDescription is not None and not isinstance(self.signatureDescription, str):
            self.signatureDescription = str(self.signatureDescription)

        if self.signatureExists is not None and not isinstance(self.signatureExists, Bool):
            self.signatureExists = Bool(self.signatureExists)

        if self.signatureVerified is not None and not isinstance(self.signatureVerified, Bool):
            self.signatureVerified = Bool(self.signatureVerified)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DiskFacet(Facet):
    """
    A disk facet is a grouping of characteristics unique to a storage mechanism where data is recorded by various
    electronic, magnetic, optical, or mechanical changes to a surface layer of one or more rotating disks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DiskFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:DiskFacet"
    class_name: ClassVar[str] = "DiskFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DiskFacet

    diskSize: Optional[int] = None
    diskType: Optional[str] = None
    freeSpace: Optional[int] = None
    partition: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.diskSize is not None and not isinstance(self.diskSize, int):
            self.diskSize = int(self.diskSize)

        if self.diskType is not None and not isinstance(self.diskType, str):
            self.diskType = str(self.diskType)

        if self.freeSpace is not None and not isinstance(self.freeSpace, int):
            self.freeSpace = int(self.freeSpace)

        if not isinstance(self.partition, list):
            self.partition = [self.partition] if self.partition is not None else []
        self.partition = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.partition]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DiskPartitionFacet(Facet):
    """
    A disk partition facet is a grouping of characteristics unique to a particular managed region on a storage
    mechanism.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DiskPartitionFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:DiskPartitionFacet"
    class_name: ClassVar[str] = "DiskPartitionFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DiskPartitionFacet

    diskPartitionType: Optional[str] = None
    mountPoint: Optional[str] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    partitionID: Optional[str] = None
    partitionLength: Optional[int] = None
    partitionOffset: Optional[int] = None
    spaceLeft: Optional[int] = None
    spaceUsed: Optional[int] = None
    totalSpace: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.diskPartitionType is not None and not isinstance(self.diskPartitionType, str):
            self.diskPartitionType = str(self.diskPartitionType)

        if self.mountPoint is not None and not isinstance(self.mountPoint, str):
            self.mountPoint = str(self.mountPoint)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.partitionID is not None and not isinstance(self.partitionID, str):
            self.partitionID = str(self.partitionID)

        if self.partitionLength is not None and not isinstance(self.partitionLength, int):
            self.partitionLength = int(self.partitionLength)

        if self.partitionOffset is not None and not isinstance(self.partitionOffset, int):
            self.partitionOffset = int(self.partitionOffset)

        if self.spaceLeft is not None and not isinstance(self.spaceLeft, int):
            self.spaceLeft = int(self.spaceLeft)

        if self.spaceUsed is not None and not isinstance(self.spaceUsed, int):
            self.spaceUsed = int(self.spaceUsed)

        if self.totalSpace is not None and not isinstance(self.totalSpace, int):
            self.totalSpace = int(self.totalSpace)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DomainNameFacet(Facet):
    """
    A domain name facet is a grouping of characteristics unique to an identification string that defines a realm of
    administrative autonomy, authority or control within the Internet. [based on
    https://en.wikipedia.org/wiki/Domain_name]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DomainNameFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:DomainNameFacet"
    class_name: ClassVar[str] = "DomainNameFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DomainNameFacet

    isTLD: Optional[Union[bool, Bool]] = None
    observable_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.isTLD is not None and not isinstance(self.isTLD, Bool):
            self.isTLD = Bool(self.isTLD)

        if self.observable_value is not None and not isinstance(self.observable_value, str):
            self.observable_value = str(self.observable_value)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EXIFFacet(Facet):
    """
    An EXIF (exchangeable image file format) facet is a grouping of characteristics unique to the formats for images,
    sound, and ancillary tags used by digital cameras (including smartphones), scanners and other systems handling
    image and sound files recorded by digital cameras conformant to JEIDA/JEITA/CIPA specifications. [based on
    https://en.wikipedia.org/wiki/Exif]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EXIFFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:EXIFFacet"
    class_name: ClassVar[str] = "EXIFFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EXIFFacet

    exifData: Optional[Union[Union[dict, ControlledDictionary], list[Union[dict, ControlledDictionary]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.exifData, list):
            self.exifData = [self.exifData] if self.exifData is not None else []
        self.exifData = [v if isinstance(v, ControlledDictionary) else ControlledDictionary(**as_dict(v)) for v in self.exifData]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EmailAccountFacet(Facet):
    """
    An email account facet is a grouping of characteristics unique to an arrangement with an entity to enable and
    control the provision of electronic mail (email) capabilities or services.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EmailAccountFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:EmailAccountFacet"
    class_name: ClassVar[str] = "EmailAccountFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EmailAccountFacet

    emailAddress: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.emailAddress is not None and not isinstance(self.emailAddress, ObservableObjectId):
            self.emailAddress = ObservableObjectId(self.emailAddress)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class EmailAddressFacet(DigitalAddressFacet):
    """
    An email address facet is a grouping of characteristics unique to an identifier for an electronic mailbox to which
    electronic mail messages (conformant to the Simple Mail Transfer Protocol (SMTP)) are sent from and delivered to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EmailAddressFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:EmailAddressFacet"
    class_name: ClassVar[str] = "EmailAddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EmailAddressFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EmailMessageFacet(Facet):
    """
    An email message facet is a grouping of characteristics unique to a message that is an instance of an electronic
    mail correspondence conformant to the internet message format described in RFC 5322 and related RFCs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EmailMessageFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:EmailMessageFacet"
    class_name: ClassVar[str] = "EmailMessageFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EmailMessageFacet

    application: Optional[Union[str, ObservableObjectId]] = None
    bcc: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    body: Optional[str] = None
    bodyMultipart: Optional[Union[Union[dict, "MimePartType"], list[Union[dict, "MimePartType"]]]] = empty_list()
    bodyRaw: Optional[Union[str, ObservableObjectId]] = None
    categories: Optional[Union[str, list[str]]] = empty_list()
    cc: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    contentDisposition: Optional[str] = None
    contentType: Optional[str] = None
    from_: Optional[Union[str, ObservableObjectId]] = None
    headerRaw: Optional[Union[str, ObservableObjectId]] = None
    inReplyTo: Optional[str] = None
    isMimeEncoded: Optional[Union[bool, Bool]] = None
    isMultipart: Optional[Union[bool, Bool]] = None
    isRead: Optional[Union[bool, Bool]] = None
    labels: Optional[Union[str, list[str]]] = empty_list()
    messageID: Optional[str] = None
    observable_modifiedTime: Optional[Union[str, XSDDateTime]] = None
    observable_references: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    otherHeaders: Optional[Union[dict, Dictionary]] = None
    priority: Optional[str] = None
    receivedLines: Optional[Union[str, list[str]]] = empty_list()
    receivedTime: Optional[Union[str, XSDDateTime]] = None
    sender: Optional[Union[str, ObservableObjectId]] = None
    sentTime: Optional[Union[str, XSDDateTime]] = None
    subject: Optional[str] = None
    to: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    xMailer: Optional[str] = None
    xOriginatingIP: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if not isinstance(self.bcc, list):
            self.bcc = [self.bcc] if self.bcc is not None else []
        self.bcc = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.bcc]

        if self.body is not None and not isinstance(self.body, str):
            self.body = str(self.body)

        if not isinstance(self.bodyMultipart, list):
            self.bodyMultipart = [self.bodyMultipart] if self.bodyMultipart is not None else []
        self.bodyMultipart = [v if isinstance(v, MimePartType) else MimePartType(**as_dict(v)) for v in self.bodyMultipart]

        if self.bodyRaw is not None and not isinstance(self.bodyRaw, ObservableObjectId):
            self.bodyRaw = ObservableObjectId(self.bodyRaw)

        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, str) else str(v) for v in self.categories]

        if not isinstance(self.cc, list):
            self.cc = [self.cc] if self.cc is not None else []
        self.cc = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.cc]

        if self.contentDisposition is not None and not isinstance(self.contentDisposition, str):
            self.contentDisposition = str(self.contentDisposition)

        if self.contentType is not None and not isinstance(self.contentType, str):
            self.contentType = str(self.contentType)

        if self.from_ is not None and not isinstance(self.from_, ObservableObjectId):
            self.from_ = ObservableObjectId(self.from_)

        if self.headerRaw is not None and not isinstance(self.headerRaw, ObservableObjectId):
            self.headerRaw = ObservableObjectId(self.headerRaw)

        if self.inReplyTo is not None and not isinstance(self.inReplyTo, str):
            self.inReplyTo = str(self.inReplyTo)

        if self.isMimeEncoded is not None and not isinstance(self.isMimeEncoded, Bool):
            self.isMimeEncoded = Bool(self.isMimeEncoded)

        if self.isMultipart is not None and not isinstance(self.isMultipart, Bool):
            self.isMultipart = Bool(self.isMultipart)

        if self.isRead is not None and not isinstance(self.isRead, Bool):
            self.isRead = Bool(self.isRead)

        if not isinstance(self.labels, list):
            self.labels = [self.labels] if self.labels is not None else []
        self.labels = [v if isinstance(v, str) else str(v) for v in self.labels]

        if self.messageID is not None and not isinstance(self.messageID, str):
            self.messageID = str(self.messageID)

        if self.observable_modifiedTime is not None and not isinstance(self.observable_modifiedTime, XSDDateTime):
            self.observable_modifiedTime = XSDDateTime(self.observable_modifiedTime)

        if not isinstance(self.observable_references, list):
            self.observable_references = [self.observable_references] if self.observable_references is not None else []
        self.observable_references = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.observable_references]

        if self.otherHeaders is not None and not isinstance(self.otherHeaders, Dictionary):
            self.otherHeaders = Dictionary(**as_dict(self.otherHeaders))

        if self.priority is not None and not isinstance(self.priority, str):
            self.priority = str(self.priority)

        if not isinstance(self.receivedLines, list):
            self.receivedLines = [self.receivedLines] if self.receivedLines is not None else []
        self.receivedLines = [v if isinstance(v, str) else str(v) for v in self.receivedLines]

        if self.receivedTime is not None and not isinstance(self.receivedTime, XSDDateTime):
            self.receivedTime = XSDDateTime(self.receivedTime)

        if self.sender is not None and not isinstance(self.sender, ObservableObjectId):
            self.sender = ObservableObjectId(self.sender)

        if self.sentTime is not None and not isinstance(self.sentTime, XSDDateTime):
            self.sentTime = XSDDateTime(self.sentTime)

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if not isinstance(self.to, list):
            self.to = [self.to] if self.to is not None else []
        self.to = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.to]

        if self.xMailer is not None and not isinstance(self.xMailer, str):
            self.xMailer = str(self.xMailer)

        if self.xOriginatingIP is not None and not isinstance(self.xOriginatingIP, ObservableObjectId):
            self.xOriginatingIP = ObservableObjectId(self.xOriginatingIP)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EncodedStreamFacet(Facet):
    """
    An encoded stream facet is a grouping of characteristics unique to the conversion of a body of data content from
    one form to another form.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EncodedStreamFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:EncodedStreamFacet"
    class_name: ClassVar[str] = "EncodedStreamFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EncodedStreamFacet

    encodingMethod: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.encodingMethod is not None and not isinstance(self.encodingMethod, str):
            self.encodingMethod = str(self.encodingMethod)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EncryptedStreamFacet(Facet):
    """
    An encrypted stream facet is a grouping of characteristics unique to the conversion of a body of data content from
    one form to another obfuscated form in such a way that reversing the conversion to obtain the original data form
    can only be accomplished through possession and use of a specific key.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EncryptedStreamFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:EncryptedStreamFacet"
    class_name: ClassVar[str] = "EncryptedStreamFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EncryptedStreamFacet

    encryptionIV: Optional[Union[str, list[str]]] = empty_list()
    encryptionKey: Optional[Union[str, list[str]]] = empty_list()
    encryptionMethod: Optional[str] = None
    encryptionMode: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.encryptionIV, list):
            self.encryptionIV = [self.encryptionIV] if self.encryptionIV is not None else []
        self.encryptionIV = [v if isinstance(v, str) else str(v) for v in self.encryptionIV]

        if not isinstance(self.encryptionKey, list):
            self.encryptionKey = [self.encryptionKey] if self.encryptionKey is not None else []
        self.encryptionKey = [v if isinstance(v, str) else str(v) for v in self.encryptionKey]

        if self.encryptionMethod is not None and not isinstance(self.encryptionMethod, str):
            self.encryptionMethod = str(self.encryptionMethod)

        if self.encryptionMode is not None and not isinstance(self.encryptionMode, str):
            self.encryptionMode = str(self.encryptionMode)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EnvironmentVariable(UcoInherentCharacterizationThing):
    """
    An environment variable is a grouping of characteristics unique to a dynamic-named value that can affect the way
    running processes will behave on a computer. [based on https://en.wikipedia.org/wiki/Environment_variable]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EnvironmentVariable"]
    class_class_curie: ClassVar[str] = "uco-observable:EnvironmentVariable"
    class_name: ClassVar[str] = "EnvironmentVariable"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EnvironmentVariable

    name: Optional[str] = None
    observable_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.observable_value is not None and not isinstance(self.observable_value, str):
            self.observable_value = str(self.observable_value)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EventRecordFacet(Facet):
    """
    An event record facet is a grouping of characteristics unique to something that happens in a digital context
    (e.g., operating system events).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EventRecordFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:EventRecordFacet"
    class_name: ClassVar[str] = "EventRecordFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EventRecordFacet

    account: Optional[Union[str, ObservableObjectId]] = None
    application: Optional[Union[str, ObservableObjectId]] = None
    cyberAction: Optional[Union[str, ObservableActionId]] = None
    eventID: Optional[str] = None
    eventRecordDevice: Optional[Union[str, ObservableObjectId]] = None
    eventRecordID: Optional[str] = None
    eventRecordRaw: Optional[str] = None
    eventRecordServiceName: Optional[str] = None
    eventRecordText: Optional[str] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    observable_endTime: Optional[Union[str, XSDDateTime]] = None
    observable_eventType: Optional[str] = None
    observable_startTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.account is not None and not isinstance(self.account, ObservableObjectId):
            self.account = ObservableObjectId(self.account)

        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if self.cyberAction is not None and not isinstance(self.cyberAction, ObservableActionId):
            self.cyberAction = ObservableActionId(self.cyberAction)

        if self.eventID is not None and not isinstance(self.eventID, str):
            self.eventID = str(self.eventID)

        if self.eventRecordDevice is not None and not isinstance(self.eventRecordDevice, ObservableObjectId):
            self.eventRecordDevice = ObservableObjectId(self.eventRecordDevice)

        if self.eventRecordID is not None and not isinstance(self.eventRecordID, str):
            self.eventRecordID = str(self.eventRecordID)

        if self.eventRecordRaw is not None and not isinstance(self.eventRecordRaw, str):
            self.eventRecordRaw = str(self.eventRecordRaw)

        if self.eventRecordServiceName is not None and not isinstance(self.eventRecordServiceName, str):
            self.eventRecordServiceName = str(self.eventRecordServiceName)

        if self.eventRecordText is not None and not isinstance(self.eventRecordText, str):
            self.eventRecordText = str(self.eventRecordText)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.observable_endTime is not None and not isinstance(self.observable_endTime, XSDDateTime):
            self.observable_endTime = XSDDateTime(self.observable_endTime)

        if self.observable_eventType is not None and not isinstance(self.observable_eventType, str):
            self.observable_eventType = str(self.observable_eventType)

        if self.observable_startTime is not None and not isinstance(self.observable_startTime, XSDDateTime):
            self.observable_startTime = XSDDateTime(self.observable_startTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ExtInodeFacet(Facet):
    """
    An extInode facet is a grouping of characteristics unique to a file system object (file, directory, etc.)
    conformant to the extended file system (EXT or related derivations) specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ExtInodeFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ExtInodeFacet"
    class_name: ClassVar[str] = "ExtInodeFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ExtInodeFacet

    extDeletionTime: Optional[Union[str, XSDDateTime]] = None
    extFileType: Optional[int] = None
    extFlags: Optional[int] = None
    extHardLinkCount: Optional[int] = None
    extInodeChangeTime: Optional[Union[str, XSDDateTime]] = None
    extInodeID: Optional[int] = None
    extPermissions: Optional[int] = None
    extSGID: Optional[int] = None
    extSUID: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.extDeletionTime is not None and not isinstance(self.extDeletionTime, XSDDateTime):
            self.extDeletionTime = XSDDateTime(self.extDeletionTime)

        if self.extFileType is not None and not isinstance(self.extFileType, int):
            self.extFileType = int(self.extFileType)

        if self.extFlags is not None and not isinstance(self.extFlags, int):
            self.extFlags = int(self.extFlags)

        if self.extHardLinkCount is not None and not isinstance(self.extHardLinkCount, int):
            self.extHardLinkCount = int(self.extHardLinkCount)

        if self.extInodeChangeTime is not None and not isinstance(self.extInodeChangeTime, XSDDateTime):
            self.extInodeChangeTime = XSDDateTime(self.extInodeChangeTime)

        if self.extInodeID is not None and not isinstance(self.extInodeID, int):
            self.extInodeID = int(self.extInodeID)

        if self.extPermissions is not None and not isinstance(self.extPermissions, int):
            self.extPermissions = int(self.extPermissions)

        if self.extSGID is not None and not isinstance(self.extSGID, int):
            self.extSGID = int(self.extSGID)

        if self.extSUID is not None and not isinstance(self.extSUID, int):
            self.extSUID = int(self.extSUID)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ExtractedString(UcoInherentCharacterizationThing):
    """
    An extracted string is a grouping of characteristics unique to a series of characters pulled from an observable
    object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ExtractedString"]
    class_class_curie: ClassVar[str] = "uco-observable:ExtractedString"
    class_name: ClassVar[str] = "ExtractedString"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ExtractedString

    byteStringValue: Optional[Union[str, UcoBase64Binary]] = None
    encoding: Optional[str] = None
    englishTranslation: Optional[str] = None
    language: Optional[str] = None
    length: Optional[int] = None
    stringValue: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.byteStringValue is not None and not isinstance(self.byteStringValue, UcoBase64Binary):
            self.byteStringValue = UcoBase64Binary(self.byteStringValue)

        if self.encoding is not None and not isinstance(self.encoding, str):
            self.encoding = str(self.encoding)

        if self.englishTranslation is not None and not isinstance(self.englishTranslation, str):
            self.englishTranslation = str(self.englishTranslation)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.length is not None and not isinstance(self.length, int):
            self.length = int(self.length)

        if self.stringValue is not None and not isinstance(self.stringValue, str):
            self.stringValue = str(self.stringValue)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ExtractedStringsFacet(Facet):
    """
    An extracted strings facet is a grouping of characteristics unique to one or more sequences of characters pulled
    from an observable object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ExtractedStringsFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ExtractedStringsFacet"
    class_name: ClassVar[str] = "ExtractedStringsFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ExtractedStringsFacet

    strings: Optional[Union[Union[dict, ExtractedString], list[Union[dict, ExtractedString]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.strings, list):
            self.strings = [self.strings] if self.strings is not None else []
        self.strings = [v if isinstance(v, ExtractedString) else ExtractedString(**as_dict(v)) for v in self.strings]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class FileFacet(Facet):
    """
    A file facet is a grouping of characteristics unique to the storage of a file (computer resource for recording
    data discretely in a computer storage device) on a file system (process that manages how and where data on a
    storage device is stored, accessed and managed). [based on https://en.wikipedia.org/Computer_file and
    https://www.techopedia.com/definition/5510/file-system]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["FileFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:FileFacet"
    class_name: ClassVar[str] = "FileFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.FileFacet

    accessedTime: Optional[Union[str, XSDDateTime]] = None
    allocationStatus: Optional[str] = None
    extension: Optional[str] = None
    fileName: Optional[Union[str, list[str]]] = empty_list()
    filePath: Optional[Union[str, list[str]]] = empty_list()
    isDirectory: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    metadataChangeTime: Optional[Union[str, XSDDateTime]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    observable_modifiedTime: Optional[Union[str, XSDDateTime]] = None
    sizeInBytes: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.accessedTime is not None and not isinstance(self.accessedTime, XSDDateTime):
            self.accessedTime = XSDDateTime(self.accessedTime)

        if self.allocationStatus is not None and not isinstance(self.allocationStatus, str):
            self.allocationStatus = str(self.allocationStatus)

        if self.extension is not None and not isinstance(self.extension, str):
            self.extension = str(self.extension)

        if not isinstance(self.fileName, list):
            self.fileName = [self.fileName] if self.fileName is not None else []
        self.fileName = [v if isinstance(v, str) else str(v) for v in self.fileName]

        if not isinstance(self.filePath, list):
            self.filePath = [self.filePath] if self.filePath is not None else []
        self.filePath = [v if isinstance(v, str) else str(v) for v in self.filePath]

        if not isinstance(self.isDirectory, list):
            self.isDirectory = [self.isDirectory] if self.isDirectory is not None else []
        self.isDirectory = [v if isinstance(v, Bool) else Bool(v) for v in self.isDirectory]

        if self.metadataChangeTime is not None and not isinstance(self.metadataChangeTime, XSDDateTime):
            self.metadataChangeTime = XSDDateTime(self.metadataChangeTime)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.observable_modifiedTime is not None and not isinstance(self.observable_modifiedTime, XSDDateTime):
            self.observable_modifiedTime = XSDDateTime(self.observable_modifiedTime)

        if self.sizeInBytes is not None and not isinstance(self.sizeInBytes, int):
            self.sizeInBytes = int(self.sizeInBytes)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class FilePermissionsFacet(Facet):
    """
    A file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change,
    navigate, execute) of a file on a file system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["FilePermissionsFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:FilePermissionsFacet"
    class_name: ClassVar[str] = "FilePermissionsFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.FilePermissionsFacet

    owner: Optional[Union[str, UcoObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.owner is not None and not isinstance(self.owner, UcoObjectId):
            self.owner = UcoObjectId(self.owner)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class FileSystemFacet(Facet):
    """
    A file system facet is a grouping of characteristics unique to the process that manages how and where data on a
    storage medium is stored, accessed and managed. [based on https://www.techopedia.com/definition/5510/file-system]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["FileSystemFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:FileSystemFacet"
    class_name: ClassVar[str] = "FileSystemFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.FileSystemFacet

    clusterSize: Optional[int] = None
    fileSystemType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.clusterSize is not None and not isinstance(self.clusterSize, int):
            self.clusterSize = int(self.clusterSize)

        if self.fileSystemType is not None and not isinstance(self.fileSystemType, str):
            self.fileSystemType = str(self.fileSystemType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class FragmentFacet(Facet):
    """
    A fragment facet is a grouping of characteristics unique to an individual piece of the content of a file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["FragmentFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:FragmentFacet"
    class_name: ClassVar[str] = "FragmentFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.FragmentFacet

    fragmentIndex: Optional[Union[int, list[int]]] = empty_list()
    totalFragments: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.fragmentIndex, list):
            self.fragmentIndex = [self.fragmentIndex] if self.fragmentIndex is not None else []
        self.fragmentIndex = [v if isinstance(v, int) else int(v) for v in self.fragmentIndex]

        if not isinstance(self.totalFragments, list):
            self.totalFragments = [self.totalFragments] if self.totalFragments is not None else []
        self.totalFragments = [v if isinstance(v, int) else int(v) for v in self.totalFragments]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GeoLocationEntryFacet(Facet):
    """
    A geolocation entry facet is a grouping of characteristics unique to a single application-specific geolocation
    entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["GeoLocationEntryFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:GeoLocationEntryFacet"
    class_name: ClassVar[str] = "GeoLocationEntryFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GeoLocationEntryFacet

    application: Optional[Union[str, ObservableObjectId]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    observable_location: Optional[Union[str, LocationId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.observable_location is not None and not isinstance(self.observable_location, LocationId):
            self.observable_location = LocationId(self.observable_location)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GeoLocationLogFacet(Facet):
    """
    A geolocation log facet is a grouping of characteristics unique to a record containing geolocation tracks and/or
    geolocation entries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["GeoLocationLogFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:GeoLocationLogFacet"
    class_name: ClassVar[str] = "GeoLocationLogFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GeoLocationLogFacet

    application: Optional[Union[str, ObservableObjectId]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GeoLocationTrackFacet(Facet):
    """
    A geolocation track facet is a grouping of characteristics unique to a set of contiguous geolocation entries
    representing a path/track taken.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["GeoLocationTrackFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:GeoLocationTrackFacet"
    class_name: ClassVar[str] = "GeoLocationTrackFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GeoLocationTrackFacet

    application: Optional[Union[str, ObservableObjectId]] = None
    geoLocationEntry: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    observable_endTime: Optional[Union[str, XSDDateTime]] = None
    observable_startTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if not isinstance(self.geoLocationEntry, list):
            self.geoLocationEntry = [self.geoLocationEntry] if self.geoLocationEntry is not None else []
        self.geoLocationEntry = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.geoLocationEntry]

        if self.observable_endTime is not None and not isinstance(self.observable_endTime, XSDDateTime):
            self.observable_endTime = XSDDateTime(self.observable_endTime)

        if self.observable_startTime is not None and not isinstance(self.observable_startTime, XSDDateTime):
            self.observable_startTime = XSDDateTime(self.observable_startTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GlobalFlagType(UcoInherentCharacterizationThing):
    """
    A global flag type is a grouping of characteristics unique to the Windows systemwide global variable named
    NtGlobalFlag that enables various internal debugging, tracing, and validation support in the operating system.
    [based on "Windows Global Flags, Chapter 3: System Mechanisms of Windows Internals by Solomon, Russinovich, and
    Ionescu]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["GlobalFlagType"]
    class_class_curie: ClassVar[str] = "uco-observable:GlobalFlagType"
    class_name: ClassVar[str] = "GlobalFlagType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GlobalFlagType

    abbreviation: Optional[str] = None
    destination: Optional[str] = None
    hexadecimalValue: Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]] = empty_list()
    symbolicName: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if self.destination is not None and not isinstance(self.destination, str):
            self.destination = str(self.destination)

        if not isinstance(self.hexadecimalValue, list):
            self.hexadecimalValue = [self.hexadecimalValue] if self.hexadecimalValue is not None else []
        self.hexadecimalValue = [v if isinstance(v, UcoHexBinary) else UcoHexBinary(v) for v in self.hexadecimalValue]

        if self.symbolicName is not None and not isinstance(self.symbolicName, str):
            self.symbolicName = str(self.symbolicName)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class HTTPConnectionFacet(Facet):
    """
    An HTTP connection facet is a grouping of characteristics unique to portions of a network connection that are
    conformant to the Hypertext Transfer Protocol (HTTP) standard.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["HTTPConnectionFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:HTTPConnectionFacet"
    class_name: ClassVar[str] = "HTTPConnectionFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.HTTPConnectionFacet

    httpMesageBodyLength: Optional[int] = None
    httpMessageBodyData: Optional[Union[str, ObservableObjectId]] = None
    httpRequestHeader: Optional[Union[dict, Dictionary]] = None
    requestMethod: Optional[str] = None
    requestValue: Optional[str] = None
    requestVersion: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.httpMesageBodyLength is not None and not isinstance(self.httpMesageBodyLength, int):
            self.httpMesageBodyLength = int(self.httpMesageBodyLength)

        if self.httpMessageBodyData is not None and not isinstance(self.httpMessageBodyData, ObservableObjectId):
            self.httpMessageBodyData = ObservableObjectId(self.httpMessageBodyData)

        if self.httpRequestHeader is not None and not isinstance(self.httpRequestHeader, Dictionary):
            self.httpRequestHeader = Dictionary(**as_dict(self.httpRequestHeader))

        if self.requestMethod is not None and not isinstance(self.requestMethod, str):
            self.requestMethod = str(self.requestMethod)

        if self.requestValue is not None and not isinstance(self.requestValue, str):
            self.requestValue = str(self.requestValue)

        if self.requestVersion is not None and not isinstance(self.requestVersion, str):
            self.requestVersion = str(self.requestVersion)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ICMPConnectionFacet(Facet):
    """
    An ICMP connection facet is a grouping of characteristics unique to portions of a network connection that are
    conformant to the Internet Control Message Protocol (ICMP) standard.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ICMPConnectionFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ICMPConnectionFacet"
    class_name: ClassVar[str] = "ICMPConnectionFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ICMPConnectionFacet

    icmpCode: Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]] = empty_list()
    icmpType: Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.icmpCode, list):
            self.icmpCode = [self.icmpCode] if self.icmpCode is not None else []
        self.icmpCode = [v if isinstance(v, UcoHexBinary) else UcoHexBinary(v) for v in self.icmpCode]

        if not isinstance(self.icmpType, list):
            self.icmpType = [self.icmpType] if self.icmpType is not None else []
        self.icmpType = [v if isinstance(v, UcoHexBinary) else UcoHexBinary(v) for v in self.icmpType]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class IComHandlerActionType(UcoInherentCharacterizationThing):
    """
    An IComHandler action type is a grouping of characteristics unique to a Windows Task-related action that fires a
    Windows COM handler (smart code in the client address space that can optimize calls between a client and server).
    [based on https://docs.microsoft.com/en-us/windows/win32/taskschd/comhandleraction]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["IComHandlerActionType"]
    class_class_curie: ClassVar[str] = "uco-observable:IComHandlerActionType"
    class_name: ClassVar[str] = "IComHandlerActionType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IComHandlerActionType

    comClassID: Optional[str] = None
    comData: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.comClassID is not None and not isinstance(self.comClassID, str):
            self.comClassID = str(self.comClassID)

        if self.comData is not None and not isinstance(self.comData, str):
            self.comData = str(self.comData)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class IExecActionType(UcoInherentCharacterizationThing):
    """
    An IExec action type is a grouping of characteristics unique to an action that executes a command-line operation
    on a Windows operating system. [based on
    https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-iexecaction?redirectedfrom=MSDN]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["IExecActionType"]
    class_class_curie: ClassVar[str] = "uco-observable:IExecActionType"
    class_name: ClassVar[str] = "IExecActionType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IExecActionType

    execArguments: Optional[str] = None
    execProgramHashes: Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]] = empty_list()
    execProgramPath: Optional[str] = None
    execWorkingDirectory: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.execArguments is not None and not isinstance(self.execArguments, str):
            self.execArguments = str(self.execArguments)

        self._normalize_inlined_as_list(slot_name="execProgramHashes", slot_type=Hash, key_name="hashMethod", keyed=False)

        if self.execProgramPath is not None and not isinstance(self.execProgramPath, str):
            self.execProgramPath = str(self.execProgramPath)

        if self.execWorkingDirectory is not None and not isinstance(self.execWorkingDirectory, str):
            self.execWorkingDirectory = str(self.execWorkingDirectory)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class IPAddressFacet(DigitalAddressFacet):
    """
    An IP address facet is a grouping of characteristics unique to an Internet Protocol (IP) standards conformant
    identifier assigned to a device to enable routing and management of IP standards conformant communication to or
    from that device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["IPAddressFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:IPAddressFacet"
    class_name: ClassVar[str] = "IPAddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IPAddressFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class IPv4AddressFacet(IPAddressFacet):
    """
    An IPv4 (Internet Protocol version 4) address facet is a grouping of characteristics unique to an IPv4 standards
    conformant identifier assigned to a device to enable routing and management of IPv4 standards conformant
    communication to or from that device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["IPv4AddressFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:IPv4AddressFacet"
    class_name: ClassVar[str] = "IPv4AddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IPv4AddressFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class IPv6AddressFacet(IPAddressFacet):
    """
    An IPv6 (Internet Protocol version 6) address facet is a grouping of characteristics unique to an IPv6 standards
    conformant identifier assigned to a device to enable routing and management of IPv6 standards conformant
    communication to or from that device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["IPv6AddressFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:IPv6AddressFacet"
    class_name: ClassVar[str] = "IPv6AddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IPv6AddressFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class IShowMessageActionType(UcoInherentCharacterizationThing):
    """
    An IShow message action type is a grouping of characteristics unique to an action that shows a message box when a
    task is activate. [based on
    https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-ishowmessageaction?redirectedfrom=MSDN]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["IShowMessageActionType"]
    class_class_curie: ClassVar[str] = "uco-observable:IShowMessageActionType"
    class_name: ClassVar[str] = "IShowMessageActionType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IShowMessageActionType

    showMessageBody: Optional[str] = None
    showMessageTitle: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.showMessageBody is not None and not isinstance(self.showMessageBody, str):
            self.showMessageBody = str(self.showMessageBody)

        if self.showMessageTitle is not None and not isinstance(self.showMessageTitle, str):
            self.showMessageTitle = str(self.showMessageTitle)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ImageFacet(Facet):
    """
    An image facet is a grouping of characteristics unique to a complete copy of a hard disk, memory, or other digital
    media.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ImageFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ImageFacet"
    class_name: ClassVar[str] = "ImageFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ImageFacet

    imageType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.imageType is not None and not isinstance(self.imageType, str):
            self.imageType = str(self.imageType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class InstantMessagingAddressFacet(DigitalAddressFacet):
    """
    An instant messaging address facet is a grouping of characteristics unique to an identifier assigned to enable
    routing and management of instant messaging digital communication.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["InstantMessagingAddressFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:InstantMessagingAddressFacet"
    class_name: ClassVar[str] = "InstantMessagingAddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.InstantMessagingAddressFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class LibraryFacet(Facet):
    """
    A library facet is a grouping of characteristics unique to a suite of data and programming code that is used to
    develop software programs and applications. [based on https://www.techopedia.com/definition/3828/software-library]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["LibraryFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:LibraryFacet"
    class_name: ClassVar[str] = "LibraryFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.LibraryFacet

    libraryType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.libraryType is not None and not isinstance(self.libraryType, str):
            self.libraryType = str(self.libraryType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class MACAddressFacet(DigitalAddressFacet):
    """
    A MAC address facet is a grouping of characteristics unique to a media access control standards conformant
    identifier assigned to a network interface to enable routing and management of communications at the data link
    layer of a network segment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MACAddressFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:MACAddressFacet"
    class_name: ClassVar[str] = "MACAddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MACAddressFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class BluetoothAddressFacet(MACAddressFacet):
    """
    A Bluetooth address facet is a grouping of characteristics unique to a Bluetooth standard conformant identifier
    assigned to a Bluetooth device to enable routing and management of Bluetooth standards conformant communication to
    or from that device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["BluetoothAddressFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:BluetoothAddressFacet"
    class_name: ClassVar[str] = "BluetoothAddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BluetoothAddressFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MemoryFacet(Facet):
    """
    A memory facet is a grouping of characteristics unique to a particular region of temporary information storage
    (e.g., RAM (random access memory), ROM (read only memory)) on a digital device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MemoryFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:MemoryFacet"
    class_name: ClassVar[str] = "MemoryFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MemoryFacet

    blockType: Optional[Union[str, "MemoryBlockTypeVocab"]] = None
    isInjected: Optional[Union[bool, Bool]] = None
    isMapped: Optional[Union[bool, Bool]] = None
    isProtected: Optional[Union[bool, Bool]] = None
    isVolatile: Optional[Union[bool, Bool]] = None
    regionEndAddress: Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]] = empty_list()
    regionSize: Optional[int] = None
    regionStartAddress: Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.blockType is not None and not isinstance(self.blockType, (MemoryBlockTypeVocab, str)):
            value = self.blockType
            for _coerce in (lambda: MemoryBlockTypeVocab(value), lambda: str(value)):
                try:
                    self.blockType = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[MemoryBlockTypeVocab, str] could be constructed from {value!r} for slot blockType")

        if self.isInjected is not None and not isinstance(self.isInjected, Bool):
            self.isInjected = Bool(self.isInjected)

        if self.isMapped is not None and not isinstance(self.isMapped, Bool):
            self.isMapped = Bool(self.isMapped)

        if self.isProtected is not None and not isinstance(self.isProtected, Bool):
            self.isProtected = Bool(self.isProtected)

        if self.isVolatile is not None and not isinstance(self.isVolatile, Bool):
            self.isVolatile = Bool(self.isVolatile)

        if not isinstance(self.regionEndAddress, list):
            self.regionEndAddress = [self.regionEndAddress] if self.regionEndAddress is not None else []
        self.regionEndAddress = [v if isinstance(v, UcoHexBinary) else UcoHexBinary(v) for v in self.regionEndAddress]

        if self.regionSize is not None and not isinstance(self.regionSize, int):
            self.regionSize = int(self.regionSize)

        if not isinstance(self.regionStartAddress, list):
            self.regionStartAddress = [self.regionStartAddress] if self.regionStartAddress is not None else []
        self.regionStartAddress = [v if isinstance(v, UcoHexBinary) else UcoHexBinary(v) for v in self.regionStartAddress]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MessageFacet(Facet):
    """
    A message facet is a grouping of characteristics unique to a discrete unit of electronic communication intended by
    the source for consumption by some recipient or group of recipients. [based on
    https://en.wikipedia.org/wiki/Message]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MessageFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:MessageFacet"
    class_name: ClassVar[str] = "MessageFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MessageFacet

    application: Optional[Union[str, ObservableObjectId]] = None
    from_: Optional[Union[str, ObservableObjectId]] = None
    messageID: Optional[str] = None
    messageText: Optional[str] = None
    messageType: Optional[str] = None
    sentTime: Optional[Union[str, XSDDateTime]] = None
    sessionID: Optional[str] = None
    to: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if self.from_ is not None and not isinstance(self.from_, ObservableObjectId):
            self.from_ = ObservableObjectId(self.from_)

        if self.messageID is not None and not isinstance(self.messageID, str):
            self.messageID = str(self.messageID)

        if self.messageText is not None and not isinstance(self.messageText, str):
            self.messageText = str(self.messageText)

        if self.messageType is not None and not isinstance(self.messageType, str):
            self.messageType = str(self.messageType)

        if self.sentTime is not None and not isinstance(self.sentTime, XSDDateTime):
            self.sentTime = XSDDateTime(self.sentTime)

        if self.sessionID is not None and not isinstance(self.sessionID, str):
            self.sessionID = str(self.sessionID)

        if not isinstance(self.to, list):
            self.to = [self.to] if self.to is not None else []
        self.to = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.to]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MessageThreadFacet(Facet):
    """
    A message thread facet is a grouping of characteristics unique to a running commentary of electronic messages
    pertaining to one topic or question.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MessageThreadFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:MessageThreadFacet"
    class_name: ClassVar[str] = "MessageThreadFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MessageThreadFacet

    messageThread: Optional[Union[str, ThreadId]] = None
    observable_participant: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    visibility: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.messageThread is not None and not isinstance(self.messageThread, ThreadId):
            self.messageThread = ThreadId(self.messageThread)

        if not isinstance(self.observable_participant, list):
            self.observable_participant = [self.observable_participant] if self.observable_participant is not None else []
        self.observable_participant = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.observable_participant]

        if self.visibility is not None and not isinstance(self.visibility, Bool):
            self.visibility = Bool(self.visibility)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MftRecordFacet(Facet):
    """
    An MFT record facet is a grouping of characteristics unique to the details of a single file as managed in an NTFS
    (new technology filesystem) master file table (which is a collection of information about all files on an NTFS
    filesystem). [based on https://docs.microsoft.com/en-us/windows/win32/devnotes/master-file-table]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MftRecordFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:MftRecordFacet"
    class_name: ClassVar[str] = "MftRecordFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MftRecordFacet

    mftFileID: Optional[int] = None
    mftFileNameAccessedTime: Optional[Union[str, XSDDateTime]] = None
    mftFileNameCreatedTime: Optional[Union[str, XSDDateTime]] = None
    mftFileNameLength: Optional[int] = None
    mftFileNameModifiedTime: Optional[Union[str, XSDDateTime]] = None
    mftFileNameRecordChangeTime: Optional[Union[str, XSDDateTime]] = None
    mftFlags: Optional[int] = None
    mftParentID: Optional[int] = None
    mftRecordChangeTime: Optional[Union[str, XSDDateTime]] = None
    ntfsHardLinkCount: Optional[int] = None
    ntfsOwnerID: Optional[str] = None
    ntfsOwnerSID: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.mftFileID is not None and not isinstance(self.mftFileID, int):
            self.mftFileID = int(self.mftFileID)

        if self.mftFileNameAccessedTime is not None and not isinstance(self.mftFileNameAccessedTime, XSDDateTime):
            self.mftFileNameAccessedTime = XSDDateTime(self.mftFileNameAccessedTime)

        if self.mftFileNameCreatedTime is not None and not isinstance(self.mftFileNameCreatedTime, XSDDateTime):
            self.mftFileNameCreatedTime = XSDDateTime(self.mftFileNameCreatedTime)

        if self.mftFileNameLength is not None and not isinstance(self.mftFileNameLength, int):
            self.mftFileNameLength = int(self.mftFileNameLength)

        if self.mftFileNameModifiedTime is not None and not isinstance(self.mftFileNameModifiedTime, XSDDateTime):
            self.mftFileNameModifiedTime = XSDDateTime(self.mftFileNameModifiedTime)

        if self.mftFileNameRecordChangeTime is not None and not isinstance(self.mftFileNameRecordChangeTime, XSDDateTime):
            self.mftFileNameRecordChangeTime = XSDDateTime(self.mftFileNameRecordChangeTime)

        if self.mftFlags is not None and not isinstance(self.mftFlags, int):
            self.mftFlags = int(self.mftFlags)

        if self.mftParentID is not None and not isinstance(self.mftParentID, int):
            self.mftParentID = int(self.mftParentID)

        if self.mftRecordChangeTime is not None and not isinstance(self.mftRecordChangeTime, XSDDateTime):
            self.mftRecordChangeTime = XSDDateTime(self.mftRecordChangeTime)

        if self.ntfsHardLinkCount is not None and not isinstance(self.ntfsHardLinkCount, int):
            self.ntfsHardLinkCount = int(self.ntfsHardLinkCount)

        if self.ntfsOwnerID is not None and not isinstance(self.ntfsOwnerID, str):
            self.ntfsOwnerID = str(self.ntfsOwnerID)

        if self.ntfsOwnerSID is not None and not isinstance(self.ntfsOwnerSID, str):
            self.ntfsOwnerSID = str(self.ntfsOwnerSID)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MimePartType(UcoInherentCharacterizationThing):
    """
    A mime part type is a grouping of characteristics unique to a component of a multi-part email body.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MimePartType"]
    class_class_curie: ClassVar[str] = "uco-observable:MimePartType"
    class_name: ClassVar[str] = "MimePartType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MimePartType

    body: Optional[str] = None
    bodyRaw: Optional[Union[str, ObservableObjectId]] = None
    contentDisposition: Optional[str] = None
    contentType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.body is not None and not isinstance(self.body, str):
            self.body = str(self.body)

        if self.bodyRaw is not None and not isinstance(self.bodyRaw, ObservableObjectId):
            self.bodyRaw = ObservableObjectId(self.bodyRaw)

        if self.contentDisposition is not None and not isinstance(self.contentDisposition, str):
            self.contentDisposition = str(self.contentDisposition)

        if self.contentType is not None and not isinstance(self.contentType, str):
            self.contentType = str(self.contentType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MobileAccountFacet(Facet):
    """
    A mobile account facet is a grouping of characteristics unique to an arrangement with an entity to enable and
    control the provision of some capability or service on a portable computing device. [based on
    https://www.lexico.com/definition/mobile_device]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MobileAccountFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:MobileAccountFacet"
    class_name: ClassVar[str] = "MobileAccountFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MobileAccountFacet

    IMSI: Optional[str] = None
    MSISDN: Optional[str] = None
    MSISDNType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.IMSI is not None and not isinstance(self.IMSI, str):
            self.IMSI = str(self.IMSI)

        if self.MSISDN is not None and not isinstance(self.MSISDN, str):
            self.MSISDN = str(self.MSISDN)

        if self.MSISDNType is not None and not isinstance(self.MSISDNType, str):
            self.MSISDNType = str(self.MSISDNType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MobileDeviceFacet(Facet):
    """
    A mobile device facet is a grouping of characteristics unique to a portable computing device. [based on
    https://www.lexico.com/definition/mobile_device]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MobileDeviceFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:MobileDeviceFacet"
    class_name: ClassVar[str] = "MobileDeviceFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MobileDeviceFacet

    ESN: Optional[str] = None
    IMEI: Optional[Union[str, list[str]]] = empty_list()
    bluetoothDeviceName: Optional[str] = None
    clockSetting: Optional[Union[str, XSDDateTime]] = None
    keypadUnlockCode: Optional[str] = None
    mockLocationsAllowed: Optional[Union[bool, Bool]] = None
    network: Optional[str] = None
    phoneActivationTime: Optional[Union[str, XSDDateTime]] = None
    storageCapacityInBytes: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ESN is not None and not isinstance(self.ESN, str):
            self.ESN = str(self.ESN)

        if not isinstance(self.IMEI, list):
            self.IMEI = [self.IMEI] if self.IMEI is not None else []
        self.IMEI = [v if isinstance(v, str) else str(v) for v in self.IMEI]

        if self.bluetoothDeviceName is not None and not isinstance(self.bluetoothDeviceName, str):
            self.bluetoothDeviceName = str(self.bluetoothDeviceName)

        if self.clockSetting is not None and not isinstance(self.clockSetting, XSDDateTime):
            self.clockSetting = XSDDateTime(self.clockSetting)

        if self.keypadUnlockCode is not None and not isinstance(self.keypadUnlockCode, str):
            self.keypadUnlockCode = str(self.keypadUnlockCode)

        if self.mockLocationsAllowed is not None and not isinstance(self.mockLocationsAllowed, Bool):
            self.mockLocationsAllowed = Bool(self.mockLocationsAllowed)

        if self.network is not None and not isinstance(self.network, str):
            self.network = str(self.network)

        if self.phoneActivationTime is not None and not isinstance(self.phoneActivationTime, XSDDateTime):
            self.phoneActivationTime = XSDDateTime(self.phoneActivationTime)

        if self.storageCapacityInBytes is not None and not isinstance(self.storageCapacityInBytes, int):
            self.storageCapacityInBytes = int(self.storageCapacityInBytes)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MutexFacet(Facet):
    """
    A mutex facet is a grouping of characteristics unique to a mechanism that enforces limits on access to a resource
    when there are many threads of execution. A mutex is designed to enforce a mutual exclusion concurrency control
    policy, and with a variety of possible methods there exists multiple unique implementations for different
    applications. [based on https://en.wikipedia.org/wiki/Lock_(computer_science)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MutexFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:MutexFacet"
    class_name: ClassVar[str] = "MutexFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MutexFacet

    isNamed: Optional[Union[bool, Bool]] = None
    mutexName: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.isNamed is not None and not isinstance(self.isNamed, Bool):
            self.isNamed = Bool(self.isNamed)

        if self.mutexName is not None and not isinstance(self.mutexName, str):
            self.mutexName = str(self.mutexName)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NTFSFileFacet(Facet):
    """
    An NTFS file facet is a grouping of characteristics unique to a file on an NTFS (new technology filesystem) file
    system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NTFSFileFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:NTFSFileFacet"
    class_name: ClassVar[str] = "NTFSFileFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NTFSFileFacet

    alternateDataStreams: Optional[Union[Union[str, AlternateDataStreamId], list[Union[str, AlternateDataStreamId]]]] = empty_list()
    entryID: Optional[int] = None
    sid: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.alternateDataStreams, list):
            self.alternateDataStreams = [self.alternateDataStreams] if self.alternateDataStreams is not None else []
        self.alternateDataStreams = [v if isinstance(v, AlternateDataStreamId) else AlternateDataStreamId(v) for v in self.alternateDataStreams]

        if self.entryID is not None and not isinstance(self.entryID, int):
            self.entryID = int(self.entryID)

        if self.sid is not None and not isinstance(self.sid, str):
            self.sid = str(self.sid)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class NTFSFilePermissionsFacet(Facet):
    """
    An NTFS file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change,
    navigate, execute) of a file on an NTFS (new technology filesystem) file system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NTFSFilePermissionsFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:NTFSFilePermissionsFacet"
    class_name: ClassVar[str] = "NTFSFilePermissionsFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NTFSFilePermissionsFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NetworkConnectionFacet(Facet):
    """
    A network connection facet is a grouping of characteristics unique to a connection (complete or attempted) accross
    a digital network (a group of two or more computer systems linked together). [based on
    https://www.webopedia.com/TERM/N/network.html]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NetworkConnectionFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:NetworkConnectionFacet"
    class_name: ClassVar[str] = "NetworkConnectionFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NetworkConnectionFacet

    destinationPort: Optional[int] = None
    dst: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    isActive: Optional[Union[bool, Bool]] = None
    observable_endTime: Optional[Union[str, XSDDateTime]] = None
    observable_startTime: Optional[Union[str, XSDDateTime]] = None
    protocols: Optional[Union[dict, ControlledDictionary]] = None
    sourcePort: Optional[int] = None
    src: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.destinationPort is not None and not isinstance(self.destinationPort, int):
            self.destinationPort = int(self.destinationPort)

        if not isinstance(self.dst, list):
            self.dst = [self.dst] if self.dst is not None else []
        self.dst = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.dst]

        if self.isActive is not None and not isinstance(self.isActive, Bool):
            self.isActive = Bool(self.isActive)

        if self.observable_endTime is not None and not isinstance(self.observable_endTime, XSDDateTime):
            self.observable_endTime = XSDDateTime(self.observable_endTime)

        if self.observable_startTime is not None and not isinstance(self.observable_startTime, XSDDateTime):
            self.observable_startTime = XSDDateTime(self.observable_startTime)

        if self.protocols is not None and not isinstance(self.protocols, ControlledDictionary):
            self.protocols = ControlledDictionary(**as_dict(self.protocols))

        if self.sourcePort is not None and not isinstance(self.sourcePort, int):
            self.sourcePort = int(self.sourcePort)

        if not isinstance(self.src, list):
            self.src = [self.src] if self.src is not None else []
        self.src = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.src]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NetworkFlowFacet(Facet):
    """
    A network flow facet is a grouping of characteristics unique to a sequence of data transiting one or more digital
    network (a group of two or more computer systems linked together) connections. [based on
    https://www.webopedia.com/TERM/N/network.html]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NetworkFlowFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:NetworkFlowFacet"
    class_name: ClassVar[str] = "NetworkFlowFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NetworkFlowFacet

    dstBytes: Optional[int] = None
    dstPackets: Optional[int] = None
    dstPayload: Optional[Union[str, ObservableObjectId]] = None
    ipfix: Optional[Union[dict, Dictionary]] = None
    srcBytes: Optional[int] = None
    srcPackets: Optional[int] = None
    srcPayload: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.dstBytes is not None and not isinstance(self.dstBytes, int):
            self.dstBytes = int(self.dstBytes)

        if self.dstPackets is not None and not isinstance(self.dstPackets, int):
            self.dstPackets = int(self.dstPackets)

        if self.dstPayload is not None and not isinstance(self.dstPayload, ObservableObjectId):
            self.dstPayload = ObservableObjectId(self.dstPayload)

        if self.ipfix is not None and not isinstance(self.ipfix, Dictionary):
            self.ipfix = Dictionary(**as_dict(self.ipfix))

        if self.srcBytes is not None and not isinstance(self.srcBytes, int):
            self.srcBytes = int(self.srcBytes)

        if self.srcPackets is not None and not isinstance(self.srcPackets, int):
            self.srcPackets = int(self.srcPackets)

        if self.srcPayload is not None and not isinstance(self.srcPayload, ObservableObjectId):
            self.srcPayload = ObservableObjectId(self.srcPayload)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NetworkInterfaceFacet(Facet):
    """
    A network interface facet is a grouping of characteristics unique to a software or hardware interface between two
    pieces of equipment or protocol layers in a computer network.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NetworkInterfaceFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:NetworkInterfaceFacet"
    class_name: ClassVar[str] = "NetworkInterfaceFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NetworkInterfaceFacet

    adapterName: Optional[str] = None
    dhcpLeaseExpires: Optional[Union[str, XSDDateTime]] = None
    dhcpLeaseObtained: Optional[Union[str, XSDDateTime]] = None
    dhcpServer: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    ip: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    ipGateway: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    macAddress: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.adapterName is not None and not isinstance(self.adapterName, str):
            self.adapterName = str(self.adapterName)

        if self.dhcpLeaseExpires is not None and not isinstance(self.dhcpLeaseExpires, XSDDateTime):
            self.dhcpLeaseExpires = XSDDateTime(self.dhcpLeaseExpires)

        if self.dhcpLeaseObtained is not None and not isinstance(self.dhcpLeaseObtained, XSDDateTime):
            self.dhcpLeaseObtained = XSDDateTime(self.dhcpLeaseObtained)

        if not isinstance(self.dhcpServer, list):
            self.dhcpServer = [self.dhcpServer] if self.dhcpServer is not None else []
        self.dhcpServer = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.dhcpServer]

        if not isinstance(self.ip, list):
            self.ip = [self.ip] if self.ip is not None else []
        self.ip = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.ip]

        if not isinstance(self.ipGateway, list):
            self.ipGateway = [self.ipGateway] if self.ipGateway is not None else []
        self.ipGateway = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.ipGateway]

        if self.macAddress is not None and not isinstance(self.macAddress, ObservableObjectId):
            self.macAddress = ObservableObjectId(self.macAddress)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NoteFacet(Facet):
    """
    A note facet is a grouping of characteristics unique to a brief textual record.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NoteFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:NoteFacet"
    class_name: ClassVar[str] = "NoteFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NoteFacet

    application: Optional[Union[str, ObservableObjectId]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    observable_modifiedTime: Optional[Union[str, XSDDateTime]] = None
    text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.observable_modifiedTime is not None and not isinstance(self.observable_modifiedTime, XSDDateTime):
            self.observable_modifiedTime = XSDDateTime(self.observable_modifiedTime)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Observable(UcoObject):
    """
    An observable is a characterizable item or action within the digital domain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Observable"]
    class_class_curie: ClassVar[str] = "uco-observable:Observable"
    class_name: ClassVar[str] = "Observable"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Observable

    id: Union[str, ObservableId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservableId):
            self.id = ObservableId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ObservableAction(Observable):
    """
    An observable action is a grouping of characteristics unique to something that may be done or performed within the
    digital domain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ObservableAction"]
    class_class_curie: ClassVar[str] = "uco-observable:ObservableAction"
    class_name: ClassVar[str] = "ObservableAction"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ObservableAction

    id: Union[str, ObservableActionId] = None
    type: Optional[Union[str, URIorCURIE]] = None
    createdBy: Optional[Union[str, IdentityAbstractionId]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    externalReference: Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]] = empty_list()
    hasFacet: Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    objectMarking: Optional[Union[Union[str, MarkingDefinitionAbstractionId], list[Union[str, MarkingDefinitionAbstractionId]]]] = empty_list()
    objectStatus: Optional[Union[str, "ObjectStatusVocab"]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, list[str]]] = empty_list()
    actionCount: Optional[Union[int, UcoNonNegativeInteger]] = None
    actionStatus: Optional[Union[str, "ActionStatusTypeVocab"]] = None
    action_endTime: Optional[Union[str, XSDDateTime]] = None
    action_object: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    action_startTime: Optional[Union[str, XSDDateTime]] = None
    environment: Optional[Union[str, UcoObjectId]] = None
    error: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    instrument: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    location: Optional[Union[Union[str, LocationId], list[Union[str, LocationId]]]] = empty_list()
    participant: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    performer: Optional[Union[str, UcoObjectId]] = None
    result: Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]] = empty_list()
    subaction: Optional[Union[Union[str, ActionId], list[Union[str, ActionId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservableActionId):
            self.id = ObservableActionId(self.id)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.createdBy is not None and not isinstance(self.createdBy, IdentityAbstractionId):
            self.createdBy = IdentityAbstractionId(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, ExternalReference) else ExternalReference(**as_dict(v)) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, Facet) else Facet(**as_dict(v)) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstractionId) else MarkingDefinitionAbstractionId(v) for v in self.objectMarking]

        if self.objectStatus is not None and not isinstance(self.objectStatus, ObjectStatusVocab):
            self.objectStatus = ObjectStatusVocab(self.objectStatus)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        if self.actionCount is not None and not isinstance(self.actionCount, UcoNonNegativeInteger):
            self.actionCount = UcoNonNegativeInteger(self.actionCount)

        if self.actionStatus is not None and not isinstance(self.actionStatus, (ActionStatusTypeVocab, str)):
            value = self.actionStatus
            for _coerce in (lambda: ActionStatusTypeVocab(value), lambda: str(value)):
                try:
                    self.actionStatus = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[ActionStatusTypeVocab, str] could be constructed from {value!r} for slot actionStatus")

        if self.action_endTime is not None and not isinstance(self.action_endTime, XSDDateTime):
            self.action_endTime = XSDDateTime(self.action_endTime)

        if not isinstance(self.action_object, list):
            self.action_object = [self.action_object] if self.action_object is not None else []
        self.action_object = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.action_object]

        if self.action_startTime is not None and not isinstance(self.action_startTime, XSDDateTime):
            self.action_startTime = XSDDateTime(self.action_startTime)

        if self.environment is not None and not isinstance(self.environment, UcoObjectId):
            self.environment = UcoObjectId(self.environment)

        if not isinstance(self.error, list):
            self.error = [self.error] if self.error is not None else []
        self.error = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.error]

        if not isinstance(self.instrument, list):
            self.instrument = [self.instrument] if self.instrument is not None else []
        self.instrument = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.instrument]

        if not isinstance(self.location, list):
            self.location = [self.location] if self.location is not None else []
        self.location = [v if isinstance(v, LocationId) else LocationId(v) for v in self.location]

        if not isinstance(self.participant, list):
            self.participant = [self.participant] if self.participant is not None else []
        self.participant = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.participant]

        if self.performer is not None and not isinstance(self.performer, UcoObjectId):
            self.performer = UcoObjectId(self.performer)

        if not isinstance(self.result, list):
            self.result = [self.result] if self.result is not None else []
        self.result = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.result]

        if not isinstance(self.subaction, list):
            self.subaction = [self.subaction] if self.subaction is not None else []
        self.subaction = [v if isinstance(v, ActionId) else ActionId(v) for v in self.subaction]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservableObject(Observable):
    """
    An observable object is a grouping of characteristics unique to a distinct article or unit within the digital
    domain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ObservableObject"]
    class_class_curie: ClassVar[str] = "uco-observable:ObservableObject"
    class_name: ClassVar[str] = "ObservableObject"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ObservableObject

    id: Union[str, ObservableObjectId] = None
    type: Optional[Union[str, URIorCURIE]] = None
    createdBy: Optional[Union[str, IdentityAbstractionId]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    externalReference: Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]] = empty_list()
    hasFacet: Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    objectMarking: Optional[Union[Union[str, MarkingDefinitionAbstractionId], list[Union[str, MarkingDefinitionAbstractionId]]]] = empty_list()
    objectStatus: Optional[Union[str, "ObjectStatusVocab"]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, list[str]]] = empty_list()
    hasChanged: Optional[Union[bool, Bool]] = None
    state: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservableObjectId):
            self.id = ObservableObjectId(self.id)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.createdBy is not None and not isinstance(self.createdBy, IdentityAbstractionId):
            self.createdBy = IdentityAbstractionId(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, ExternalReference) else ExternalReference(**as_dict(v)) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, Facet) else Facet(**as_dict(v)) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstractionId) else MarkingDefinitionAbstractionId(v) for v in self.objectMarking]

        if self.objectStatus is not None and not isinstance(self.objectStatus, ObjectStatusVocab):
            self.objectStatus = ObjectStatusVocab(self.objectStatus)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        if self.hasChanged is not None and not isinstance(self.hasChanged, Bool):
            self.hasChanged = Bool(self.hasChanged)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class API(ObservableObject):
    """
    An API (application programming interface) is a computing interface that defines interactions between multiple
    software or mixed hardware-software intermediaries. It defines the kinds of calls or requests that can be made,
    how to make them, the data formats that should be used, the conventions to follow, etc. [based on
    https://en.wikipedia.org/wiki/API]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["API"]
    class_class_curie: ClassVar[str] = "uco-observable:API"
    class_name: ClassVar[str] = "API"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.API

    id: Union[str, APIId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, APIId):
            self.id = APIId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ARPCache(ObservableObject):
    """
    An ARP cache is a collection of Address Resolution Protocol (ARP) entries (mostly dynamic) that are created when
    an IP address is resolved to a MAC address (so the computer can effectively communicate with the IP address).
    [based on https://en.wikipedia.org/wiki/ARP_cache]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ARPCache"]
    class_class_curie: ClassVar[str] = "uco-observable:ARPCache"
    class_name: ClassVar[str] = "ARPCache"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ARPCache

    id: Union[str, ARPCacheId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ARPCacheId):
            self.id = ARPCacheId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ARPCacheEntry(ObservableObject):
    """
    An ARP cache entry is a single Address Resolution Protocol (ARP) response record that is created when an IP
    address is resolved to a MAC address (so the computer can effectively communicate with the IP address). [based on
    https://en.wikipedia.org/wiki/ARP_cache]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ARPCacheEntry"]
    class_class_curie: ClassVar[str] = "uco-observable:ARPCacheEntry"
    class_name: ClassVar[str] = "ARPCacheEntry"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ARPCacheEntry

    id: Union[str, ARPCacheEntryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ARPCacheEntryId):
            self.id = ARPCacheEntryId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Account(ObservableObject):
    """
    An account is an arrangement with an entity to enable and control the provision of some capability or service.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Account"]
    class_class_curie: ClassVar[str] = "uco-observable:Account"
    class_name: ClassVar[str] = "Account"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Account

    id: Union[str, AccountId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AccountId):
            self.id = AccountId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Address(ObservableObject):
    """
    An address is an identifier assigned to enable routing and management of information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Address"]
    class_class_curie: ClassVar[str] = "uco-observable:Address"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Address

    id: Union[str, AddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AddressId):
            self.id = AddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AlternateDataStream(ObservableObject):
    """
    An alternate data stream is data content stored within an NTFS file that is independent of the standard content
    stream of the file and is hidden from access by default NTFS file viewing mechanisms.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AlternateDataStream"]
    class_class_curie: ClassVar[str] = "uco-observable:AlternateDataStream"
    class_name: ClassVar[str] = "AlternateDataStream"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AlternateDataStream

    id: Union[str, AlternateDataStreamId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlternateDataStreamId):
            self.id = AlternateDataStreamId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Application(ObservableObject):
    """
    An application is a particular software program designed for end users.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Application"]
    class_class_curie: ClassVar[str] = "uco-observable:Application"
    class_name: ClassVar[str] = "Application"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Application

    id: Union[str, ApplicationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApplicationId):
            self.id = ApplicationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Audio(ObservableObject):
    """
    Audio is a digital representation of sound.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Audio"]
    class_class_curie: ClassVar[str] = "uco-observable:Audio"
    class_name: ClassVar[str] = "Audio"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Audio

    id: Union[str, AudioId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AudioId):
            self.id = AudioId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AutonomousSystem(ObservableObject):
    """
    An autonomous system is a collection of connected Internet Protocol (IP) routing prefixes under the control of one
    or more network operators on behalf of a single administrative entity or domain that presents a common, clearly
    defined routing policy to the Internet. [based on https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AutonomousSystem"]
    class_class_curie: ClassVar[str] = "uco-observable:AutonomousSystem"
    class_name: ClassVar[str] = "AutonomousSystem"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AutonomousSystem

    id: Union[str, AutonomousSystemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutonomousSystemId):
            self.id = AutonomousSystemId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BotConfiguration(ObservableObject):
    """
    A bot configuration is a set of contextual settings for a software application that runs automated tasks (scripts)
    over the Internet at a much higher rate than would be possible for a human alone.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["BotConfiguration"]
    class_class_curie: ClassVar[str] = "uco-observable:BotConfiguration"
    class_name: ClassVar[str] = "BotConfiguration"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BotConfiguration

    id: Union[str, BotConfigurationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BotConfigurationId):
            self.id = BotConfigurationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BrowserBookmark(ObservableObject):
    """
    A browser bookmark is a saved shortcut that directs a WWW (World Wide Web) browser software program to a
    particular WWW accessible resource. [based on https://techterms.com/definition/bookmark]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["BrowserBookmark"]
    class_class_curie: ClassVar[str] = "uco-observable:BrowserBookmark"
    class_name: ClassVar[str] = "BrowserBookmark"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BrowserBookmark

    id: Union[str, BrowserBookmarkId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BrowserBookmarkId):
            self.id = BrowserBookmarkId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BrowserCookie(ObservableObject):
    """
    A browser cookie is a piece of of data sent from a website and stored on the user's computer by the user's web
    browser while the user is browsing. [based on https://en.wikipedia.org/wiki/HTTP_cookie]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["BrowserCookie"]
    class_class_curie: ClassVar[str] = "uco-observable:BrowserCookie"
    class_name: ClassVar[str] = "BrowserCookie"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BrowserCookie

    id: Union[str, BrowserCookieId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BrowserCookieId):
            self.id = BrowserCookieId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Calendar(ObservableObject):
    """
    A calendar is a collection of appointments, meetings, and events.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Calendar"]
    class_class_curie: ClassVar[str] = "uco-observable:Calendar"
    class_name: ClassVar[str] = "Calendar"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Calendar

    id: Union[str, CalendarId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CalendarId):
            self.id = CalendarId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CalendarEntry(ObservableObject):
    """
    A calendar entry is an appointment, meeting or event within a collection of appointments, meetings and events.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CalendarEntry"]
    class_class_curie: ClassVar[str] = "uco-observable:CalendarEntry"
    class_name: ClassVar[str] = "CalendarEntry"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CalendarEntry

    id: Union[str, CalendarEntryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CalendarEntryId):
            self.id = CalendarEntryId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Call(ObservableObject):
    """
    A call is a connection as part of a realtime cyber communication between one or more parties.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Call"]
    class_class_curie: ClassVar[str] = "uco-observable:Call"
    class_name: ClassVar[str] = "Call"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Call

    id: Union[str, CallId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CallId):
            self.id = CallId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CapturedTelecommunicationsInformation(ObservableObject):
    """
    UCO 1.5.0 declares the class uco-observable:CapturedTelecommunicationsInformation without a definition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CapturedTelecommunicationsInformation"]
    class_class_curie: ClassVar[str] = "uco-observable:CapturedTelecommunicationsInformation"
    class_name: ClassVar[str] = "CapturedTelecommunicationsInformation"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CapturedTelecommunicationsInformation

    id: Union[str, CapturedTelecommunicationsInformationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CapturedTelecommunicationsInformationId):
            self.id = CapturedTelecommunicationsInformationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CellSite(ObservableObject):
    """
    UCO 1.5.0 declares the class uco-observable:CellSite without a definition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CellSite"]
    class_class_curie: ClassVar[str] = "uco-observable:CellSite"
    class_name: ClassVar[str] = "CellSite"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CellSite

    id: Union[str, CellSiteId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellSiteId):
            self.id = CellSiteId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Code(ObservableObject):
    """
    Code is a direct representation (source, byte or binary) of a collection of computer instructions that form
    software which tell a computer how to work. [based on https://en.wikipedia.org/wiki/Software]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Code"]
    class_class_curie: ClassVar[str] = "uco-observable:Code"
    class_name: ClassVar[str] = "Code"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Code

    id: Union[str, CodeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CodeId):
            self.id = CodeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ComputerSpecification(ObservableObject):
    """
    A computer specification is the hardware and software of a programmable electronic device that can store,
    retrieve, and process data. {based on merriam-webster.com/dictionary/computer]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ComputerSpecification"]
    class_class_curie: ClassVar[str] = "uco-observable:ComputerSpecification"
    class_name: ClassVar[str] = "ComputerSpecification"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ComputerSpecification

    id: Union[str, ComputerSpecificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComputerSpecificationId):
            self.id = ComputerSpecificationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Contact(ObservableObject):
    """
    A contact is a set of identification and communication related details for a single entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Contact"]
    class_class_curie: ClassVar[str] = "uco-observable:Contact"
    class_name: ClassVar[str] = "Contact"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Contact

    id: Union[str, ContactId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContactId):
            self.id = ContactId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContactList(ObservableObject):
    """
    A contact list is a set of multiple individual contacts such as that found in a digital address book.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContactList"]
    class_class_curie: ClassVar[str] = "uco-observable:ContactList"
    class_name: ClassVar[str] = "ContactList"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContactList

    id: Union[str, ContactListId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContactListId):
            self.id = ContactListId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ContentData(ObservableObject):
    """
    Content data is a block of digital data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ContentData"]
    class_class_curie: ClassVar[str] = "uco-observable:ContentData"
    class_name: ClassVar[str] = "ContentData"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ContentData

    id: Union[str, ContentDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContentDataId):
            self.id = ContentDataId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CookieHistory(ObservableObject):
    """
    A cookie history is the stored web cookie history for a particular web browser.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CookieHistory"]
    class_class_curie: ClassVar[str] = "uco-observable:CookieHistory"
    class_name: ClassVar[str] = "CookieHistory"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CookieHistory

    id: Union[str, CookieHistoryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CookieHistoryId):
            self.id = CookieHistoryId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Credential(ObservableObject):
    """
    A credential is a single specific login and password combination for authorization of access to a digital account
    or system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Credential"]
    class_class_curie: ClassVar[str] = "uco-observable:Credential"
    class_name: ClassVar[str] = "Credential"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Credential

    id: Union[str, CredentialId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CredentialId):
            self.id = CredentialId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CredentialDump(ObservableObject):
    """
    A credential dump is a collection (typically forcibly extracted from a system) of specific login and password
    combinations for authorization of access to a digital account or system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CredentialDump"]
    class_class_curie: ClassVar[str] = "uco-observable:CredentialDump"
    class_name: ClassVar[str] = "CredentialDump"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CredentialDump

    id: Union[str, CredentialDumpId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CredentialDumpId):
            self.id = CredentialDumpId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DNSCache(ObservableObject):
    """
    An DNS cache is a temporary locally stored collection of previous Domain Name System (DNS) query results (created
    when an domain name is resolved to a IP address) for a particular computer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DNSCache"]
    class_class_curie: ClassVar[str] = "uco-observable:DNSCache"
    class_name: ClassVar[str] = "DNSCache"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DNSCache

    id: Union[str, DNSCacheId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DNSCacheId):
            self.id = DNSCacheId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DNSRecord(ObservableObject):
    """
    A DNS record is a single Domain Name System (DNS) artifact specifying information of a particular type (routing,
    authority, responsibility, security, etc.) for a specific Internet domain name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DNSRecord"]
    class_class_curie: ClassVar[str] = "uco-observable:DNSRecord"
    class_name: ClassVar[str] = "DNSRecord"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DNSRecord

    id: Union[str, DNSRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DNSRecordId):
            self.id = DNSRecordId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Device(ObservableObject):
    """
    A device is a piece of equipment or a mechanism designed to serve a special purpose or perform a special function.
    [based on https://www.merriam-webster.com/dictionary/device]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Device"]
    class_class_curie: ClassVar[str] = "uco-observable:Device"
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Device

    id: Union[str, DeviceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Adaptor(Device):
    """
    An adaptor is a device that physically converts the pin outputs but does not alter the underlying protocol (e.g.
    uSD to SD, CF to ATA, etc.)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Adaptor"]
    class_class_curie: ClassVar[str] = "uco-observable:Adaptor"
    class_name: ClassVar[str] = "Adaptor"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Adaptor

    id: Union[str, AdaptorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdaptorId):
            self.id = AdaptorId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AndroidDevice(Device):
    """
    An Android device is a device running the Android operating system. [based on
    https://en.wikipedia.org/wiki/Android_(operating_system)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AndroidDevice"]
    class_class_curie: ClassVar[str] = "uco-observable:AndroidDevice"
    class_name: ClassVar[str] = "AndroidDevice"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AndroidDevice

    id: Union[str, AndroidDeviceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AndroidDeviceId):
            self.id = AndroidDeviceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class AppleDevice(Device):
    """
    An apple device is a smart device that applies either the MacOS or iOS operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AppleDevice"]
    class_class_curie: ClassVar[str] = "uco-observable:AppleDevice"
    class_name: ClassVar[str] = "AppleDevice"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AppleDevice

    id: Union[str, AppleDeviceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AppleDeviceId):
            self.id = AppleDeviceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Appliance(Device):
    """
    An appliance is a purpose-built computer with software or firmware that is designed to provide a specific
    computing capability or resource. [based on https://en.wikipedia.org/wiki/Computer_appliance]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Appliance"]
    class_class_curie: ClassVar[str] = "uco-observable:Appliance"
    class_name: ClassVar[str] = "Appliance"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Appliance

    id: Union[str, ApplianceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApplianceId):
            self.id = ApplianceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Computer(Device):
    """
    A computer is an electronic device for storing and processing data, typically in binary, according to instructions
    given to it in a variable program. [based on 'Computer.' Oxford English Dictionary, Oxford University Press,
    2022.]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Computer"]
    class_class_curie: ClassVar[str] = "uco-observable:Computer"
    class_name: ClassVar[str] = "Computer"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Computer

    id: Union[str, ComputerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComputerId):
            self.id = ComputerId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DigitalAccount(Account):
    """
    A digital account is an arrangement with an entity to enable and control the provision of some capability or
    service within the digital domain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DigitalAccount"]
    class_class_curie: ClassVar[str] = "uco-observable:DigitalAccount"
    class_name: ClassVar[str] = "DigitalAccount"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DigitalAccount

    id: Union[str, DigitalAccountId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DigitalAccountId):
            self.id = DigitalAccountId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ApplicationAccount(DigitalAccount):
    """
    An application account is an account within a particular software program designed for end users.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ApplicationAccount"]
    class_class_curie: ClassVar[str] = "uco-observable:ApplicationAccount"
    class_name: ClassVar[str] = "ApplicationAccount"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ApplicationAccount

    id: Union[str, ApplicationAccountId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApplicationAccountId):
            self.id = ApplicationAccountId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DigitalAddress(Address):
    """
    A digital address is an identifier assigned to enable routing and management of digital communication.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DigitalAddress"]
    class_class_curie: ClassVar[str] = "uco-observable:DigitalAddress"
    class_name: ClassVar[str] = "DigitalAddress"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DigitalAddress

    id: Union[str, DigitalAddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DigitalAddressId):
            self.id = DigitalAddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DigitalCamera(Device):
    """
    A digital camera is a camera that captures photographs in digital memory as opposed to capturing images on
    photographic film.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DigitalCamera"]
    class_class_curie: ClassVar[str] = "uco-observable:DigitalCamera"
    class_name: ClassVar[str] = "DigitalCamera"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DigitalCamera

    id: Union[str, DigitalCameraId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DigitalCameraId):
            self.id = DigitalCameraId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DigitalSignatureInfo(ObservableObject):
    """
    A digital signature info is a value calculated via a mathematical scheme for demonstrating the authenticity of an
    electronic message or document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DigitalSignatureInfo"]
    class_class_curie: ClassVar[str] = "uco-observable:DigitalSignatureInfo"
    class_name: ClassVar[str] = "DigitalSignatureInfo"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DigitalSignatureInfo

    id: Union[str, DigitalSignatureInfoId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DigitalSignatureInfoId):
            self.id = DigitalSignatureInfoId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Disk(ObservableObject):
    """
    A disk is a storage mechanism where data is recorded by various electronic, magnetic, optical, or mechanical
    changes to a surface layer of one or more rotating disks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Disk"]
    class_class_curie: ClassVar[str] = "uco-observable:Disk"
    class_name: ClassVar[str] = "Disk"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Disk

    id: Union[str, DiskId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiskId):
            self.id = DiskId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DiskPartition(ObservableObject):
    """
    A disk partition is a particular managed region on a storage mechanism where data is recorded by various
    electronic, magnetic, optical, or mechanical changes to a surface layer of one or more rotating disks. [based on
    https://en.wikipedia.org/wiki/Disk_storage]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DiskPartition"]
    class_class_curie: ClassVar[str] = "uco-observable:DiskPartition"
    class_name: ClassVar[str] = "DiskPartition"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DiskPartition

    id: Union[str, DiskPartitionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiskPartitionId):
            self.id = DiskPartitionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class DomainName(ObservableObject):
    """
    A domain name is an identification string that defines a realm of administrative autonomy, authority or control
    within the Internet. [based on https://en.wikipedia.org/wiki/Domain_name]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["DomainName"]
    class_class_curie: ClassVar[str] = "uco-observable:DomainName"
    class_name: ClassVar[str] = "DomainName"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.DomainName

    id: Union[str, DomainNameId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DomainNameId):
            self.id = DomainNameId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EmailAccount(DigitalAccount):
    """
    An email account is an arrangement with an entity to enable and control the provision of electronic mail (email)
    capabilities or services.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EmailAccount"]
    class_class_curie: ClassVar[str] = "uco-observable:EmailAccount"
    class_name: ClassVar[str] = "EmailAccount"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EmailAccount

    id: Union[str, EmailAccountId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmailAccountId):
            self.id = EmailAccountId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EmailAddress(DigitalAddress):
    """
    An email address is an identifier for an electronic mailbox to which electronic mail messages (conformant to the
    Simple Mail Transfer Protocol (SMTP)) are sent from and delivered to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EmailAddress"]
    class_class_curie: ClassVar[str] = "uco-observable:EmailAddress"
    class_name: ClassVar[str] = "EmailAddress"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EmailAddress

    id: Union[str, EmailAddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmailAddressId):
            self.id = EmailAddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EmbeddedDevice(Device):
    """
    An embedded device is a highly specialized microprocessor device meant for one or very few specific purposes and
    is usually embedded or included within another object or as part of a larger system. Examples include answer
    machine, door access logger, card scanner, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EmbeddedDevice"]
    class_class_curie: ClassVar[str] = "uco-observable:EmbeddedDevice"
    class_name: ClassVar[str] = "EmbeddedDevice"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EmbeddedDevice

    id: Union[str, EmbeddedDeviceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmbeddedDeviceId):
            self.id = EmbeddedDeviceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EventLog(ObservableObject):
    """
    An event log is a collection of event records.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EventLog"]
    class_class_curie: ClassVar[str] = "uco-observable:EventLog"
    class_name: ClassVar[str] = "EventLog"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EventLog

    id: Union[str, EventLogId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventLogId):
            self.id = EventLogId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EventRecord(ObservableObject):
    """
    An event record is something that happens in a digital context (e.g., operating system events).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EventRecord"]
    class_class_curie: ClassVar[str] = "uco-observable:EventRecord"
    class_name: ClassVar[str] = "EventRecord"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EventRecord

    id: Union[str, EventRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventRecordId):
            self.id = EventRecordId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class FileSystem(ObservableObject):
    """
    A file system is the process that manages how and where data on a storage medium is stored, accessed and managed.
    [based on https://www.techopedia.com/definition/5510/file-system]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["FileSystem"]
    class_class_curie: ClassVar[str] = "uco-observable:FileSystem"
    class_name: ClassVar[str] = "FileSystem"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.FileSystem

    id: Union[str, FileSystemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileSystemId):
            self.id = FileSystemId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class FileSystemObject(ObservableObject):
    """
    A file system object is an informational object represented and managed within a file system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["FileSystemObject"]
    class_class_curie: ClassVar[str] = "uco-observable:FileSystemObject"
    class_name: ClassVar[str] = "FileSystemObject"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.FileSystemObject

    id: Union[str, FileSystemObjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileSystemObjectId):
            self.id = FileSystemObjectId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BlockDeviceNode(FileSystemObject):
    """
    A block device node is a UNIX filesystem special file that serves as a conduit to communicate with devices,
    providing buffered randomly accesible input and output. Block device nodes are used to apply access rights to the
    devices and to direct operations on the files to the appropriate device drivers. [based on
    https://en.wikipedia.org/wiki/Unix_file_types]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["BlockDeviceNode"]
    class_class_curie: ClassVar[str] = "uco-observable:BlockDeviceNode"
    class_name: ClassVar[str] = "BlockDeviceNode"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BlockDeviceNode

    id: Union[str, BlockDeviceNodeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BlockDeviceNodeId):
            self.id = BlockDeviceNodeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class CharacterDeviceNode(FileSystemObject):
    """
    A character device node is a UNIX filesystem special file that serves as a conduit to communicate with devices,
    providing only a serial stream of input or accepting a serial stream of output. Character device nodes are used to
    apply access rights to the devices and to direct operations on the files to the appropriate device drivers. [based
    on https://en.wikipedia.org/wiki/Unix_file_types]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["CharacterDeviceNode"]
    class_class_curie: ClassVar[str] = "uco-observable:CharacterDeviceNode"
    class_name: ClassVar[str] = "CharacterDeviceNode"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.CharacterDeviceNode

    id: Union[str, CharacterDeviceNodeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CharacterDeviceNodeId):
            self.id = CharacterDeviceNodeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Directory(FileSystemObject):
    """
    A directory is a file system cataloging structure which contains references to other computer files, and possibly
    other directories. On many computers, directories are known as folders, or drawers, analogous to a workbench or
    the traditional office filing cabinet. In UNIX a directory is implemented as a special file. [based on
    https://en.wikipedia.org/wiki/Directory_(computing)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Directory"]
    class_class_curie: ClassVar[str] = "uco-observable:Directory"
    class_name: ClassVar[str] = "Directory"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Directory

    id: Union[str, DirectoryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DirectoryId):
            self.id = DirectoryId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class File(FileSystemObject):
    """
    A file is a computer resource for recording data discretely on a computer storage device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["File"]
    class_class_curie: ClassVar[str] = "uco-observable:File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.File

    id: Union[str, FileId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileId):
            self.id = FileId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ArchiveFile(File):
    """
    An archive file is a file that is composed of one or more computer files along with metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ArchiveFile"]
    class_class_curie: ClassVar[str] = "uco-observable:ArchiveFile"
    class_name: ClassVar[str] = "ArchiveFile"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ArchiveFile

    id: Union[str, ArchiveFileId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArchiveFileId):
            self.id = ArchiveFileId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GUI(ObservableObject):
    """
    A GUI is a graphical user interface that allows users to interact with electronic devices through graphical icons
    and audio indicators such as primary notation, instead of text-based user interfaces, typed command labels or text
    navigation. [based on https://en.wikipedia.org/wiki/Graphical_user_interface]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["GUI"]
    class_class_curie: ClassVar[str] = "uco-observable:GUI"
    class_name: ClassVar[str] = "GUI"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GUI

    id: Union[str, GUIId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GUIId):
            self.id = GUIId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GamingConsole(Device):
    """
    A gaming console (video game console or game console) is an electronic system that connects to a display,
    typically a TV or computer monitor, for the primary purpose of playing video games.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["GamingConsole"]
    class_class_curie: ClassVar[str] = "uco-observable:GamingConsole"
    class_name: ClassVar[str] = "GamingConsole"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GamingConsole

    id: Union[str, GamingConsoleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GamingConsoleId):
            self.id = GamingConsoleId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GenericObservableObject(ObservableObject):
    """
    A generic observable object is an article or unit within the digital domain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["GenericObservableObject"]
    class_class_curie: ClassVar[str] = "uco-observable:GenericObservableObject"
    class_name: ClassVar[str] = "GenericObservableObject"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GenericObservableObject

    id: Union[str, GenericObservableObjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenericObservableObjectId):
            self.id = GenericObservableObjectId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GeoLocationEntry(ObservableObject):
    """
    A geolocation entry is a single application-specific geolocation entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["GeoLocationEntry"]
    class_class_curie: ClassVar[str] = "uco-observable:GeoLocationEntry"
    class_name: ClassVar[str] = "GeoLocationEntry"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GeoLocationEntry

    id: Union[str, GeoLocationEntryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeoLocationEntryId):
            self.id = GeoLocationEntryId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GeoLocationLog(ObservableObject):
    """
    A geolocation log is a record containing geolocation tracks and/or geolocation entries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["GeoLocationLog"]
    class_class_curie: ClassVar[str] = "uco-observable:GeoLocationLog"
    class_name: ClassVar[str] = "GeoLocationLog"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GeoLocationLog

    id: Union[str, GeoLocationLogId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeoLocationLogId):
            self.id = GeoLocationLogId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class GeoLocationTrack(ObservableObject):
    """
    A geolocation track is a set of contiguous geolocation entries representing a path/track taken.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["GeoLocationTrack"]
    class_class_curie: ClassVar[str] = "uco-observable:GeoLocationTrack"
    class_name: ClassVar[str] = "GeoLocationTrack"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.GeoLocationTrack

    id: Union[str, GeoLocationTrackId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeoLocationTrackId):
            self.id = GeoLocationTrackId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Hostname(ObservableObject):
    """
    A hostname is a label that is assigned to a device connected to a computer network and that is used to identify
    the device in various forms of electronic communication, such as the World Wide Web. A hostname may be a domain
    name, if it is properly organized into the domain name system. A domain name may be a hostname if it has been
    assigned to an Internet host and associated with the host's IP address. [based on
    https://en.wikipedia.org/wiki/Hostname]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Hostname"]
    class_class_curie: ClassVar[str] = "uco-observable:Hostname"
    class_name: ClassVar[str] = "Hostname"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Hostname

    id: Union[str, HostnameId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HostnameId):
            self.id = HostnameId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class IPAddress(DigitalAddress):
    """
    An IP address is an Internet Protocol (IP) standards conformant identifier assigned to a device to enable routing
    and management of IP standards conformant communication to or from that device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["IPAddress"]
    class_class_curie: ClassVar[str] = "uco-observable:IPAddress"
    class_name: ClassVar[str] = "IPAddress"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IPAddress

    id: Union[str, IPAddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IPAddressId):
            self.id = IPAddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class IPNetmask(ObservableObject):
    """
    An IP netmask is a 32-bit 'mask' used to divide an IP address into subnets and specify the network's available
    hosts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["IPNetmask"]
    class_class_curie: ClassVar[str] = "uco-observable:IPNetmask"
    class_name: ClassVar[str] = "IPNetmask"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IPNetmask

    id: Union[str, IPNetmaskId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IPNetmaskId):
            self.id = IPNetmaskId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class IPv4Address(IPAddress):
    """
    An IPv4 (Internet Protocol version 4) address is an IPv4 standards conformant identifier assigned to a device to
    enable routing and management of IPv4 standards conformant communication to or from that device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["IPv4Address"]
    class_class_curie: ClassVar[str] = "uco-observable:IPv4Address"
    class_name: ClassVar[str] = "IPv4Address"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IPv4Address

    id: Union[str, IPv4AddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IPv4AddressId):
            self.id = IPv4AddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class IPv6Address(IPAddress):
    """
    An IPv6 (Internet Protocol version 6) address is an IPv6 standards conformant identifier assigned to a device to
    enable routing and management of IPv6 standards conformant communication to or from that device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["IPv6Address"]
    class_class_curie: ClassVar[str] = "uco-observable:IPv6Address"
    class_name: ClassVar[str] = "IPv6Address"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IPv6Address

    id: Union[str, IPv6AddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IPv6AddressId):
            self.id = IPv6AddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Image(ObservableObject):
    """
    An image is a complete copy of a hard disk, memory, or other digital media.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Image"]
    class_class_curie: ClassVar[str] = "uco-observable:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Image

    id: Union[str, ImageId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImageId):
            self.id = ImageId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class InstantMessagingAddress(DigitalAddress):
    """
    UCO 1.5.0 declares the class uco-observable:InstantMessagingAddress without a definition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["InstantMessagingAddress"]
    class_class_curie: ClassVar[str] = "uco-observable:InstantMessagingAddress"
    class_name: ClassVar[str] = "InstantMessagingAddress"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.InstantMessagingAddress

    id: Union[str, InstantMessagingAddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstantMessagingAddressId):
            self.id = InstantMessagingAddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Junction(FileSystemObject):
    """
    A junction is a specific NTFS (New Technology File System) reparse point to redirect a directory access to another
    directory which can be on the same volume or another volume. A junction is similar to a directory symbolic link
    but may differ on whether they are processed on the local system or on the remote file server. [based on
    https://jp-andre.pagesperso-orange.fr/junctions.html]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Junction"]
    class_class_curie: ClassVar[str] = "uco-observable:Junction"
    class_name: ClassVar[str] = "Junction"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Junction

    id: Union[str, JunctionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JunctionId):
            self.id = JunctionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Laptop(Computer):
    """
    A laptop, laptop computer, or notebook computer is a small, portable personal computer with a screen and
    alphanumeric keyboard. These typically have a clam shell form factor with the screen mounted on the inside of the
    upper lid and the keyboard on the inside of the lower lid, although 2-in-1 PCs with a detachable keyboard are
    often marketed as laptops or as having a laptop mode. (Devices categorized by their manufacturer as a Laptop)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Laptop"]
    class_class_curie: ClassVar[str] = "uco-observable:Laptop"
    class_name: ClassVar[str] = "Laptop"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Laptop

    id: Union[str, LaptopId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LaptopId):
            self.id = LaptopId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Library(ObservableObject):
    """
    A library is a suite of data and programming code that is used to develop software programs and applications.
    [based on https://www.techopedia.com/definition/3828/software-library]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Library"]
    class_class_curie: ClassVar[str] = "uco-observable:Library"
    class_name: ClassVar[str] = "Library"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Library

    id: Union[str, LibraryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LibraryId):
            self.id = LibraryId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MACAddress(DigitalAddress):
    """
    A MAC address is a media access control standards conformant identifier assigned to a network interface to enable
    routing and management of communications at the data link layer of a network segment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MACAddress"]
    class_class_curie: ClassVar[str] = "uco-observable:MACAddress"
    class_name: ClassVar[str] = "MACAddress"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MACAddress

    id: Union[str, MACAddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MACAddressId):
            self.id = MACAddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class BluetoothAddress(MACAddress):
    """
    A Bluetooth address is a Bluetooth standard conformant identifier assigned to a Bluetooth device to enable routing
    and management of Bluetooth standards conformant communication to or from that device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["BluetoothAddress"]
    class_class_curie: ClassVar[str] = "uco-observable:BluetoothAddress"
    class_name: ClassVar[str] = "BluetoothAddress"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BluetoothAddress

    id: Union[str, BluetoothAddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BluetoothAddressId):
            self.id = BluetoothAddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Memory(ObservableObject):
    """
    Memory is a particular region of temporary information storage (e.g., RAM (random access memory), ROM (read only
    memory)) on a digital device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Memory"]
    class_class_curie: ClassVar[str] = "uco-observable:Memory"
    class_name: ClassVar[str] = "Memory"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Memory

    id: Union[str, MemoryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MemoryId):
            self.id = MemoryId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Message(ObservableObject):
    """
    A message is a discrete unit of electronic communication intended by the source for consumption by some recipient
    or group of recipients. [based on https://en.wikipedia.org/wiki/Message]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Message"]
    class_class_curie: ClassVar[str] = "uco-observable:Message"
    class_name: ClassVar[str] = "Message"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Message

    id: Union[str, MessageId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MessageId):
            self.id = MessageId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class EmailMessage(Message):
    """
    An email message is a message that is an instance of an electronic mail correspondence conformant to the internet
    message format described in RFC 5322 and related RFCs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["EmailMessage"]
    class_class_curie: ClassVar[str] = "uco-observable:EmailMessage"
    class_name: ClassVar[str] = "EmailMessage"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.EmailMessage

    id: Union[str, EmailMessageId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmailMessageId):
            self.id = EmailMessageId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ForumPost(Message):
    """
    A forum post is message submitted by a user account to an online forum where the message content (and typically
    metadata including who posted it and when) is viewable by any party with viewing permissions on the forum.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ForumPost"]
    class_class_curie: ClassVar[str] = "uco-observable:ForumPost"
    class_name: ClassVar[str] = "ForumPost"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ForumPost

    id: Union[str, ForumPostId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ForumPostId):
            self.id = ForumPostId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ForumPrivateMessage(Message):
    """
    A forum private message (aka PM or DM (direct message)) is a one-to-one message from one specific user account to
    another specific user account on an online form where transmission is managed by the online forum platform and the
    message is only viewable by the parties directly involved.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ForumPrivateMessage"]
    class_class_curie: ClassVar[str] = "uco-observable:ForumPrivateMessage"
    class_name: ClassVar[str] = "ForumPrivateMessage"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ForumPrivateMessage

    id: Union[str, ForumPrivateMessageId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ForumPrivateMessageId):
            self.id = ForumPrivateMessageId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MessageThread(ObservableObject):
    """
    A message thread is a running commentary of electronic messages pertaining to one topic or question.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MessageThread"]
    class_class_curie: ClassVar[str] = "uco-observable:MessageThread"
    class_name: ClassVar[str] = "MessageThread"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MessageThread

    id: Union[str, MessageThreadId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MessageThreadId):
            self.id = MessageThreadId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MobileAccount(DigitalAccount):
    """
    A mobile account is an arrangement with an entity to enable and control the provision of some capability or
    service on a portable computing device. [based on https://www.lexico.com/definition/mobile_device]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MobileAccount"]
    class_class_curie: ClassVar[str] = "uco-observable:MobileAccount"
    class_name: ClassVar[str] = "MobileAccount"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MobileAccount

    id: Union[str, MobileAccountId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MobileAccountId):
            self.id = MobileAccountId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MobileDevice(Device):
    """
    A mobile device is a portable computing device. [based on https://www.lexico.com.definition/mobile_device]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MobileDevice"]
    class_class_curie: ClassVar[str] = "uco-observable:MobileDevice"
    class_name: ClassVar[str] = "MobileDevice"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MobileDevice

    id: Union[str, MobileDeviceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MobileDeviceId):
            self.id = MobileDeviceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Drone(MobileDevice):
    """
    A drone, unmanned aerial vehicle (UAV), is an aircraft without a human pilot, crew, or passengers that typically
    involve a ground-based controller and a system for communications with the UAV.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Drone"]
    class_class_curie: ClassVar[str] = "uco-observable:Drone"
    class_name: ClassVar[str] = "Drone"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Drone

    id: Union[str, DroneId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DroneId):
            self.id = DroneId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class MobilePhone(MobileDevice):
    """
    A mobile phone is a portable telephone that at least can make and receive calls over a radio frequency link while
    the user is moving within a telephone service area. This category encompasses all types of mobiles, simple and
    smart and satellite ones all together.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["MobilePhone"]
    class_class_curie: ClassVar[str] = "uco-observable:MobilePhone"
    class_name: ClassVar[str] = "MobilePhone"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.MobilePhone

    id: Union[str, MobilePhoneId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MobilePhoneId):
            self.id = MobilePhoneId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Mutex(ObservableObject):
    """
    A mutex is a mechanism that enforces limits on access to a resource when there are many threads of execution. A
    mutex is designed to enforce a mutual exclusion concurrency control policy, and with a variety of possible methods
    there exists multiple unique implementations for different applications. [based on
    https://en.wikipedia.org/wiki/Lock_(computer_science)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Mutex"]
    class_class_curie: ClassVar[str] = "uco-observable:Mutex"
    class_name: ClassVar[str] = "Mutex"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Mutex

    id: Union[str, MutexId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MutexId):
            self.id = MutexId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NTFSFile(File):
    """
    An NTFS file is a New Technology File System (NTFS) file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NTFSFile"]
    class_class_curie: ClassVar[str] = "uco-observable:NTFSFile"
    class_name: ClassVar[str] = "NTFSFile"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NTFSFile

    id: Union[str, NTFSFileId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NTFSFileId):
            self.id = NTFSFileId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NamedPipe(FileSystemObject):
    """
    A named pipe is a mechanism for FIFO (first-in-first-out) inter-process communication. It is persisted as a
    filesystem object (that can be deleted like any other file), can be written to or read from by any process and
    exists beyond the lifespan of any process interacting with it (unlike simple anonymous pipes). [based on
    https://en.wikipedia.org/wiki/Named_pipe]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NamedPipe"]
    class_class_curie: ClassVar[str] = "uco-observable:NamedPipe"
    class_name: ClassVar[str] = "NamedPipe"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NamedPipe

    id: Union[str, NamedPipeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedPipeId):
            self.id = NamedPipeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NetworkAppliance(Appliance):
    """
    A network appliance is a purpose-built computer with software or firmware that is designed to provide a specific
    network management function.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NetworkAppliance"]
    class_class_curie: ClassVar[str] = "uco-observable:NetworkAppliance"
    class_name: ClassVar[str] = "NetworkAppliance"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NetworkAppliance

    id: Union[str, NetworkApplianceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NetworkApplianceId):
            self.id = NetworkApplianceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NetworkConnection(ObservableObject):
    """
    A network connection is a connection (completed or attempted) across a digital network (a group of two or more
    computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NetworkConnection"]
    class_class_curie: ClassVar[str] = "uco-observable:NetworkConnection"
    class_name: ClassVar[str] = "NetworkConnection"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NetworkConnection

    id: Union[str, NetworkConnectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NetworkConnectionId):
            self.id = NetworkConnectionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class HTTPConnection(NetworkConnection):
    """
    An HTTP connection is network connection that is conformant to the Hypertext Transfer Protocol (HTTP) standard.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["HTTPConnection"]
    class_class_curie: ClassVar[str] = "uco-observable:HTTPConnection"
    class_name: ClassVar[str] = "HTTPConnection"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.HTTPConnection

    id: Union[str, HTTPConnectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HTTPConnectionId):
            self.id = HTTPConnectionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ICMPConnection(NetworkConnection):
    """
    An ICMP connection is a network connection that is conformant to the Internet Control Message Protocol (ICMP)
    standard.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ICMPConnection"]
    class_class_curie: ClassVar[str] = "uco-observable:ICMPConnection"
    class_name: ClassVar[str] = "ICMPConnection"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ICMPConnection

    id: Union[str, ICMPConnectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ICMPConnectionId):
            self.id = ICMPConnectionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NetworkFlow(ObservableObject):
    """
    A network flow is a sequence of data transiting one or more digital network (a group or two or more computer
    systems linked together) connections. [based on https://www.webopedia.com/TERM/N/network.html]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NetworkFlow"]
    class_class_curie: ClassVar[str] = "uco-observable:NetworkFlow"
    class_name: ClassVar[str] = "NetworkFlow"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NetworkFlow

    id: Union[str, NetworkFlowId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NetworkFlowId):
            self.id = NetworkFlowId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NetworkInterface(ObservableObject):
    """
    A network interface is a software or hardware interface between two pieces of equipment or protocol layers in a
    computer network.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NetworkInterface"]
    class_class_curie: ClassVar[str] = "uco-observable:NetworkInterface"
    class_name: ClassVar[str] = "NetworkInterface"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NetworkInterface

    id: Union[str, NetworkInterfaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NetworkInterfaceId):
            self.id = NetworkInterfaceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NetworkProtocol(ObservableObject):
    """
    A network protocol is an established set of structured rules that determine how data is transmitted between
    different devices in the same network. Essentially, it allows connected devices to communicate with each other,
    regardless of any differences in their internal processes, structure or design. [based on
    https://www.comptia.org/content/guides/what-is-a-network-protocol]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NetworkProtocol"]
    class_class_curie: ClassVar[str] = "uco-observable:NetworkProtocol"
    class_name: ClassVar[str] = "NetworkProtocol"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NetworkProtocol

    id: Union[str, NetworkProtocolId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NetworkProtocolId):
            self.id = NetworkProtocolId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NetworkRoute(ObservableObject):
    """
    A network route is a specific path (of specific network nodes, connections and protocols) for traffic in a network
    or between or across multiple networks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NetworkRoute"]
    class_class_curie: ClassVar[str] = "uco-observable:NetworkRoute"
    class_name: ClassVar[str] = "NetworkRoute"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NetworkRoute

    id: Union[str, NetworkRouteId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NetworkRouteId):
            self.id = NetworkRouteId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class NetworkSubnet(ObservableObject):
    """
    A network subnet is a logical subdivision of an IP network. [based on https://en.wikipedia.org/wiki/Subnetwork]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["NetworkSubnet"]
    class_class_curie: ClassVar[str] = "uco-observable:NetworkSubnet"
    class_name: ClassVar[str] = "NetworkSubnet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.NetworkSubnet

    id: Union[str, NetworkSubnetId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NetworkSubnetId):
            self.id = NetworkSubnetId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Note(ObservableObject):
    """
    A note is a brief textual record.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Note"]
    class_class_curie: ClassVar[str] = "uco-observable:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Note

    id: Union[str, NoteId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoteId):
            self.id = NoteId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ObservablePattern(Observable):
    """
    An observable pattern is a grouping of characteristics unique to a logical pattern composed of observable object
    and observable action properties.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ObservablePattern"]
    class_class_curie: ClassVar[str] = "uco-observable:ObservablePattern"
    class_name: ClassVar[str] = "ObservablePattern"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ObservablePattern

    id: Union[str, ObservablePatternId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservablePatternId):
            self.id = ObservablePatternId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ObservableRelationship(Observable):
    """
    An observable relationship is a grouping of characteristics unique to an assertion of an association between two
    observable objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ObservableRelationship"]
    class_class_curie: ClassVar[str] = "uco-observable:ObservableRelationship"
    class_name: ClassVar[str] = "ObservableRelationship"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ObservableRelationship

    id: Union[str, ObservableRelationshipId] = None
    isDirectional: Union[bool, Bool] = None
    source: Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]] = None
    target: Union[str, UcoObjectId] = None
    type: Optional[Union[str, URIorCURIE]] = None
    createdBy: Optional[Union[str, IdentityAbstractionId]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    externalReference: Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]] = empty_list()
    hasFacet: Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    objectMarking: Optional[Union[Union[str, MarkingDefinitionAbstractionId], list[Union[str, MarkingDefinitionAbstractionId]]]] = empty_list()
    objectStatus: Optional[Union[str, "ObjectStatusVocab"]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, list[str]]] = empty_list()
    endTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    kindOfRelationship: Optional[str] = None
    startTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservableRelationshipId):
            self.id = ObservableRelationshipId(self.id)

        if self._is_empty(self.isDirectional):
            self.MissingRequiredField("isDirectional")
        if not isinstance(self.isDirectional, Bool):
            self.isDirectional = Bool(self.isDirectional)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, UcoObjectId) else UcoObjectId(v) for v in self.source]

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, UcoObjectId):
            self.target = UcoObjectId(self.target)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.createdBy is not None and not isinstance(self.createdBy, IdentityAbstractionId):
            self.createdBy = IdentityAbstractionId(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, ExternalReference) else ExternalReference(**as_dict(v)) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, Facet) else Facet(**as_dict(v)) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstractionId) else MarkingDefinitionAbstractionId(v) for v in self.objectMarking]

        if self.objectStatus is not None and not isinstance(self.objectStatus, ObjectStatusVocab):
            self.objectStatus = ObjectStatusVocab(self.objectStatus)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        if not isinstance(self.endTime, list):
            self.endTime = [self.endTime] if self.endTime is not None else []
        self.endTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.endTime]

        if self.kindOfRelationship is not None and not isinstance(self.kindOfRelationship, str):
            self.kindOfRelationship = str(self.kindOfRelationship)

        if not isinstance(self.startTime, list):
            self.startTime = [self.startTime] if self.startTime is not None else []
        self.startTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.startTime]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Observation(Action):
    """
    An observation is a temporal perception of an observable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Observation"]
    class_class_curie: ClassVar[str] = "uco-observable:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Observation

    id: Union[str, ObservationId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservationId):
            self.id = ObservationId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class OnlineService(ObservableObject):
    """
    An online service is a particular provision mechanism of information access, distribution or manipulation over the
    Internet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["OnlineService"]
    class_class_curie: ClassVar[str] = "uco-observable:OnlineService"
    class_name: ClassVar[str] = "OnlineService"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.OnlineService

    id: Union[str, OnlineServiceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OnlineServiceId):
            self.id = OnlineServiceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class OnlineServiceFacet(Facet):
    """
    An online service facet is a grouping of characteristics unique to a particular provision mechanism of information
    access, distribution or manipulation over the Internet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["OnlineServiceFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:OnlineServiceFacet"
    class_name: ClassVar[str] = "OnlineServiceFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.OnlineServiceFacet

    inetLocation: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    name: Optional[str] = None
    observable_location: Optional[Union[Union[str, LocationId], list[Union[str, LocationId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.inetLocation, list):
            self.inetLocation = [self.inetLocation] if self.inetLocation is not None else []
        self.inetLocation = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.inetLocation]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.observable_location, list):
            self.observable_location = [self.observable_location] if self.observable_location is not None else []
        self.observable_location = [v if isinstance(v, LocationId) else LocationId(v) for v in self.observable_location]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class OperatingSystem(ObservableObject):
    """
    An operating system is the software that manages computer hardware, software resources, and provides common
    services for computer programs. [based on https://en.wikipedia.org/wiki/Operating_system]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["OperatingSystem"]
    class_class_curie: ClassVar[str] = "uco-observable:OperatingSystem"
    class_name: ClassVar[str] = "OperatingSystem"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.OperatingSystem

    id: Union[str, OperatingSystemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperatingSystemId):
            self.id = OperatingSystemId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class OperatingSystemFacet(Facet):
    """
    An operating system facet is a grouping of characteristics unique to the software that manages computer hardware,
    software resources, and provides common services for computer programs. [based on
    https://en.wikipedia.org/wiki/Operating_system]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["OperatingSystemFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:OperatingSystemFacet"
    class_name: ClassVar[str] = "OperatingSystemFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.OperatingSystemFacet

    advertisingID: Optional[Union[str, list[str]]] = empty_list()
    bitness: Optional[str] = None
    environmentVariables: Optional[Union[dict, Dictionary]] = None
    installDate: Optional[Union[str, XSDDateTime]] = None
    isLimitAdTrackingEnabled: Optional[Union[bool, Bool]] = None
    manufacturer: Optional[Union[str, IdentityId]] = None
    observable_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.advertisingID, list):
            self.advertisingID = [self.advertisingID] if self.advertisingID is not None else []
        self.advertisingID = [v if isinstance(v, str) else str(v) for v in self.advertisingID]

        if self.bitness is not None and not isinstance(self.bitness, str):
            self.bitness = str(self.bitness)

        if self.environmentVariables is not None and not isinstance(self.environmentVariables, Dictionary):
            self.environmentVariables = Dictionary(**as_dict(self.environmentVariables))

        if self.installDate is not None and not isinstance(self.installDate, XSDDateTime):
            self.installDate = XSDDateTime(self.installDate)

        if self.isLimitAdTrackingEnabled is not None and not isinstance(self.isLimitAdTrackingEnabled, Bool):
            self.isLimitAdTrackingEnabled = Bool(self.isLimitAdTrackingEnabled)

        if self.manufacturer is not None and not isinstance(self.manufacturer, IdentityId):
            self.manufacturer = IdentityId(self.manufacturer)

        if self.observable_version is not None and not isinstance(self.observable_version, str):
            self.observable_version = str(self.observable_version)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class PDFFile(File):
    """
    A PDF file is a Portable Document Format (PDF) file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["PDFFile"]
    class_class_curie: ClassVar[str] = "uco-observable:PDFFile"
    class_name: ClassVar[str] = "PDFFile"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.PDFFile

    id: Union[str, PDFFileId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PDFFileId):
            self.id = PDFFileId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class PDFFileFacet(Facet):
    """
    A PDF file facet is a grouping of characteristics unique to a PDF (Portable Document Format) file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["PDFFileFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:PDFFileFacet"
    class_name: ClassVar[str] = "PDFFileFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.PDFFileFacet

    documentInformationDictionary: Optional[Union[dict, ControlledDictionary]] = None
    isOptimized: Optional[Union[bool, Bool]] = None
    observable_version: Optional[str] = None
    pdfCreationDate: Optional[Union[str, XSDDateTime]] = None
    pdfId0: Optional[Union[str, list[str]]] = empty_list()
    pdfId1: Optional[str] = None
    pdfModDate: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.documentInformationDictionary is not None and not isinstance(self.documentInformationDictionary, ControlledDictionary):
            self.documentInformationDictionary = ControlledDictionary(**as_dict(self.documentInformationDictionary))

        if self.isOptimized is not None and not isinstance(self.isOptimized, Bool):
            self.isOptimized = Bool(self.isOptimized)

        if self.observable_version is not None and not isinstance(self.observable_version, str):
            self.observable_version = str(self.observable_version)

        if self.pdfCreationDate is not None and not isinstance(self.pdfCreationDate, XSDDateTime):
            self.pdfCreationDate = XSDDateTime(self.pdfCreationDate)

        if not isinstance(self.pdfId0, list):
            self.pdfId0 = [self.pdfId0] if self.pdfId0 is not None else []
        self.pdfId0 = [v if isinstance(v, str) else str(v) for v in self.pdfId0]

        if self.pdfId1 is not None and not isinstance(self.pdfId1, str):
            self.pdfId1 = str(self.pdfId1)

        if self.pdfModDate is not None and not isinstance(self.pdfModDate, XSDDateTime):
            self.pdfModDate = XSDDateTime(self.pdfModDate)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class PathRelationFacet(Facet):
    """
    A path relation facet is a grouping of characteristics unique to the location of one object within another
    containing object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["PathRelationFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:PathRelationFacet"
    class_name: ClassVar[str] = "PathRelationFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.PathRelationFacet

    path: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.path, list):
            self.path = [self.path] if self.path is not None else []
        self.path = [v if isinstance(v, str) else str(v) for v in self.path]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class PaymentCard(ObservableObject):
    """
    A payment card is a physical token that is part of a payment system issued by financial institutions, such as a
    bank, to a customer that enables its owner (the cardholder) to access the funds in the customer's designated bank
    accounts, or through a credit account and make payments by electronic funds transfer and access automated teller
    machines (ATMs). [based on https://en.wikipedia.org/wiki/Payment_card]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["PaymentCard"]
    class_class_curie: ClassVar[str] = "uco-observable:PaymentCard"
    class_name: ClassVar[str] = "PaymentCard"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.PaymentCard

    id: Union[str, PaymentCardId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PaymentCardId):
            self.id = PaymentCardId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class PhoneAccount(DigitalAccount):
    """
    A phone account is an arrangement with an entity to enable and control the provision of a telephony capability or
    service.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["PhoneAccount"]
    class_class_curie: ClassVar[str] = "uco-observable:PhoneAccount"
    class_name: ClassVar[str] = "PhoneAccount"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.PhoneAccount

    id: Union[str, PhoneAccountId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhoneAccountId):
            self.id = PhoneAccountId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class PhoneAccountFacet(Facet):
    """
    A phone account facet is a grouping of characteristics unique to an arrangement with an entity to enable and
    control the provision of a telephony capability or service.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["PhoneAccountFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:PhoneAccountFacet"
    class_name: ClassVar[str] = "PhoneAccountFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.PhoneAccountFacet

    phoneNumber: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.phoneNumber is not None and not isinstance(self.phoneNumber, str):
            self.phoneNumber = str(self.phoneNumber)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Pipe(ObservableObject):
    """
    A pipe is a mechanism for one-way inter-process communication using message passing where data written by one
    process is buffered by the operating system until it is read by the next process, and this uni-directional channel
    disappears when the processes are completed. [based on https://en.wikipedia.org/wiki/Pipeline_(Unix) ;
    https://en.wikipedia.org/wiki/Anonymous_pipe]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Pipe"]
    class_class_curie: ClassVar[str] = "uco-observable:Pipe"
    class_name: ClassVar[str] = "Pipe"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Pipe

    id: Union[str, PipeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PipeId):
            self.id = PipeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Post(Message):
    """
    A post is message submitted to an online discussion/publishing site (forum, blog, etc.).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Post"]
    class_class_curie: ClassVar[str] = "uco-observable:Post"
    class_name: ClassVar[str] = "Post"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Post

    id: Union[str, PostId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostId):
            self.id = PostId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Process(ObservableObject):
    """
    A process is an instance of a computer program executed on an operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Process"]
    class_class_curie: ClassVar[str] = "uco-observable:Process"
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Process

    id: Union[str, ProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessId):
            self.id = ProcessId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ProcessFacet(Facet):
    """
    A process facet is a grouping of characteristics unique to an instance of a computer program executed on an
    operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ProcessFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ProcessFacet"
    class_name: ClassVar[str] = "ProcessFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ProcessFacet

    arguments: Optional[Union[str, list[str]]] = empty_list()
    binary: Optional[Union[str, ObservableObjectId]] = None
    creatorUser: Optional[Union[str, ObservableObjectId]] = None
    currentWorkingDirectory: Optional[str] = None
    environmentVariables: Optional[Union[dict, Dictionary]] = None
    exitStatus: Optional[int] = None
    exitTime: Optional[Union[str, XSDDateTime]] = None
    isHidden: Optional[Union[bool, Bool]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    parent: Optional[Union[str, ObservableObjectId]] = None
    pid: Optional[int] = None
    status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.arguments, list):
            self.arguments = [self.arguments] if self.arguments is not None else []
        self.arguments = [v if isinstance(v, str) else str(v) for v in self.arguments]

        if self.binary is not None and not isinstance(self.binary, ObservableObjectId):
            self.binary = ObservableObjectId(self.binary)

        if self.creatorUser is not None and not isinstance(self.creatorUser, ObservableObjectId):
            self.creatorUser = ObservableObjectId(self.creatorUser)

        if self.currentWorkingDirectory is not None and not isinstance(self.currentWorkingDirectory, str):
            self.currentWorkingDirectory = str(self.currentWorkingDirectory)

        if self.environmentVariables is not None and not isinstance(self.environmentVariables, Dictionary):
            self.environmentVariables = Dictionary(**as_dict(self.environmentVariables))

        if self.exitStatus is not None and not isinstance(self.exitStatus, int):
            self.exitStatus = int(self.exitStatus)

        if self.exitTime is not None and not isinstance(self.exitTime, XSDDateTime):
            self.exitTime = XSDDateTime(self.exitTime)

        if self.isHidden is not None and not isinstance(self.isHidden, Bool):
            self.isHidden = Bool(self.isHidden)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.parent is not None and not isinstance(self.parent, ObservableObjectId):
            self.parent = ObservableObjectId(self.parent)

        if self.pid is not None and not isinstance(self.pid, int):
            self.pid = int(self.pid)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ProcessThread(ObservableObject):
    """
    A process thread is the smallest sequence of programmed instructions that can be managed independently by a
    scheduler on a computer, which is typically a part of the operating system. It is a component of a process.
    Multiple threads can exist within one process, executing concurrently and sharing resources such as memory, while
    different processes do not share these resources. In particular, the threads of a process share its executable
    code and the values of its dynamically allocated variables and non-thread-local global variables at any given
    time. [based on https://en.wikipedia.org/wiki/Thread_(computing)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ProcessThread"]
    class_class_curie: ClassVar[str] = "uco-observable:ProcessThread"
    class_name: ClassVar[str] = "ProcessThread"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ProcessThread

    id: Union[str, ProcessThreadId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessThreadId):
            self.id = ProcessThreadId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Profile(ObservableObject):
    """
    A profile is an explicit digital representation of identity and characteristics of the owner of a single user
    account associated with an online service or application. [based on https://en.wikipedia.org/wiki/User_profile]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Profile"]
    class_class_curie: ClassVar[str] = "uco-observable:Profile"
    class_name: ClassVar[str] = "Profile"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Profile

    id: Union[str, ProfileId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProfileId):
            self.id = ProfileId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ProfileFacet(Facet):
    """
    A profile facet is a grouping of characteristics unique to an explicit digital representation of identity and
    characteristics of the owner of a single user account associated with an online service or application. [based on
    https://en.wikipedia.org/wiki/User_profile]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ProfileFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ProfileFacet"
    class_name: ClassVar[str] = "ProfileFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ProfileFacet

    contactAddress: Optional[Union[dict, ContactAddress]] = None
    contactEmail: Optional[Union[dict, ContactEmail]] = None
    contactMessaging: Optional[Union[dict, ContactMessaging]] = None
    contactPhone: Optional[Union[dict, ContactPhone]] = None
    contactURL: Optional[Union[dict, ContactURL]] = None
    displayName: Optional[str] = None
    name: Optional[str] = None
    profileAccount: Optional[Union[str, ObservableObjectId]] = None
    profileCreated: Optional[Union[str, XSDDateTime]] = None
    profileIdentity: Optional[Union[str, IdentityId]] = None
    profileLanguage: Optional[Union[str, list[str]]] = empty_list()
    profileService: Optional[Union[str, ObservableObjectId]] = None
    profileWebsite: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contactAddress is not None and not isinstance(self.contactAddress, ContactAddress):
            self.contactAddress = ContactAddress(**as_dict(self.contactAddress))

        if self.contactEmail is not None and not isinstance(self.contactEmail, ContactEmail):
            self.contactEmail = ContactEmail(**as_dict(self.contactEmail))

        if self.contactMessaging is not None and not isinstance(self.contactMessaging, ContactMessaging):
            self.contactMessaging = ContactMessaging(**as_dict(self.contactMessaging))

        if self.contactPhone is not None and not isinstance(self.contactPhone, ContactPhone):
            self.contactPhone = ContactPhone(**as_dict(self.contactPhone))

        if self.contactURL is not None and not isinstance(self.contactURL, ContactURL):
            self.contactURL = ContactURL(**as_dict(self.contactURL))

        if self.displayName is not None and not isinstance(self.displayName, str):
            self.displayName = str(self.displayName)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.profileAccount is not None and not isinstance(self.profileAccount, ObservableObjectId):
            self.profileAccount = ObservableObjectId(self.profileAccount)

        if self.profileCreated is not None and not isinstance(self.profileCreated, XSDDateTime):
            self.profileCreated = XSDDateTime(self.profileCreated)

        if self.profileIdentity is not None and not isinstance(self.profileIdentity, IdentityId):
            self.profileIdentity = IdentityId(self.profileIdentity)

        if not isinstance(self.profileLanguage, list):
            self.profileLanguage = [self.profileLanguage] if self.profileLanguage is not None else []
        self.profileLanguage = [v if isinstance(v, str) else str(v) for v in self.profileLanguage]

        if self.profileService is not None and not isinstance(self.profileService, ObservableObjectId):
            self.profileService = ObservableObjectId(self.profileService)

        if self.profileWebsite is not None and not isinstance(self.profileWebsite, ObservableObjectId):
            self.profileWebsite = ObservableObjectId(self.profileWebsite)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class PropertiesEnumeratedEffectFacet(DefinedEffectFacet):
    """
    A properties enumerated effect facet is a grouping of characteristics unique to the effects of actions upon
    observable objects where a characteristic of the observable object is enumerated. An example of this would be
    startup parameters for a process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["PropertiesEnumeratedEffectFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:PropertiesEnumeratedEffectFacet"
    class_name: ClassVar[str] = "PropertiesEnumeratedEffectFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.PropertiesEnumeratedEffectFacet

    properties: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.properties is not None and not isinstance(self.properties, str):
            self.properties = str(self.properties)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class PropertyReadEffectFacet(DefinedEffectFacet):
    """
    A properties read effect facet is a grouping of characteristics unique to the effects of actions upon observable
    objects where a characteristic is read from an observable object. An example of this would be the current running
    state of a process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["PropertyReadEffectFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:PropertyReadEffectFacet"
    class_name: ClassVar[str] = "PropertyReadEffectFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.PropertyReadEffectFacet

    observable_value: Optional[str] = None
    propertyName: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.observable_value is not None and not isinstance(self.observable_value, str):
            self.observable_value = str(self.observable_value)

        if self.propertyName is not None and not isinstance(self.propertyName, str):
            self.propertyName = str(self.propertyName)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ProtocolConverter(Device):
    """
    A protocol converter is a device that converts from one protocol to another (e.g. SD to USB, SATA to USB, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ProtocolConverter"]
    class_class_curie: ClassVar[str] = "uco-observable:ProtocolConverter"
    class_name: ClassVar[str] = "ProtocolConverter"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ProtocolConverter

    id: Union[str, ProtocolConverterId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProtocolConverterId):
            self.id = ProtocolConverterId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class RasterPicture(File):
    """
    A raster picture is a raster (or bitmap) image.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["RasterPicture"]
    class_class_curie: ClassVar[str] = "uco-observable:RasterPicture"
    class_name: ClassVar[str] = "RasterPicture"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.RasterPicture

    id: Union[str, RasterPictureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RasterPictureId):
            self.id = RasterPictureId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class RasterPictureFacet(Facet):
    """
    A raster picture facet is a grouping of characteristics unique to a raster (or bitmap) image.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["RasterPictureFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:RasterPictureFacet"
    class_name: ClassVar[str] = "RasterPictureFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.RasterPictureFacet

    bitsPerPixel: Optional[int] = None
    camera: Optional[Union[str, ObservableObjectId]] = None
    imageCompressionMethod: Optional[str] = None
    pictureHeight: Optional[int] = None
    pictureType: Optional[str] = None
    pictureWidth: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.bitsPerPixel is not None and not isinstance(self.bitsPerPixel, int):
            self.bitsPerPixel = int(self.bitsPerPixel)

        if self.camera is not None and not isinstance(self.camera, ObservableObjectId):
            self.camera = ObservableObjectId(self.camera)

        if self.imageCompressionMethod is not None and not isinstance(self.imageCompressionMethod, str):
            self.imageCompressionMethod = str(self.imageCompressionMethod)

        if self.pictureHeight is not None and not isinstance(self.pictureHeight, int):
            self.pictureHeight = int(self.pictureHeight)

        if self.pictureType is not None and not isinstance(self.pictureType, str):
            self.pictureType = str(self.pictureType)

        if self.pictureWidth is not None and not isinstance(self.pictureWidth, int):
            self.pictureWidth = int(self.pictureWidth)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class RecoveredObject(ObservableObject):
    """
    An observable object that was the result of a recovery operation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["RecoveredObject"]
    class_class_curie: ClassVar[str] = "uco-observable:RecoveredObject"
    class_name: ClassVar[str] = "RecoveredObject"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.RecoveredObject

    id: Union[str, RecoveredObjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecoveredObjectId):
            self.id = RecoveredObjectId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class RecoveredObjectFacet(Facet):
    """
    Recoverability status of name, metadata, and content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["RecoveredObjectFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:RecoveredObjectFacet"
    class_name: ClassVar[str] = "RecoveredObjectFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.RecoveredObjectFacet

    contentRecoveredStatus: Optional[Union[str, "RecoveredObjectStatusVocab"]] = None
    metadataRecoveredStatus: Optional[Union[str, "RecoveredObjectStatusVocab"]] = None
    nameRecoveredStatus: Optional[Union[str, "RecoveredObjectStatusVocab"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contentRecoveredStatus is not None and not isinstance(self.contentRecoveredStatus, (RecoveredObjectStatusVocab, str)):
            value = self.contentRecoveredStatus
            for _coerce in (lambda: RecoveredObjectStatusVocab(value), lambda: str(value)):
                try:
                    self.contentRecoveredStatus = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[RecoveredObjectStatusVocab, str] could be constructed from {value!r} for slot contentRecoveredStatus")

        if self.metadataRecoveredStatus is not None and not isinstance(self.metadataRecoveredStatus, (RecoveredObjectStatusVocab, str)):
            value = self.metadataRecoveredStatus
            for _coerce in (lambda: RecoveredObjectStatusVocab(value), lambda: str(value)):
                try:
                    self.metadataRecoveredStatus = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[RecoveredObjectStatusVocab, str] could be constructed from {value!r} for slot metadataRecoveredStatus")

        if self.nameRecoveredStatus is not None and not isinstance(self.nameRecoveredStatus, (RecoveredObjectStatusVocab, str)):
            value = self.nameRecoveredStatus
            for _coerce in (lambda: RecoveredObjectStatusVocab(value), lambda: str(value)):
                try:
                    self.nameRecoveredStatus = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[RecoveredObjectStatusVocab, str] could be constructed from {value!r} for slot nameRecoveredStatus")

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ReparsePoint(FileSystemObject):
    """
    A reparse point is a type of NTFS (New Technology File System) object which is an optional attribute of files and
    directories meant to define some sort of preprocessing before accessing the said file or directory. For instance
    reparse points can be used to redirect access to files which have been moved to long term storage so that some
    application would retrieve them and make them directly accessible. A reparse point contains a reparse tag and data
    that are interpreted by a filesystem filter identified by the tag. [based on
    https://jp-andre.pagesperso-orange.fr/junctions.html ; https://en.wikipedia.org/wiki/NTFS_reparse_point]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ReparsePoint"]
    class_class_curie: ClassVar[str] = "uco-observable:ReparsePoint"
    class_name: ClassVar[str] = "ReparsePoint"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ReparsePoint

    id: Union[str, ReparsePointId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReparsePointId):
            self.id = ReparsePointId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SIMCard(Device):
    """
    A SIM card is a subscriber identification module card intended to securely store the international mobile
    subscriber identity (IMSI) number and its related key, which are used to identify and authenticate subscribers on
    mobile telephony. [based on https://en.wikipedia.org/wiki/SIM_card]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SIMCard"]
    class_class_curie: ClassVar[str] = "uco-observable:SIMCard"
    class_name: ClassVar[str] = "SIMCard"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SIMCard

    id: Union[str, SIMCardId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SIMCardId):
            self.id = SIMCardId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SIMCardFacet(Facet):
    """
    A SIM card facet is a grouping of characteristics unique to a subscriber identification module card intended to
    securely store the international mobile subscriber identity (IMSI) number and its related key, which are used to
    identify and authenticate subscribers on mobile telephony devices (such as mobile phones and computers). [based on
    https://en.wikipedia.org/wiki/SIM_card]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SIMCardFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:SIMCardFacet"
    class_name: ClassVar[str] = "SIMCardFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SIMCardFacet

    ICCID: Optional[str] = None
    IMSI: Optional[str] = None
    PIN: Optional[str] = None
    PUK: Optional[str] = None
    SIMForm: Optional[str] = None
    SIMType: Optional[str] = None
    carrier: Optional[Union[str, IdentityId]] = None
    storageCapacityInBytes: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ICCID is not None and not isinstance(self.ICCID, str):
            self.ICCID = str(self.ICCID)

        if self.IMSI is not None and not isinstance(self.IMSI, str):
            self.IMSI = str(self.IMSI)

        if self.PIN is not None and not isinstance(self.PIN, str):
            self.PIN = str(self.PIN)

        if self.PUK is not None and not isinstance(self.PUK, str):
            self.PUK = str(self.PUK)

        if self.SIMForm is not None and not isinstance(self.SIMForm, str):
            self.SIMForm = str(self.SIMForm)

        if self.SIMType is not None and not isinstance(self.SIMType, str):
            self.SIMType = str(self.SIMType)

        if self.carrier is not None and not isinstance(self.carrier, IdentityId):
            self.carrier = IdentityId(self.carrier)

        if self.storageCapacityInBytes is not None and not isinstance(self.storageCapacityInBytes, int):
            self.storageCapacityInBytes = int(self.storageCapacityInBytes)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SIPAddress(DigitalAddress):
    """
    A SIP address is an identifier for Session Initiation Protocol (SIP) communication.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SIPAddress"]
    class_class_curie: ClassVar[str] = "uco-observable:SIPAddress"
    class_name: ClassVar[str] = "SIPAddress"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SIPAddress

    id: Union[str, SIPAddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SIPAddressId):
            self.id = SIPAddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class SIPAddressFacet(DigitalAddressFacet):
    """
    A SIP address facet is a grouping of characteristics unique to a Session Initiation Protocol (SIP) standards
    conformant identifier assigned to a user to enable routing and management of SIP standards conformant
    communication to or from that user loosely coupled from any particular devices.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SIPAddressFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:SIPAddressFacet"
    class_name: ClassVar[str] = "SIPAddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SIPAddressFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SMSMessage(Message):
    """
    An SMS message is a message conformant to the short message service (SMS) communication protocol standards.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SMSMessage"]
    class_class_curie: ClassVar[str] = "uco-observable:SMSMessage"
    class_name: ClassVar[str] = "SMSMessage"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SMSMessage

    id: Union[str, SMSMessageId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SMSMessageId):
            self.id = SMSMessageId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SMSMessageFacet(Facet):
    """
    A SMS message facet is a grouping of characteristics unique to a message conformant to the short message service
    (SMS) communication protocol standards.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SMSMessageFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:SMSMessageFacet"
    class_name: ClassVar[str] = "SMSMessageFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SMSMessageFacet

    isRead: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.isRead is not None and not isinstance(self.isRead, Bool):
            self.isRead = Bool(self.isRead)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SQLiteBlob(ObservableObject):
    """
    An SQLite blob is a blob (binary large object) of data within an SQLite database. [based on
    https://en.wikipedia.org/wiki/SQLite]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SQLiteBlob"]
    class_class_curie: ClassVar[str] = "uco-observable:SQLiteBlob"
    class_name: ClassVar[str] = "SQLiteBlob"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SQLiteBlob

    id: Union[str, SQLiteBlobId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SQLiteBlobId):
            self.id = SQLiteBlobId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SQLiteBlobFacet(Facet):
    """
    An SQLite blob facet is a grouping of characteristics unique to a blob (binary large object) of data within an
    SQLite database. [based on https://en.wikipedia.org/wiki/SQLite]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SQLiteBlobFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:SQLiteBlobFacet"
    class_name: ClassVar[str] = "SQLiteBlobFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SQLiteBlobFacet

    columnName: Optional[str] = None
    rowCondition: Optional[str] = None
    rowIndex: Optional[Union[Union[int, UcoPositiveInteger], list[Union[int, UcoPositiveInteger]]]] = empty_list()
    tableName: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.columnName is not None and not isinstance(self.columnName, str):
            self.columnName = str(self.columnName)

        if self.rowCondition is not None and not isinstance(self.rowCondition, str):
            self.rowCondition = str(self.rowCondition)

        if not isinstance(self.rowIndex, list):
            self.rowIndex = [self.rowIndex] if self.rowIndex is not None else []
        self.rowIndex = [v if isinstance(v, UcoPositiveInteger) else UcoPositiveInteger(v) for v in self.rowIndex]

        if self.tableName is not None and not isinstance(self.tableName, str):
            self.tableName = str(self.tableName)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SecurityAppliance(Appliance):
    """
    A security appliance is a purpose-built computer with software or firmware that is designed to provide a specific
    security function to protect computer networks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SecurityAppliance"]
    class_class_curie: ClassVar[str] = "uco-observable:SecurityAppliance"
    class_name: ClassVar[str] = "SecurityAppliance"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SecurityAppliance

    id: Union[str, SecurityApplianceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecurityApplianceId):
            self.id = SecurityApplianceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Semaphore(ObservableObject):
    """
    A semaphore is a variable or abstract data type used to control access to a common resource by multiple processes
    and avoid critical section problems in a concurrent system such as a multitasking operating system. [based on
    https://en.wikipedia.org/wiki/Semaphore_(programming)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Semaphore"]
    class_class_curie: ClassVar[str] = "uco-observable:Semaphore"
    class_name: ClassVar[str] = "Semaphore"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Semaphore

    id: Union[str, SemaphoreId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SemaphoreId):
            self.id = SemaphoreId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SendControlCodeEffectFacet(DefinedEffectFacet):
    """
    A send control code effect facet is a grouping of characteristics unique to the effects of actions upon observable
    objects where a control code, or other control-oriented communication signal, is sent to the observable object. An
    example of this would be an action sending a control code changing the running state of a process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SendControlCodeEffectFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:SendControlCodeEffectFacet"
    class_name: ClassVar[str] = "SendControlCodeEffectFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SendControlCodeEffectFacet

    controlCode: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.controlCode is not None and not isinstance(self.controlCode, str):
            self.controlCode = str(self.controlCode)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Server(Computer):
    """
    A server is a server rack-mount based computer, minicomputer, supercomputer, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Server"]
    class_class_curie: ClassVar[str] = "uco-observable:Server"
    class_name: ClassVar[str] = "Server"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Server

    id: Union[str, ServerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServerId):
            self.id = ServerId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ShopListing(ObservableObject):
    """
    A shop listing is a listing of offered products on an online marketplace/shop.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ShopListing"]
    class_class_curie: ClassVar[str] = "uco-observable:ShopListing"
    class_name: ClassVar[str] = "ShopListing"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ShopListing

    id: Union[str, ShopListingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ShopListingId):
            self.id = ShopListingId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SmartDevice(Device):
    """
    A smart device is a microprocessor IoT device that is expected to be connected directly to cloud-based networks or
    via smartphone
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SmartDevice"]
    class_class_curie: ClassVar[str] = "uco-observable:SmartDevice"
    class_name: ClassVar[str] = "SmartDevice"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SmartDevice

    id: Union[str, SmartDeviceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SmartDeviceId):
            self.id = SmartDeviceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SmartPhone(MobilePhone):
    """
    A smartphone is a portable device that combines mobile telephone and computing functions into one unit. Examples
    include iPhone, Samsung Galaxy, Huawei, Blackberry. (Inferred by model and OperatingSystemFacet)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SmartPhone"]
    class_class_curie: ClassVar[str] = "uco-observable:SmartPhone"
    class_name: ClassVar[str] = "SmartPhone"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SmartPhone

    id: Union[str, SmartPhoneId] = None
    type: Optional[Union[str, URIorCURIE]] = None
    createdBy: Optional[Union[str, IdentityAbstractionId]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    externalReference: Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]] = empty_list()
    hasFacet: Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    objectMarking: Optional[Union[Union[str, MarkingDefinitionAbstractionId], list[Union[str, MarkingDefinitionAbstractionId]]]] = empty_list()
    objectStatus: Optional[Union[str, "ObjectStatusVocab"]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, list[str]]] = empty_list()
    hasChanged: Optional[Union[bool, Bool]] = None
    state: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SmartPhoneId):
            self.id = SmartPhoneId(self.id)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.createdBy is not None and not isinstance(self.createdBy, IdentityAbstractionId):
            self.createdBy = IdentityAbstractionId(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, ExternalReference) else ExternalReference(**as_dict(v)) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, Facet) else Facet(**as_dict(v)) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstractionId) else MarkingDefinitionAbstractionId(v) for v in self.objectMarking]

        if self.objectStatus is not None and not isinstance(self.objectStatus, ObjectStatusVocab):
            self.objectStatus = ObjectStatusVocab(self.objectStatus)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        if self.hasChanged is not None and not isinstance(self.hasChanged, Bool):
            self.hasChanged = Bool(self.hasChanged)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)


            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class AndroidPhone(SmartPhone):
    """
    An android phone is a smart phone that applies the Android mobile operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["AndroidPhone"]
    class_class_curie: ClassVar[str] = "uco-observable:AndroidPhone"
    class_name: ClassVar[str] = "AndroidPhone"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.AndroidPhone

    id: Union[str, AndroidPhoneId] = None
    type: Optional[Union[str, URIorCURIE]] = None
    createdBy: Optional[Union[str, IdentityAbstractionId]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    externalReference: Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]] = empty_list()
    hasFacet: Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    objectMarking: Optional[Union[Union[str, MarkingDefinitionAbstractionId], list[Union[str, MarkingDefinitionAbstractionId]]]] = empty_list()
    objectStatus: Optional[Union[str, "ObjectStatusVocab"]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, list[str]]] = empty_list()
    hasChanged: Optional[Union[bool, Bool]] = None
    state: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AndroidPhoneId):
            self.id = AndroidPhoneId(self.id)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.createdBy is not None and not isinstance(self.createdBy, IdentityAbstractionId):
            self.createdBy = IdentityAbstractionId(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, ExternalReference) else ExternalReference(**as_dict(v)) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, Facet) else Facet(**as_dict(v)) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstractionId) else MarkingDefinitionAbstractionId(v) for v in self.objectMarking]

        if self.objectStatus is not None and not isinstance(self.objectStatus, ObjectStatusVocab):
            self.objectStatus = ObjectStatusVocab(self.objectStatus)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        if self.hasChanged is not None and not isinstance(self.hasChanged, Bool):
            self.hasChanged = Bool(self.hasChanged)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BlackberryPhone(SmartPhone):
    """
    A blackberry phone is a smart phone that applies the Blackberry OS mobile operating system. (Blackberry 10
    re-introduces Blackberry OS, prior to that the OS was Android.)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["BlackberryPhone"]
    class_class_curie: ClassVar[str] = "uco-observable:BlackberryPhone"
    class_name: ClassVar[str] = "BlackberryPhone"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.BlackberryPhone

    id: Union[str, BlackberryPhoneId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BlackberryPhoneId):
            self.id = BlackberryPhoneId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class IPhone(SmartPhone):
    """
    An iPhone is a smart phone that applies the iOS mobile operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["IPhone"]
    class_class_curie: ClassVar[str] = "uco-observable:IPhone"
    class_name: ClassVar[str] = "IPhone"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.IPhone

    id: Union[str, IPhoneId] = None
    type: Optional[Union[str, URIorCURIE]] = None
    createdBy: Optional[Union[str, IdentityAbstractionId]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    externalReference: Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]] = empty_list()
    hasFacet: Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    objectMarking: Optional[Union[Union[str, MarkingDefinitionAbstractionId], list[Union[str, MarkingDefinitionAbstractionId]]]] = empty_list()
    objectStatus: Optional[Union[str, "ObjectStatusVocab"]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, list[str]]] = empty_list()
    hasChanged: Optional[Union[bool, Bool]] = None
    state: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IPhoneId):
            self.id = IPhoneId(self.id)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.createdBy is not None and not isinstance(self.createdBy, IdentityAbstractionId):
            self.createdBy = IdentityAbstractionId(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, ExternalReference) else ExternalReference(**as_dict(v)) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, Facet) else Facet(**as_dict(v)) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstractionId) else MarkingDefinitionAbstractionId(v) for v in self.objectMarking]

        if self.objectStatus is not None and not isinstance(self.objectStatus, ObjectStatusVocab):
            self.objectStatus = ObjectStatusVocab(self.objectStatus)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        if self.hasChanged is not None and not isinstance(self.hasChanged, Bool):
            self.hasChanged = Bool(self.hasChanged)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Snapshot(FileSystemObject):
    """
    A snapshot is a file system object representing a snapshot of the contents of a part of a file system at a point
    in time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Snapshot"]
    class_class_curie: ClassVar[str] = "uco-observable:Snapshot"
    class_name: ClassVar[str] = "Snapshot"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Snapshot

    id: Union[str, SnapshotId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SnapshotId):
            self.id = SnapshotId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Socket(FileSystemObject):
    """
    A socket is a special file used for inter-process communication, which enables communication between two
    processes. In addition to sending data, processes can send file descriptors across a Unix domain socket connection
    using the sendmsg() and recvmsg() system calls. Unlike named pipes which allow only unidirectional data flow,
    sockets are fully duplex-capable. [based on https://en.wikipedia.org/wiki/Unix_file_types]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Socket"]
    class_class_curie: ClassVar[str] = "uco-observable:Socket"
    class_name: ClassVar[str] = "Socket"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Socket

    id: Union[str, SocketId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SocketId):
            self.id = SocketId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SocketAddress(Address):
    """
    A socket address (combining and IP address and a port number) is a composite identifier for a network socket
    endpoint supporting internet protocol communications.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SocketAddress"]
    class_class_curie: ClassVar[str] = "uco-observable:SocketAddress"
    class_name: ClassVar[str] = "SocketAddress"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SocketAddress

    id: Union[str, SocketAddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SocketAddressId):
            self.id = SocketAddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Software(ObservableObject):
    """
    Software is a definitely scoped instance of a collection of data or computer instructions that tell the computer
    how to work. [based on https://en.wikipedia.org/wiki/Software]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Software"]
    class_class_curie: ClassVar[str] = "uco-observable:Software"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Software

    id: Union[str, SoftwareId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareId):
            self.id = SoftwareId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ConfiguredSoftware(Software):
    """
    A ConfiguredSoftware is a Software that is known to be configured to run in a more specified manner than some
    unconfigured or less-configured Software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ConfiguredSoftware"]
    class_class_curie: ClassVar[str] = "uco-observable:ConfiguredSoftware"
    class_name: ClassVar[str] = "ConfiguredSoftware"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ConfiguredSoftware

    id: Union[str, ConfiguredSoftwareId] = None
    isConfigurationOf: Optional[Union[str, SoftwareId]] = None
    usesConfiguration: Optional[Union[str, ConfigurationId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConfiguredSoftwareId):
            self.id = ConfiguredSoftwareId(self.id)

        if self.isConfigurationOf is not None and not isinstance(self.isConfigurationOf, SoftwareId):
            self.isConfigurationOf = SoftwareId(self.isConfigurationOf)

        if self.usesConfiguration is not None and not isinstance(self.usesConfiguration, ConfigurationId):
            self.usesConfiguration = ConfigurationId(self.usesConfiguration)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SoftwareFacet(Facet):
    """
    A software facet is a grouping of characteristics unique to a software program (a definitively scoped instance of
    a collection of data or computer instructions that tell the computer how to work). [based on
    https://en.wikipedia.org/wiki/Software]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SoftwareFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:SoftwareFacet"
    class_name: ClassVar[str] = "SoftwareFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SoftwareFacet

    language: Optional[str] = None
    manufacturer: Optional[Union[str, IdentityId]] = None
    observable_cpeid: Optional[str] = None
    observable_swid: Optional[str] = None
    observable_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.manufacturer is not None and not isinstance(self.manufacturer, IdentityId):
            self.manufacturer = IdentityId(self.manufacturer)

        if self.observable_cpeid is not None and not isinstance(self.observable_cpeid, str):
            self.observable_cpeid = str(self.observable_cpeid)

        if self.observable_swid is not None and not isinstance(self.observable_swid, str):
            self.observable_swid = str(self.observable_swid)

        if self.observable_version is not None and not isinstance(self.observable_version, str):
            self.observable_version = str(self.observable_version)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class StateChangeEffectFacet(DefinedEffectFacet):
    """
    A state change effect facet is a grouping of characteristics unique to the effects of actions upon observable
    objects where a state of the observable object is changed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["StateChangeEffectFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:StateChangeEffectFacet"
    class_name: ClassVar[str] = "StateChangeEffectFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.StateChangeEffectFacet

    newObject: Optional[Union[str, ObservableObjectId]] = None
    oldObject: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.newObject is not None and not isinstance(self.newObject, ObservableObjectId):
            self.newObject = ObservableObjectId(self.newObject)

        if self.oldObject is not None and not isinstance(self.oldObject, ObservableObjectId):
            self.oldObject = ObservableObjectId(self.oldObject)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class StorageMedium(Device):
    """
    A storage medium is any digital storage device that applies electromagnetic or optical surfaces, or depends solely
    on electronic circuits as solid state storage, for storing digital data. Examples include HDD (PATA), SATA, SSD,
    Optical, Memory_Card, Tape, etc
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["StorageMedium"]
    class_class_curie: ClassVar[str] = "uco-observable:StorageMedium"
    class_name: ClassVar[str] = "StorageMedium"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.StorageMedium

    id: Union[str, StorageMediumId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StorageMediumId):
            self.id = StorageMediumId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class StorageMediumFacet(Facet):
    """
    A storage medium facet is a grouping of characteristics unique to a the storage capabilities of a piece of
    equipment or a mechanism designed to serve a special purpose or perform a special function.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["StorageMediumFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:StorageMediumFacet"
    class_name: ClassVar[str] = "StorageMediumFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.StorageMediumFacet

    totalStorageCapacityInBytes: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.totalStorageCapacityInBytes is not None and not isinstance(self.totalStorageCapacityInBytes, int):
            self.totalStorageCapacityInBytes = int(self.totalStorageCapacityInBytes)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SymbolicLink(FileSystemObject):
    """
    A symbolic link is a file that contains a reference to another file or directory in the form of an absolute or
    relative path and that affects pathname resolution. [based on https://en.wikipedia.org/wiki/Symbolic_link]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SymbolicLink"]
    class_class_curie: ClassVar[str] = "uco-observable:SymbolicLink"
    class_name: ClassVar[str] = "SymbolicLink"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SymbolicLink

    id: Union[str, SymbolicLinkId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SymbolicLinkId):
            self.id = SymbolicLinkId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class SymbolicLinkFacet(Facet):
    """
    A symbolic link facet is a grouping of characteristics unique to a file that contains a reference to another file
    or directory in the form of an absolute or relative path and that affects pathname resolution. [based on
    https://en.wikipedia.org/wiki/Symbolic_link]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["SymbolicLinkFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:SymbolicLinkFacet"
    class_name: ClassVar[str] = "SymbolicLinkFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.SymbolicLinkFacet

    targetFile: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.targetFile is not None and not isinstance(self.targetFile, ObservableObjectId):
            self.targetFile = ObservableObjectId(self.targetFile)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class TCPConnection(NetworkConnection):
    """
    A TCP connection is a network connection that is conformant to the Transfer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["TCPConnection"]
    class_class_curie: ClassVar[str] = "uco-observable:TCPConnection"
    class_name: ClassVar[str] = "TCPConnection"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.TCPConnection

    id: Union[str, TCPConnectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TCPConnectionId):
            self.id = TCPConnectionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class TCPConnectionFacet(Facet):
    """
    A TCP connection facet is a grouping of characteristics unique to portions of a network connection that are
    conformant to the Transmission Control Protocl (TCP) standard.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["TCPConnectionFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:TCPConnectionFacet"
    class_name: ClassVar[str] = "TCPConnectionFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.TCPConnectionFacet

    destinationFlags: Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]] = empty_list()
    sourceFlags: Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.destinationFlags, list):
            self.destinationFlags = [self.destinationFlags] if self.destinationFlags is not None else []
        self.destinationFlags = [v if isinstance(v, UcoHexBinary) else UcoHexBinary(v) for v in self.destinationFlags]

        if not isinstance(self.sourceFlags, list):
            self.sourceFlags = [self.sourceFlags] if self.sourceFlags is not None else []
        self.sourceFlags = [v if isinstance(v, UcoHexBinary) else UcoHexBinary(v) for v in self.sourceFlags]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class TableField(ObservableObject):
    """
    A database table field and its associated value contained within a relational database.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["TableField"]
    class_class_curie: ClassVar[str] = "uco-observable:TableField"
    class_name: ClassVar[str] = "TableField"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.TableField

    id: Union[str, TableFieldId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TableFieldId):
            self.id = TableFieldId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class TableFieldFacet(Facet):
    """
    A database record facet contains properties associated with a specific table record value from a database.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["TableFieldFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:TableFieldFacet"
    class_name: ClassVar[str] = "TableFieldFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.TableFieldFacet

    recordFieldIsNull: Optional[Union[bool, Bool]] = None
    recordFieldName: Optional[str] = None
    recordFieldValue: Optional[Union[str, UcoBase64Binary, Decimal, int]] = None
    recordRowID: Optional[Union[int, str]] = None
    tableName: Optional[str] = None
    tableSchema: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.recordFieldIsNull is not None and not isinstance(self.recordFieldIsNull, Bool):
            self.recordFieldIsNull = Bool(self.recordFieldIsNull)

        if self.recordFieldName is not None and not isinstance(self.recordFieldName, str):
            self.recordFieldName = str(self.recordFieldName)

        if self.recordFieldValue is not None and not isinstance(self.recordFieldValue, (UcoBase64Binary, Decimal, int, str)):
            value = self.recordFieldValue
            for _coerce in (lambda: UcoBase64Binary(value), lambda: Decimal(value), lambda: int(value), lambda: str(value)):
                try:
                    self.recordFieldValue = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[UcoBase64Binary, Decimal, int, str] could be constructed from {value!r} for slot recordFieldValue")

        if self.recordRowID is not None and not isinstance(self.recordRowID, (int, str)):
            value = self.recordRowID
            for _coerce in (lambda: int(value), lambda: str(value)):
                try:
                    self.recordRowID = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[int, str] could be constructed from {value!r} for slot recordRowID")

        if self.tableName is not None and not isinstance(self.tableName, str):
            self.tableName = str(self.tableName)

        if self.tableSchema is not None and not isinstance(self.tableSchema, str):
            self.tableSchema = str(self.tableSchema)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Tablet(Computer):
    """
    A tablet is a mobile computer that is primarily operated by touching the screen. (Devices categorized by their
    manufacturer as a Tablet)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Tablet"]
    class_class_curie: ClassVar[str] = "uco-observable:Tablet"
    class_name: ClassVar[str] = "Tablet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Tablet

    id: Union[str, TabletId] = None
    type: Optional[Union[str, URIorCURIE]] = None
    createdBy: Optional[Union[str, IdentityAbstractionId]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    externalReference: Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]] = empty_list()
    hasFacet: Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    objectMarking: Optional[Union[Union[str, MarkingDefinitionAbstractionId], list[Union[str, MarkingDefinitionAbstractionId]]]] = empty_list()
    objectStatus: Optional[Union[str, "ObjectStatusVocab"]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, list[str]]] = empty_list()
    hasChanged: Optional[Union[bool, Bool]] = None
    state: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TabletId):
            self.id = TabletId(self.id)

        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)

        if self.createdBy is not None and not isinstance(self.createdBy, IdentityAbstractionId):
            self.createdBy = IdentityAbstractionId(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, ExternalReference) else ExternalReference(**as_dict(v)) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, Facet) else Facet(**as_dict(v)) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstractionId) else MarkingDefinitionAbstractionId(v) for v in self.objectMarking]

        if self.objectStatus is not None and not isinstance(self.objectStatus, ObjectStatusVocab):
            self.objectStatus = ObjectStatusVocab(self.objectStatus)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        if self.hasChanged is not None and not isinstance(self.hasChanged, Bool):
            self.hasChanged = Bool(self.hasChanged)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaskActionType(UcoInherentCharacterizationThing):
    """
    A task action type is a grouping of characteristics for a scheduled action to be completed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["TaskActionType"]
    class_class_curie: ClassVar[str] = "uco-observable:TaskActionType"
    class_name: ClassVar[str] = "TaskActionType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.TaskActionType

    actionID: Optional[str] = None
    actionType: Optional[Union[str, "TaskActionTypeVocab"]] = None
    iComHandlerAction: Optional[Union[dict, IComHandlerActionType]] = None
    iEmailAction: Optional[Union[str, ObservableObjectId]] = None
    iExecAction: Optional[Union[dict, IExecActionType]] = None
    iShowMessageAction: Optional[Union[dict, IShowMessageActionType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.actionID is not None and not isinstance(self.actionID, str):
            self.actionID = str(self.actionID)

        if self.actionType is not None and not isinstance(self.actionType, (TaskActionTypeVocab, str)):
            value = self.actionType
            for _coerce in (lambda: TaskActionTypeVocab(value), lambda: str(value)):
                try:
                    self.actionType = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[TaskActionTypeVocab, str] could be constructed from {value!r} for slot actionType")

        if self.iComHandlerAction is not None and not isinstance(self.iComHandlerAction, IComHandlerActionType):
            self.iComHandlerAction = IComHandlerActionType(**as_dict(self.iComHandlerAction))

        if self.iEmailAction is not None and not isinstance(self.iEmailAction, ObservableObjectId):
            self.iEmailAction = ObservableObjectId(self.iEmailAction)

        if self.iExecAction is not None and not isinstance(self.iExecAction, IExecActionType):
            self.iExecAction = IExecActionType(**as_dict(self.iExecAction))

        if self.iShowMessageAction is not None and not isinstance(self.iShowMessageAction, IShowMessageActionType):
            self.iShowMessageAction = IShowMessageActionType(**as_dict(self.iShowMessageAction))

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class TriggerType(UcoInherentCharacterizationThing):
    """
    A trigger type is a grouping of characterizes unique to a set of criteria that, when met, starts the execution of
    a task within a Windows operating system. [based on
    https://docs.microsoft.com/en-us/windows/win32/taskschd/task-triggers]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["TriggerType"]
    class_class_curie: ClassVar[str] = "uco-observable:TriggerType"
    class_name: ClassVar[str] = "TriggerType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.TriggerType

    isEnabled: Optional[Union[bool, Bool]] = None
    triggerBeginTime: Optional[Union[str, XSDDateTime]] = None
    triggerDelay: Optional[str] = None
    triggerEndTime: Optional[Union[str, XSDDateTime]] = None
    triggerFrequency: Optional[Union[str, "TriggerFrequencyVocab"]] = None
    triggerMaxRunTime: Optional[str] = None
    triggerSessionChangeType: Optional[str] = None
    triggerType: Optional[Union[str, "TriggerTypeVocab"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.isEnabled is not None and not isinstance(self.isEnabled, Bool):
            self.isEnabled = Bool(self.isEnabled)

        if self.triggerBeginTime is not None and not isinstance(self.triggerBeginTime, XSDDateTime):
            self.triggerBeginTime = XSDDateTime(self.triggerBeginTime)

        if self.triggerDelay is not None and not isinstance(self.triggerDelay, str):
            self.triggerDelay = str(self.triggerDelay)

        if self.triggerEndTime is not None and not isinstance(self.triggerEndTime, XSDDateTime):
            self.triggerEndTime = XSDDateTime(self.triggerEndTime)

        if self.triggerFrequency is not None and not isinstance(self.triggerFrequency, (TriggerFrequencyVocab, str)):
            value = self.triggerFrequency
            for _coerce in (lambda: TriggerFrequencyVocab(value), lambda: str(value)):
                try:
                    self.triggerFrequency = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[TriggerFrequencyVocab, str] could be constructed from {value!r} for slot triggerFrequency")

        if self.triggerMaxRunTime is not None and not isinstance(self.triggerMaxRunTime, str):
            self.triggerMaxRunTime = str(self.triggerMaxRunTime)

        if self.triggerSessionChangeType is not None and not isinstance(self.triggerSessionChangeType, str):
            self.triggerSessionChangeType = str(self.triggerSessionChangeType)

        if self.triggerType is not None and not isinstance(self.triggerType, (TriggerTypeVocab, str)):
            value = self.triggerType
            for _coerce in (lambda: TriggerTypeVocab(value), lambda: str(value)):
                try:
                    self.triggerType = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[TriggerTypeVocab, str] could be constructed from {value!r} for slot triggerType")

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Tweet(Message):
    """
    A tweet is message submitted by a Twitter user account to the Twitter microblogging platform.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Tweet"]
    class_class_curie: ClassVar[str] = "uco-observable:Tweet"
    class_name: ClassVar[str] = "Tweet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Tweet

    id: Union[str, TweetId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TweetId):
            self.id = TweetId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class TwitterProfileFacet(Facet):
    """
    A twitter profile facet is a grouping of characteristics unique to an explicit digital representation of identity
    and characteristics of the owner of a single Twitter user account. [based on
    https://en.wikipedia.org/wiki/User_profile]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["TwitterProfileFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:TwitterProfileFacet"
    class_name: ClassVar[str] = "TwitterProfileFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.TwitterProfileFacet

    favoritesCount: Optional[Union[int, UcoNonNegativeInteger]] = None
    followersCount: Optional[Union[int, UcoNonNegativeInteger]] = None
    friendsCount: Optional[Union[int, UcoNonNegativeInteger]] = None
    listedCount: Optional[int] = None
    profileBackgroundHash: Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]] = empty_list()
    profileBackgroundLocation: Optional[Union[str, ObservableObjectId]] = None
    profileBannerHash: Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]] = empty_list()
    profileBannerLocation: Optional[Union[str, ObservableObjectId]] = None
    profileImageHash: Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]] = empty_list()
    profileImageLocation: Optional[Union[str, ObservableObjectId]] = None
    profileIsProtected: Optional[Union[bool, Bool]] = None
    profileIsVerified: Optional[Union[bool, Bool]] = None
    statusesCount: Optional[Union[int, UcoNonNegativeInteger]] = None
    twitterHandle: Optional[str] = None
    twitterId: Optional[str] = None
    userLocationString: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.favoritesCount is not None and not isinstance(self.favoritesCount, UcoNonNegativeInteger):
            self.favoritesCount = UcoNonNegativeInteger(self.favoritesCount)

        if self.followersCount is not None and not isinstance(self.followersCount, UcoNonNegativeInteger):
            self.followersCount = UcoNonNegativeInteger(self.followersCount)

        if self.friendsCount is not None and not isinstance(self.friendsCount, UcoNonNegativeInteger):
            self.friendsCount = UcoNonNegativeInteger(self.friendsCount)

        if self.listedCount is not None and not isinstance(self.listedCount, int):
            self.listedCount = int(self.listedCount)

        self._normalize_inlined_as_list(slot_name="profileBackgroundHash", slot_type=Hash, key_name="hashMethod", keyed=False)

        if self.profileBackgroundLocation is not None and not isinstance(self.profileBackgroundLocation, ObservableObjectId):
            self.profileBackgroundLocation = ObservableObjectId(self.profileBackgroundLocation)

        self._normalize_inlined_as_list(slot_name="profileBannerHash", slot_type=Hash, key_name="hashMethod", keyed=False)

        if self.profileBannerLocation is not None and not isinstance(self.profileBannerLocation, ObservableObjectId):
            self.profileBannerLocation = ObservableObjectId(self.profileBannerLocation)

        self._normalize_inlined_as_list(slot_name="profileImageHash", slot_type=Hash, key_name="hashMethod", keyed=False)

        if self.profileImageLocation is not None and not isinstance(self.profileImageLocation, ObservableObjectId):
            self.profileImageLocation = ObservableObjectId(self.profileImageLocation)

        if self.profileIsProtected is not None and not isinstance(self.profileIsProtected, Bool):
            self.profileIsProtected = Bool(self.profileIsProtected)

        if self.profileIsVerified is not None and not isinstance(self.profileIsVerified, Bool):
            self.profileIsVerified = Bool(self.profileIsVerified)

        if self.statusesCount is not None and not isinstance(self.statusesCount, UcoNonNegativeInteger):
            self.statusesCount = UcoNonNegativeInteger(self.statusesCount)

        if self.twitterHandle is not None and not isinstance(self.twitterHandle, str):
            self.twitterHandle = str(self.twitterHandle)

        if self.twitterId is not None and not isinstance(self.twitterId, str):
            self.twitterId = str(self.twitterId)

        if self.userLocationString is not None and not isinstance(self.userLocationString, str):
            self.userLocationString = str(self.userLocationString)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UNIXAccount(DigitalAccount):
    """
    A UNIX account is an account on a UNIX operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["UNIXAccount"]
    class_class_curie: ClassVar[str] = "uco-observable:UNIXAccount"
    class_name: ClassVar[str] = "UNIXAccount"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UNIXAccount

    id: Union[str, UNIXAccountId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UNIXAccountId):
            self.id = UNIXAccountId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UNIXAccountFacet(Facet):
    """
    A UNIX account facet is a grouping of characteristics unique to an account on a UNIX operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["UNIXAccountFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:UNIXAccountFacet"
    class_name: ClassVar[str] = "UNIXAccountFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UNIXAccountFacet

    gid: Optional[int] = None
    shell: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.gid is not None and not isinstance(self.gid, int):
            self.gid = int(self.gid)

        if self.shell is not None and not isinstance(self.shell, str):
            self.shell = str(self.shell)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UNIXFile(File):
    """
    A UNIX file is a file pertaining to the UNIX operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["UNIXFile"]
    class_class_curie: ClassVar[str] = "uco-observable:UNIXFile"
    class_name: ClassVar[str] = "UNIXFile"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UNIXFile

    id: Union[str, UNIXFileId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UNIXFileId):
            self.id = UNIXFileId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class UNIXFilePermissionsFacet(Facet):
    """
    A UNIX file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change,
    navigate, execute) of a file on a UNIX file system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["UNIXFilePermissionsFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:UNIXFilePermissionsFacet"
    class_name: ClassVar[str] = "UNIXFilePermissionsFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UNIXFilePermissionsFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UNIXProcess(Process):
    """
    A UNIX process is an instance of a computer program executed on a UNIX operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["UNIXProcess"]
    class_class_curie: ClassVar[str] = "uco-observable:UNIXProcess"
    class_name: ClassVar[str] = "UNIXProcess"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UNIXProcess

    id: Union[str, UNIXProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UNIXProcessId):
            self.id = UNIXProcessId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UNIXProcessFacet(Facet):
    """
    A UNIX process facet is a grouping of characteristics unique to an instance of a computer program executed on a
    UNIX operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["UNIXProcessFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:UNIXProcessFacet"
    class_name: ClassVar[str] = "UNIXProcessFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UNIXProcessFacet

    openFileDescriptor: Optional[Union[int, list[int]]] = empty_list()
    ruid: Optional[Union[Union[int, UcoNonNegativeInteger], list[Union[int, UcoNonNegativeInteger]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.openFileDescriptor, list):
            self.openFileDescriptor = [self.openFileDescriptor] if self.openFileDescriptor is not None else []
        self.openFileDescriptor = [v if isinstance(v, int) else int(v) for v in self.openFileDescriptor]

        if not isinstance(self.ruid, list):
            self.ruid = [self.ruid] if self.ruid is not None else []
        self.ruid = [v if isinstance(v, UcoNonNegativeInteger) else UcoNonNegativeInteger(v) for v in self.ruid]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UNIXVolumeFacet(Facet):
    """
    A UNIX volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a
    single UNIX file system. [based on https://en.wikipedia.org/wiki/Volume_(computing)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["UNIXVolumeFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:UNIXVolumeFacet"
    class_name: ClassVar[str] = "UNIXVolumeFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UNIXVolumeFacet

    mountPoint: Optional[str] = None
    options: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.mountPoint is not None and not isinstance(self.mountPoint, str):
            self.mountPoint = str(self.mountPoint)

        if self.options is not None and not isinstance(self.options, str):
            self.options = str(self.options)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class URL(ObservableObject):
    """
    A URL is a uniform resource locator (URL) acting as a resolvable address to a particular WWW (World Wide Web)
    accessible resource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["URL"]
    class_class_curie: ClassVar[str] = "uco-observable:URL"
    class_name: ClassVar[str] = "URL"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.URL

    id: Union[str, URLId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, URLId):
            self.id = URLId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class URLFacet(Facet):
    """
    A URL facet is a grouping of characteristics unique to a uniform resource locator (URL) acting as a resolvable
    address to a particular WWW (World Wide Web) accessible resource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["URLFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:URLFacet"
    class_name: ClassVar[str] = "URLFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.URLFacet

    fragment: Optional[str] = None
    fullValue: Optional[str] = None
    host: Optional[Union[str, ObservableObjectId]] = None
    password: Optional[str] = None
    path: Optional[str] = None
    port: Optional[int] = None
    query: Optional[str] = None
    scheme: Optional[str] = None
    userName: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fragment is not None and not isinstance(self.fragment, str):
            self.fragment = str(self.fragment)

        if self.fullValue is not None and not isinstance(self.fullValue, str):
            self.fullValue = str(self.fullValue)

        if self.host is not None and not isinstance(self.host, ObservableObjectId):
            self.host = ObservableObjectId(self.host)

        if self.password is not None and not isinstance(self.password, str):
            self.password = str(self.password)

        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        if self.port is not None and not isinstance(self.port, int):
            self.port = int(self.port)

        if self.query is not None and not isinstance(self.query, str):
            self.query = str(self.query)

        if self.scheme is not None and not isinstance(self.scheme, str):
            self.scheme = str(self.scheme)

        if self.userName is not None and not isinstance(self.userName, str):
            self.userName = str(self.userName)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class URLHistory(ObservableObject):
    """
    A URL history characterizes the stored URL history for a particular web browser
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["URLHistory"]
    class_class_curie: ClassVar[str] = "uco-observable:URLHistory"
    class_name: ClassVar[str] = "URLHistory"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.URLHistory

    id: Union[str, URLHistoryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, URLHistoryId):
            self.id = URLHistoryId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class URLHistoryEntry(UcoInherentCharacterizationThing):
    """
    A URL history entry is a grouping of characteristics unique to the properties of a single URL history entry for a
    particular browser.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["URLHistoryEntry"]
    class_class_curie: ClassVar[str] = "uco-observable:URLHistoryEntry"
    class_name: ClassVar[str] = "URLHistoryEntry"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.URLHistoryEntry

    browserUserProfile: Optional[str] = None
    expirationTime: Optional[Union[str, XSDDateTime]] = None
    firstVisit: Optional[Union[str, XSDDateTime]] = None
    hostname: Optional[str] = None
    keywordSearchTerm: Optional[Union[str, list[str]]] = empty_list()
    lastVisit: Optional[Union[str, XSDDateTime]] = None
    manuallyEnteredCount: Optional[Union[int, UcoNonNegativeInteger]] = None
    pageTitle: Optional[str] = None
    referrerUrl: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    url: Optional[Union[str, ObservableObjectId]] = None
    visitCount: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.browserUserProfile is not None and not isinstance(self.browserUserProfile, str):
            self.browserUserProfile = str(self.browserUserProfile)

        if self.expirationTime is not None and not isinstance(self.expirationTime, XSDDateTime):
            self.expirationTime = XSDDateTime(self.expirationTime)

        if self.firstVisit is not None and not isinstance(self.firstVisit, XSDDateTime):
            self.firstVisit = XSDDateTime(self.firstVisit)

        if self.hostname is not None and not isinstance(self.hostname, str):
            self.hostname = str(self.hostname)

        if not isinstance(self.keywordSearchTerm, list):
            self.keywordSearchTerm = [self.keywordSearchTerm] if self.keywordSearchTerm is not None else []
        self.keywordSearchTerm = [v if isinstance(v, str) else str(v) for v in self.keywordSearchTerm]

        if self.lastVisit is not None and not isinstance(self.lastVisit, XSDDateTime):
            self.lastVisit = XSDDateTime(self.lastVisit)

        if self.manuallyEnteredCount is not None and not isinstance(self.manuallyEnteredCount, UcoNonNegativeInteger):
            self.manuallyEnteredCount = UcoNonNegativeInteger(self.manuallyEnteredCount)

        if self.pageTitle is not None and not isinstance(self.pageTitle, str):
            self.pageTitle = str(self.pageTitle)

        if not isinstance(self.referrerUrl, list):
            self.referrerUrl = [self.referrerUrl] if self.referrerUrl is not None else []
        self.referrerUrl = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.referrerUrl]

        if self.url is not None and not isinstance(self.url, ObservableObjectId):
            self.url = ObservableObjectId(self.url)

        if self.visitCount is not None and not isinstance(self.visitCount, int):
            self.visitCount = int(self.visitCount)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class URLHistoryFacet(Facet):
    """
    A URL history facet is a grouping of characteristics unique to the stored URL history for a particular web browser
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["URLHistoryFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:URLHistoryFacet"
    class_name: ClassVar[str] = "URLHistoryFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.URLHistoryFacet

    browserInformation: Optional[Union[str, ObservableObjectId]] = None
    urlHistoryEntry: Optional[Union[Union[dict, URLHistoryEntry], list[Union[dict, URLHistoryEntry]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.browserInformation is not None and not isinstance(self.browserInformation, ObservableObjectId):
            self.browserInformation = ObservableObjectId(self.browserInformation)

        if not isinstance(self.urlHistoryEntry, list):
            self.urlHistoryEntry = [self.urlHistoryEntry] if self.urlHistoryEntry is not None else []
        self.urlHistoryEntry = [v if isinstance(v, URLHistoryEntry) else URLHistoryEntry(**as_dict(v)) for v in self.urlHistoryEntry]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class URLVisit(ObservableObject):
    """
    A URL visit characterizes the properties of a visit of a URL within a particular browser.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["URLVisit"]
    class_class_curie: ClassVar[str] = "uco-observable:URLVisit"
    class_name: ClassVar[str] = "URLVisit"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.URLVisit

    id: Union[str, URLVisitId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, URLVisitId):
            self.id = URLVisitId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class URLVisitFacet(Facet):
    """
    A URL visit facet is a grouping of characteristics unique to the properties of a visit of a URL within a
    particular browser.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["URLVisitFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:URLVisitFacet"
    class_name: ClassVar[str] = "URLVisitFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.URLVisitFacet

    browserInformation: Optional[Union[str, ObservableObjectId]] = None
    fromURLVisit: Optional[Union[str, ObservableObjectId]] = None
    url: Optional[Union[str, ObservableObjectId]] = None
    urlTransitionType: Optional[Union[str, "URLTransitionTypeVocab"]] = None
    visitDuration: Optional[Union[str, UcoDuration]] = None
    visitTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.browserInformation is not None and not isinstance(self.browserInformation, ObservableObjectId):
            self.browserInformation = ObservableObjectId(self.browserInformation)

        if self.fromURLVisit is not None and not isinstance(self.fromURLVisit, ObservableObjectId):
            self.fromURLVisit = ObservableObjectId(self.fromURLVisit)

        if self.url is not None and not isinstance(self.url, ObservableObjectId):
            self.url = ObservableObjectId(self.url)

        if self.urlTransitionType is not None and not isinstance(self.urlTransitionType, (URLTransitionTypeVocab, str)):
            value = self.urlTransitionType
            for _coerce in (lambda: URLTransitionTypeVocab(value), lambda: str(value)):
                try:
                    self.urlTransitionType = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[URLTransitionTypeVocab, str] could be constructed from {value!r} for slot urlTransitionType")

        if self.visitDuration is not None and not isinstance(self.visitDuration, UcoDuration):
            self.visitDuration = UcoDuration(self.visitDuration)

        if self.visitTime is not None and not isinstance(self.visitTime, XSDDateTime):
            self.visitTime = XSDDateTime(self.visitTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UserAccount(DigitalAccount):
    """
    A user account is an account controlling a user's access to a network, system or platform.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["UserAccount"]
    class_class_curie: ClassVar[str] = "uco-observable:UserAccount"
    class_name: ClassVar[str] = "UserAccount"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UserAccount

    id: Union[str, UserAccountId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UserAccountId):
            self.id = UserAccountId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UserAccountFacet(Facet):
    """
    A user account facet is a grouping of characteristics unique to an account controlling a user's access to a
    network, system, or platform.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["UserAccountFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:UserAccountFacet"
    class_name: ClassVar[str] = "UserAccountFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UserAccountFacet

    canEscalatePrivs: Optional[Union[bool, Bool]] = None
    homeDirectory: Optional[str] = None
    isPrivileged: Optional[Union[bool, Bool]] = None
    isServiceAccount: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.canEscalatePrivs is not None and not isinstance(self.canEscalatePrivs, Bool):
            self.canEscalatePrivs = Bool(self.canEscalatePrivs)

        if self.homeDirectory is not None and not isinstance(self.homeDirectory, str):
            self.homeDirectory = str(self.homeDirectory)

        if self.isPrivileged is not None and not isinstance(self.isPrivileged, Bool):
            self.isPrivileged = Bool(self.isPrivileged)

        if self.isServiceAccount is not None and not isinstance(self.isServiceAccount, Bool):
            self.isServiceAccount = Bool(self.isServiceAccount)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UserSession(ObservableObject):
    """
    A user session is a temporary and interactive information interchange between two or more communicating devices
    within the managed scope of a single user. [based on https://en.wikipedia.org/wiki/Session_(computer_science)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["UserSession"]
    class_class_curie: ClassVar[str] = "uco-observable:UserSession"
    class_name: ClassVar[str] = "UserSession"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UserSession

    id: Union[str, UserSessionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UserSessionId):
            self.id = UserSessionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class UserSessionFacet(Facet):
    """
    A user session facet is a grouping of characteristics unique to a temporary and interactive information
    interchange between two or more communicating devices within the managed scope of a single user. [based on
    https://en.wikipedia.org/wiki/Session_(computer_science)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["UserSessionFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:UserSessionFacet"
    class_name: ClassVar[str] = "UserSessionFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.UserSessionFacet

    effectiveGroup: Optional[str] = None
    effectiveGroupID: Optional[str] = None
    effectiveUser: Optional[Union[str, ObservableObjectId]] = None
    loginTime: Optional[Union[str, XSDDateTime]] = None
    logoutTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.effectiveGroup is not None and not isinstance(self.effectiveGroup, str):
            self.effectiveGroup = str(self.effectiveGroup)

        if self.effectiveGroupID is not None and not isinstance(self.effectiveGroupID, str):
            self.effectiveGroupID = str(self.effectiveGroupID)

        if self.effectiveUser is not None and not isinstance(self.effectiveUser, ObservableObjectId):
            self.effectiveUser = ObservableObjectId(self.effectiveUser)

        if self.loginTime is not None and not isinstance(self.loginTime, XSDDateTime):
            self.loginTime = XSDDateTime(self.loginTime)

        if self.logoutTime is not None and not isinstance(self.logoutTime, XSDDateTime):
            self.logoutTime = XSDDateTime(self.logoutTime)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class ValuesEnumeratedEffectFacet(DefinedEffectFacet):
    """
    A values enumerated effect facet is a grouping of characteristics unique to the effects of actions upon observable
    objects where a value of the observable object is enumerated. An example of this would be the values of a registry
    key.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["ValuesEnumeratedEffectFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:ValuesEnumeratedEffectFacet"
    class_name: ClassVar[str] = "ValuesEnumeratedEffectFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.ValuesEnumeratedEffectFacet

    values: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.values is not None and not isinstance(self.values, str):
            self.values = str(self.values)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Volume(ObservableObject):
    """
    A volume is a single accessible storage area (volume) with a single file system. [based on
    https://en.wikipedia.org/wiki/Volume_(computing)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Volume"]
    class_class_curie: ClassVar[str] = "uco-observable:Volume"
    class_name: ClassVar[str] = "Volume"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Volume

    id: Union[str, VolumeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VolumeId):
            self.id = VolumeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class VolumeFacet(Facet):
    """
    A volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a single
    file system. [based on https://en.wikipedia.org/wiki/Volume_(computing)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["VolumeFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:VolumeFacet"
    class_name: ClassVar[str] = "VolumeFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.VolumeFacet

    sectorSize: Optional[int] = None
    volumeID: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sectorSize is not None and not isinstance(self.sectorSize, int):
            self.sectorSize = int(self.sectorSize)

        if self.volumeID is not None and not isinstance(self.volumeID, str):
            self.volumeID = str(self.volumeID)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WearableDevice(SmartDevice):
    """
    A wearable device is an electronic device that is designed to be worn on a person's body.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WearableDevice"]
    class_class_curie: ClassVar[str] = "uco-observable:WearableDevice"
    class_name: ClassVar[str] = "WearableDevice"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WearableDevice

    id: Union[str, WearableDeviceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WearableDeviceId):
            self.id = WearableDeviceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WebPage(ObservableObject):
    """
    A web page is a specific collection of information provided by a website and displayed to a user in a web browser.
    A website typically consists of many web pages linked together in a coherent fashion. [based on
    https://en.wikipedia.org/wiki/Web_page]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WebPage"]
    class_class_curie: ClassVar[str] = "uco-observable:WebPage"
    class_name: ClassVar[str] = "WebPage"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WebPage

    id: Union[str, WebPageId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WebPageId):
            self.id = WebPageId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WhoIs(ObservableObject):
    """
    WhoIs is a response record conformant to the WHOIS protocol standard (RFC 3912). [based on
    https://en.wikipedia.org/wiki/WHOIS]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WhoIs"]
    class_class_curie: ClassVar[str] = "uco-observable:WhoIs"
    class_name: ClassVar[str] = "WhoIs"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WhoIs

    id: Union[str, WhoIsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WhoIsId):
            self.id = WhoIsId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WhoIsFacet(Facet):
    """
    A whois facet is a grouping of characteristics unique to a response record conformant to the WHOIS protocol
    standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WhoIsFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WhoIsFacet"
    class_name: ClassVar[str] = "WhoIsFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WhoIsFacet

    creationDate: Optional[Union[str, XSDDateTime]] = None
    dnssec: Optional[Union[str, "WhoisDNSSECTypeVocab"]] = None
    domainID: Optional[str] = None
    domainName: Optional[Union[str, ObservableObjectId]] = None
    expirationDate: Optional[Union[str, XSDDateTime]] = None
    ipAddress: Optional[Union[str, ObservableObjectId]] = None
    lookupDate: Optional[Union[str, XSDDateTime]] = None
    nameServer: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    regionalInternetRegistry: Optional[Union[str, "RegionalRegistryTypeVocab"]] = None
    registrantContactInfo: Optional[Union[str, ObservableObjectId]] = None
    registrantIDs: Optional[Union[str, list[str]]] = empty_list()
    registrarInfo: Optional[Union[dict, "WhoisRegistrarInfoType"]] = None
    remarks: Optional[str] = None
    serverName: Optional[Union[str, ObservableObjectId]] = None
    sponsoringRegistrar: Optional[str] = None
    status: Optional[Union[str, "TaskStatusVocab", "WhoisStatusTypeVocab"]] = None
    updatedDate: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.creationDate is not None and not isinstance(self.creationDate, XSDDateTime):
            self.creationDate = XSDDateTime(self.creationDate)

        if self.dnssec is not None and not isinstance(self.dnssec, WhoisDNSSECTypeVocab):
            self.dnssec = WhoisDNSSECTypeVocab(self.dnssec)

        if self.domainID is not None and not isinstance(self.domainID, str):
            self.domainID = str(self.domainID)

        if self.domainName is not None and not isinstance(self.domainName, ObservableObjectId):
            self.domainName = ObservableObjectId(self.domainName)

        if self.expirationDate is not None and not isinstance(self.expirationDate, XSDDateTime):
            self.expirationDate = XSDDateTime(self.expirationDate)

        if self.ipAddress is not None and not isinstance(self.ipAddress, ObservableObjectId):
            self.ipAddress = ObservableObjectId(self.ipAddress)

        if self.lookupDate is not None and not isinstance(self.lookupDate, XSDDateTime):
            self.lookupDate = XSDDateTime(self.lookupDate)

        if not isinstance(self.nameServer, list):
            self.nameServer = [self.nameServer] if self.nameServer is not None else []
        self.nameServer = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.nameServer]

        if self.regionalInternetRegistry is not None and not isinstance(self.regionalInternetRegistry, (RegionalRegistryTypeVocab, str)):
            value = self.regionalInternetRegistry
            for _coerce in (lambda: RegionalRegistryTypeVocab(value), lambda: str(value)):
                try:
                    self.regionalInternetRegistry = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[RegionalRegistryTypeVocab, str] could be constructed from {value!r} for slot regionalInternetRegistry")

        if self.registrantContactInfo is not None and not isinstance(self.registrantContactInfo, ObservableObjectId):
            self.registrantContactInfo = ObservableObjectId(self.registrantContactInfo)

        if not isinstance(self.registrantIDs, list):
            self.registrantIDs = [self.registrantIDs] if self.registrantIDs is not None else []
        self.registrantIDs = [v if isinstance(v, str) else str(v) for v in self.registrantIDs]

        if self.registrarInfo is not None and not isinstance(self.registrarInfo, WhoisRegistrarInfoType):
            self.registrarInfo = WhoisRegistrarInfoType(**as_dict(self.registrarInfo))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        if self.serverName is not None and not isinstance(self.serverName, ObservableObjectId):
            self.serverName = ObservableObjectId(self.serverName)

        if self.sponsoringRegistrar is not None and not isinstance(self.sponsoringRegistrar, str):
            self.sponsoringRegistrar = str(self.sponsoringRegistrar)

        if self.status is not None and not isinstance(self.status, (TaskStatusVocab, WhoisStatusTypeVocab, str)):
            value = self.status
            for _coerce in (lambda: TaskStatusVocab(value), lambda: WhoisStatusTypeVocab(value), lambda: str(value)):
                try:
                    self.status = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[TaskStatusVocab, WhoisStatusTypeVocab, str] could be constructed from {value!r} for slot status")

        if self.updatedDate is not None and not isinstance(self.updatedDate, XSDDateTime):
            self.updatedDate = XSDDateTime(self.updatedDate)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WhoisContactFacet(ContactFacet):
    """
    A Whois contact type is a grouping of characteristics unique to contact-related information present in a response
    record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WhoisContactFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WhoisContactFacet"
    class_name: ClassVar[str] = "WhoisContactFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WhoisContactFacet

    whoisContactType: Optional[Union[str, "WhoisContactTypeVocab"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.whoisContactType is not None and not isinstance(self.whoisContactType, (WhoisContactTypeVocab, str)):
            value = self.whoisContactType
            for _coerce in (lambda: WhoisContactTypeVocab(value), lambda: str(value)):
                try:
                    self.whoisContactType = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[WhoisContactTypeVocab, str] could be constructed from {value!r} for slot whoisContactType")

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WhoisRegistrarInfoType(UcoInherentCharacterizationThing):
    """
    A Whois registrar info type is a grouping of characteristics unique to registrar-related information present in a
    response record conformant to the WHOIS protocol standard (RFC 3912). [based on
    https://en.wikipedia.org/wiki/WHOIS]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WhoisRegistrarInfoType"]
    class_class_curie: ClassVar[str] = "uco-observable:WhoisRegistrarInfoType"
    class_name: ClassVar[str] = "WhoisRegistrarInfoType"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WhoisRegistrarInfoType

    contactPhoneNumber: Optional[Union[str, ObservableObjectId]] = None
    emailAddress: Optional[Union[str, ObservableObjectId]] = None
    geolocationAddress: Optional[Union[str, LocationId]] = None
    referralURL: Optional[Union[str, ObservableObjectId]] = None
    registrarGUID: Optional[str] = None
    registrarID: Optional[str] = None
    registrarName: Optional[str] = None
    whoisServer: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contactPhoneNumber is not None and not isinstance(self.contactPhoneNumber, ObservableObjectId):
            self.contactPhoneNumber = ObservableObjectId(self.contactPhoneNumber)

        if self.emailAddress is not None and not isinstance(self.emailAddress, ObservableObjectId):
            self.emailAddress = ObservableObjectId(self.emailAddress)

        if self.geolocationAddress is not None and not isinstance(self.geolocationAddress, LocationId):
            self.geolocationAddress = LocationId(self.geolocationAddress)

        if self.referralURL is not None and not isinstance(self.referralURL, ObservableObjectId):
            self.referralURL = ObservableObjectId(self.referralURL)

        if self.registrarGUID is not None and not isinstance(self.registrarGUID, str):
            self.registrarGUID = str(self.registrarGUID)

        if self.registrarID is not None and not isinstance(self.registrarID, str):
            self.registrarID = str(self.registrarID)

        if self.registrarName is not None and not isinstance(self.registrarName, str):
            self.registrarName = str(self.registrarName)

        if self.whoisServer is not None and not isinstance(self.whoisServer, ObservableObjectId):
            self.whoisServer = ObservableObjectId(self.whoisServer)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WifiAddress(MACAddress):
    """
    A Wi-Fi address is a media access control (MAC) standards-conformant identifier assigned to a device network
    interface to enable routing and management of IEEE 802.11 standards-conformant communications to and from that
    device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WifiAddress"]
    class_class_curie: ClassVar[str] = "uco-observable:WifiAddress"
    class_name: ClassVar[str] = "WifiAddress"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WifiAddress

    id: Union[str, WifiAddressId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WifiAddressId):
            self.id = WifiAddressId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


class WifiAddressFacet(MACAddressFacet):
    """
    A Wi-Fi address facet is a grouping of characteristics unique to a media access control (MAC) standards conformant
    identifier assigned to a device network interface to enable routing and management of IEEE 802.11
    standards-conformant communications to and from that device.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WifiAddressFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WifiAddressFacet"
    class_name: ClassVar[str] = "WifiAddressFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WifiAddressFacet


    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class Wiki(ObservableObject):
    """
    A wiki is an online hypertext publication collaboratively edited and managed by its own audience directly using a
    web browser. A typical wiki contains multiple pages/articles for the subjects or scope of the project and could be
    either open to the public or limited to use within an organization for maintaining its internal knowledge base.
    [based on https://en.wikipedia.org/wiki/Wiki]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["Wiki"]
    class_class_curie: ClassVar[str] = "uco-observable:Wiki"
    class_name: ClassVar[str] = "Wiki"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.Wiki

    id: Union[str, WikiId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WikiId):
            self.id = WikiId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WikiArticle(ObservableObject):
    """
    A wiki article is one or more pages in a wiki focused on characterizing a particular topic.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WikiArticle"]
    class_class_curie: ClassVar[str] = "uco-observable:WikiArticle"
    class_name: ClassVar[str] = "WikiArticle"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WikiArticle

    id: Union[str, WikiArticleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WikiArticleId):
            self.id = WikiArticleId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsAccount(DigitalAccount):
    """
    A Windows account is a user account on a Windows operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsAccount"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsAccount"
    class_name: ClassVar[str] = "WindowsAccount"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsAccount

    id: Union[str, WindowsAccountId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsAccountId):
            self.id = WindowsAccountId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsAccountFacet(Facet):
    """
    A Windows account facet is a grouping of characteristics unique to a user account on a Windows operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsAccountFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsAccountFacet"
    class_name: ClassVar[str] = "WindowsAccountFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsAccountFacet

    groups: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.groups, list):
            self.groups = [self.groups] if self.groups is not None else []
        self.groups = [v if isinstance(v, str) else str(v) for v in self.groups]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsActiveDirectoryAccount(DigitalAccount):
    """
    A Windows Active Directory account is an account managed by directory-based identity-related services of a Windows
    operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsActiveDirectoryAccount"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsActiveDirectoryAccount"
    class_name: ClassVar[str] = "WindowsActiveDirectoryAccount"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsActiveDirectoryAccount

    id: Union[str, WindowsActiveDirectoryAccountId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsActiveDirectoryAccountId):
            self.id = WindowsActiveDirectoryAccountId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsActiveDirectoryAccountFacet(Facet):
    """
    A Windows Active Directory account facet is a grouping of characteristics unique to an account managed by
    directory-based identity-related services of a Windows operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsActiveDirectoryAccountFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsActiveDirectoryAccountFacet"
    class_name: ClassVar[str] = "WindowsActiveDirectoryAccountFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsActiveDirectoryAccountFacet

    activeDirectoryGroups: Optional[Union[str, list[str]]] = empty_list()
    objectGUID: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.activeDirectoryGroups, list):
            self.activeDirectoryGroups = [self.activeDirectoryGroups] if self.activeDirectoryGroups is not None else []
        self.activeDirectoryGroups = [v if isinstance(v, str) else str(v) for v in self.activeDirectoryGroups]

        if self.objectGUID is not None and not isinstance(self.objectGUID, str):
            self.objectGUID = str(self.objectGUID)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsComputerSpecification(ObservableObject):
    """
    A Windows computer specification is the hardware ans software of a programmable electronic device that can store,
    retrieve, and process data running a Microsoft Windows operating system. [based on
    merriam-webster.com/dictionary/computer]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsComputerSpecification"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsComputerSpecification"
    class_name: ClassVar[str] = "WindowsComputerSpecification"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsComputerSpecification

    id: Union[str, WindowsComputerSpecificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsComputerSpecificationId):
            self.id = WindowsComputerSpecificationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsComputerSpecificationFacet(Facet):
    """
    A Windows computer specification facet is a grouping of characteristics unique to the hardware and software of a
    programmable electronic device that can store, retrieve, and process data running a Microsoft Windows operating
    system. [based on merriam-webster.com/dictionary/computer]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsComputerSpecificationFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsComputerSpecificationFacet"
    class_name: ClassVar[str] = "WindowsComputerSpecificationFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsComputerSpecificationFacet

    domain: Optional[Union[str, list[str]]] = empty_list()
    globalFlagList: Optional[Union[Union[dict, GlobalFlagType], list[Union[dict, GlobalFlagType]]]] = empty_list()
    lastShutdownDate: Optional[Union[str, XSDDateTime]] = None
    msProductID: Optional[str] = None
    msProductName: Optional[str] = None
    netBIOSName: Optional[str] = None
    osInstallDate: Optional[Union[str, XSDDateTime]] = None
    osLastUpgradeDate: Optional[Union[str, XSDDateTime]] = None
    registeredOrganization: Optional[Union[str, IdentityId]] = None
    registeredOwner: Optional[Union[str, IdentityId]] = None
    windowsDirectory: Optional[Union[str, ObservableObjectId]] = None
    windowsSystemDirectory: Optional[Union[str, ObservableObjectId]] = None
    windowsTempDirectory: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.domain, list):
            self.domain = [self.domain] if self.domain is not None else []
        self.domain = [v if isinstance(v, str) else str(v) for v in self.domain]

        if not isinstance(self.globalFlagList, list):
            self.globalFlagList = [self.globalFlagList] if self.globalFlagList is not None else []
        self.globalFlagList = [v if isinstance(v, GlobalFlagType) else GlobalFlagType(**as_dict(v)) for v in self.globalFlagList]

        if self.lastShutdownDate is not None and not isinstance(self.lastShutdownDate, XSDDateTime):
            self.lastShutdownDate = XSDDateTime(self.lastShutdownDate)

        if self.msProductID is not None and not isinstance(self.msProductID, str):
            self.msProductID = str(self.msProductID)

        if self.msProductName is not None and not isinstance(self.msProductName, str):
            self.msProductName = str(self.msProductName)

        if self.netBIOSName is not None and not isinstance(self.netBIOSName, str):
            self.netBIOSName = str(self.netBIOSName)

        if self.osInstallDate is not None and not isinstance(self.osInstallDate, XSDDateTime):
            self.osInstallDate = XSDDateTime(self.osInstallDate)

        if self.osLastUpgradeDate is not None and not isinstance(self.osLastUpgradeDate, XSDDateTime):
            self.osLastUpgradeDate = XSDDateTime(self.osLastUpgradeDate)

        if self.registeredOrganization is not None and not isinstance(self.registeredOrganization, IdentityId):
            self.registeredOrganization = IdentityId(self.registeredOrganization)

        if self.registeredOwner is not None and not isinstance(self.registeredOwner, IdentityId):
            self.registeredOwner = IdentityId(self.registeredOwner)

        if self.windowsDirectory is not None and not isinstance(self.windowsDirectory, ObservableObjectId):
            self.windowsDirectory = ObservableObjectId(self.windowsDirectory)

        if self.windowsSystemDirectory is not None and not isinstance(self.windowsSystemDirectory, ObservableObjectId):
            self.windowsSystemDirectory = ObservableObjectId(self.windowsSystemDirectory)

        if self.windowsTempDirectory is not None and not isinstance(self.windowsTempDirectory, ObservableObjectId):
            self.windowsTempDirectory = ObservableObjectId(self.windowsTempDirectory)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsCriticalSection(ObservableObject):
    """
    A Windows critical section is a Windows object that provides synchronization similar to that provided by a mutex
    object, except that a critical section can be used only by the threads of a single process. Critical section
    objects cannot be shared across processes. Event, mutex, and semaphore objects can also be used in a
    single-process application, but critical section objects provide a slightly faster, more efficient mechanism for
    mutual-exclusion synchronization (a processor-specific test and set instruction). Like a mutex object, a critical
    section object can be owned by only one thread at a time, which makes it useful for protecting a shared resource
    from simultaneous access. Unlike a mutex object, there is no way to tell whether a critical section has been
    abandoned. [based on https://docs.microsoft.com/en-us/windows/win32/sync/critical-section-objects]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsCriticalSection"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsCriticalSection"
    class_name: ClassVar[str] = "WindowsCriticalSection"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsCriticalSection

    id: Union[str, WindowsCriticalSectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsCriticalSectionId):
            self.id = WindowsCriticalSectionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsEvent(ObservableObject):
    """
    A Windows event is a notification record of an occurance of interest (system, security, application, etc.) on a
    Windows operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsEvent"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsEvent"
    class_name: ClassVar[str] = "WindowsEvent"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsEvent

    id: Union[str, WindowsEventId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsEventId):
            self.id = WindowsEventId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsFilemapping(ObservableObject):
    """
    A Windows file mapping is the association of a file's contents with a portion of the virtual address space of a
    process within a Windows operating system. The system creates a file mapping object (also known as a section
    object) to maintain this association. A file view is the portion of virtual address space that a process uses to
    access the file's contents. File mapping allows the process to use both random input and output (I/O) and
    sequential I/O. It also allows the process to work efficiently with a large data file, such as a database, without
    having to map the whole file into memory. Multiple processes can also use memory-mapped files to share data.
    Processes read from and write to the file view using pointers, just as they would with dynamically allocated
    memory. The use of file mapping improves efficiency because the file resides on disk, but the file view resides in
    memory.[based on https://docs.microsoft.com/en-us/windows/win32/memory/file-mapping]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsFilemapping"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsFilemapping"
    class_name: ClassVar[str] = "WindowsFilemapping"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsFilemapping

    id: Union[str, WindowsFilemappingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsFilemappingId):
            self.id = WindowsFilemappingId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsHandle(ObservableObject):
    """
    A Windows handle is an abstract reference to a resource within the Windows operating system, such as a window,
    memory, an open file or a pipe. It is the mechanism by which applications interact with such resources in the
    Windows operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsHandle"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsHandle"
    class_name: ClassVar[str] = "WindowsHandle"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsHandle

    id: Union[str, WindowsHandleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsHandleId):
            self.id = WindowsHandleId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsHook(ObservableObject):
    """
    A Windows hook is a mechanism by which an application can intercept events, such as messages, mouse actions, and
    keystrokes within the Windows operating system. A function that intercepts a particular type of event is known as
    a hook procedure. A hook procedure can act on each event it receives, and then modify or discard the event. [based
    on https://docs.microsoft.com/en-us/windows/win32/winmsg/about-hooks]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsHook"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsHook"
    class_name: ClassVar[str] = "WindowsHook"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsHook

    id: Union[str, WindowsHookId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsHookId):
            self.id = WindowsHookId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsMailslot(ObservableObject):
    """
    A Windows mailslot is is a pseudofile that resides in memory, and may be accessed using standard file functions.
    The data in a mailslot message can be in any form, but cannot be larger than 424 bytes when sent between
    computers. Unlike disk files, mailslots are temporary. When all handles to a mailslot are closed, the mailslot and
    all the data it contains are deleted. [based on
    https://docs.microsoft.com/en-us/windows/win32/ipc/about-mailslots]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsMailslot"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsMailslot"
    class_name: ClassVar[str] = "WindowsMailslot"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsMailslot

    id: Union[str, WindowsMailslotId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsMailslotId):
            self.id = WindowsMailslotId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsNetworkShare(ObservableObject):
    """
    A Windows network share is a Windows computer resource made available from one host to other hosts on a computer
    network. It is a device or piece of information on a computer that can be remotely accessed from another computer
    transparently as if it were a resource in the local machine. Network sharing is made possible by inter-process
    communication over the network. [based on https://en.wikipedia.org/wiki/Shared_resource]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsNetworkShare"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsNetworkShare"
    class_name: ClassVar[str] = "WindowsNetworkShare"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsNetworkShare

    id: Union[str, WindowsNetworkShareId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsNetworkShareId):
            self.id = WindowsNetworkShareId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsPEBinaryFile(File):
    """
    A Windows PE binary file is a Windows portable executable (PE) file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsPEBinaryFile"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsPEBinaryFile"
    class_name: ClassVar[str] = "WindowsPEBinaryFile"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsPEBinaryFile

    id: Union[str, WindowsPEBinaryFileId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsPEBinaryFileId):
            self.id = WindowsPEBinaryFileId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsPEBinaryFileFacet(Facet):
    """
    A Windows PE binary file facet is a grouping of characteristics unique to a Windows portable executable (PE) file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsPEBinaryFileFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsPEBinaryFileFacet"
    class_name: ClassVar[str] = "WindowsPEBinaryFileFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsPEBinaryFileFacet

    characteristics: Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]] = empty_list()
    fileHeaderHashes: Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]] = empty_list()
    impHash: Optional[str] = None
    machine: Optional[Union[str, list[str]]] = empty_list()
    numberOfSections: Optional[int] = None
    numberOfSymbols: Optional[int] = None
    optionalHeader: Optional[Union[dict, "WindowsPEOptionalHeader"]] = None
    peType: Optional[str] = None
    pointerToSymbolTable: Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]] = empty_list()
    sections: Optional[Union[Union[dict, "WindowsPESection"], list[Union[dict, "WindowsPESection"]]]] = empty_list()
    sizeOfOptionalHeader: Optional[int] = None
    timeDateStamp: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.characteristics, list):
            self.characteristics = [self.characteristics] if self.characteristics is not None else []
        self.characteristics = [v if isinstance(v, UcoUnsignedShort) else UcoUnsignedShort(v) for v in self.characteristics]

        self._normalize_inlined_as_list(slot_name="fileHeaderHashes", slot_type=Hash, key_name="hashMethod", keyed=False)

        if self.impHash is not None and not isinstance(self.impHash, str):
            self.impHash = str(self.impHash)

        if not isinstance(self.machine, list):
            self.machine = [self.machine] if self.machine is not None else []
        self.machine = [v if isinstance(v, str) else str(v) for v in self.machine]

        if self.numberOfSections is not None and not isinstance(self.numberOfSections, int):
            self.numberOfSections = int(self.numberOfSections)

        if self.numberOfSymbols is not None and not isinstance(self.numberOfSymbols, int):
            self.numberOfSymbols = int(self.numberOfSymbols)

        if self.optionalHeader is not None and not isinstance(self.optionalHeader, WindowsPEOptionalHeader):
            self.optionalHeader = WindowsPEOptionalHeader(**as_dict(self.optionalHeader))

        if self.peType is not None and not isinstance(self.peType, str):
            self.peType = str(self.peType)

        if not isinstance(self.pointerToSymbolTable, list):
            self.pointerToSymbolTable = [self.pointerToSymbolTable] if self.pointerToSymbolTable is not None else []
        self.pointerToSymbolTable = [v if isinstance(v, UcoHexBinary) else UcoHexBinary(v) for v in self.pointerToSymbolTable]

        if not isinstance(self.sections, list):
            self.sections = [self.sections] if self.sections is not None else []
        self.sections = [v if isinstance(v, WindowsPESection) else WindowsPESection(**as_dict(v)) for v in self.sections]

        if self.sizeOfOptionalHeader is not None and not isinstance(self.sizeOfOptionalHeader, int):
            self.sizeOfOptionalHeader = int(self.sizeOfOptionalHeader)

        if self.timeDateStamp is not None and not isinstance(self.timeDateStamp, XSDDateTime):
            self.timeDateStamp = XSDDateTime(self.timeDateStamp)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsPEFileHeader(UcoInherentCharacterizationThing):
    """
    A Windows PE file header is a grouping of characteristics unique to the 'header' of a Windows PE (Portable
    Executable) file, consisting of a collection of metadata about the overall nature and structure of the file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsPEFileHeader"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsPEFileHeader"
    class_name: ClassVar[str] = "WindowsPEFileHeader"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsPEFileHeader

    timeDateStamp: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.timeDateStamp is not None and not isinstance(self.timeDateStamp, XSDDateTime):
            self.timeDateStamp = XSDDateTime(self.timeDateStamp)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsPEOptionalHeader(UcoInherentCharacterizationThing):
    """
    A Windows PE optional header is a grouping of characteristics unique to the 'optional header' of a Windows PE
    (Portable Executable) file, consisting of a collection of metadata about the executable code structure of the
    file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsPEOptionalHeader"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsPEOptionalHeader"
    class_name: ClassVar[str] = "WindowsPEOptionalHeader"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsPEOptionalHeader

    addressOfEntryPoint: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    baseOfCode: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    checksum: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    dllCharacteristics: Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]] = empty_list()
    fileAlignment: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    imageBase: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    loaderFlags: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    magic: Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]] = empty_list()
    majorImageVersion: Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]] = empty_list()
    majorLinkerVersion: Optional[Union[Union[int, UcoByte], list[Union[int, UcoByte]]]] = empty_list()
    majorOSVersion: Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]] = empty_list()
    majorSubsystemVersion: Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]] = empty_list()
    minorImageVersion: Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]] = empty_list()
    minorLinkerVersion: Optional[Union[Union[int, UcoByte], list[Union[int, UcoByte]]]] = empty_list()
    minorOSVersion: Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]] = empty_list()
    minorSubsystemVersion: Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]] = empty_list()
    numberOfRVAAndSizes: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    sectionAlignment: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    sizeOfCode: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    sizeOfHeaders: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    sizeOfHeapCommit: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    sizeOfHeapReserve: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    sizeOfImage: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    sizeOfInitializedData: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    sizeOfStackCommit: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    sizeOfStackReserve: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    sizeOfUninitializedData: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    subsystem: Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]] = empty_list()
    win32VersionValue: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.addressOfEntryPoint, list):
            self.addressOfEntryPoint = [self.addressOfEntryPoint] if self.addressOfEntryPoint is not None else []
        self.addressOfEntryPoint = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.addressOfEntryPoint]

        if not isinstance(self.baseOfCode, list):
            self.baseOfCode = [self.baseOfCode] if self.baseOfCode is not None else []
        self.baseOfCode = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.baseOfCode]

        if not isinstance(self.checksum, list):
            self.checksum = [self.checksum] if self.checksum is not None else []
        self.checksum = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.checksum]

        if not isinstance(self.dllCharacteristics, list):
            self.dllCharacteristics = [self.dllCharacteristics] if self.dllCharacteristics is not None else []
        self.dllCharacteristics = [v if isinstance(v, UcoUnsignedShort) else UcoUnsignedShort(v) for v in self.dllCharacteristics]

        if not isinstance(self.fileAlignment, list):
            self.fileAlignment = [self.fileAlignment] if self.fileAlignment is not None else []
        self.fileAlignment = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.fileAlignment]

        if not isinstance(self.imageBase, list):
            self.imageBase = [self.imageBase] if self.imageBase is not None else []
        self.imageBase = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.imageBase]

        if not isinstance(self.loaderFlags, list):
            self.loaderFlags = [self.loaderFlags] if self.loaderFlags is not None else []
        self.loaderFlags = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.loaderFlags]

        if not isinstance(self.magic, list):
            self.magic = [self.magic] if self.magic is not None else []
        self.magic = [v if isinstance(v, UcoUnsignedShort) else UcoUnsignedShort(v) for v in self.magic]

        if not isinstance(self.majorImageVersion, list):
            self.majorImageVersion = [self.majorImageVersion] if self.majorImageVersion is not None else []
        self.majorImageVersion = [v if isinstance(v, UcoUnsignedShort) else UcoUnsignedShort(v) for v in self.majorImageVersion]

        if not isinstance(self.majorLinkerVersion, list):
            self.majorLinkerVersion = [self.majorLinkerVersion] if self.majorLinkerVersion is not None else []
        self.majorLinkerVersion = [v if isinstance(v, UcoByte) else UcoByte(v) for v in self.majorLinkerVersion]

        if not isinstance(self.majorOSVersion, list):
            self.majorOSVersion = [self.majorOSVersion] if self.majorOSVersion is not None else []
        self.majorOSVersion = [v if isinstance(v, UcoUnsignedShort) else UcoUnsignedShort(v) for v in self.majorOSVersion]

        if not isinstance(self.majorSubsystemVersion, list):
            self.majorSubsystemVersion = [self.majorSubsystemVersion] if self.majorSubsystemVersion is not None else []
        self.majorSubsystemVersion = [v if isinstance(v, UcoUnsignedShort) else UcoUnsignedShort(v) for v in self.majorSubsystemVersion]

        if not isinstance(self.minorImageVersion, list):
            self.minorImageVersion = [self.minorImageVersion] if self.minorImageVersion is not None else []
        self.minorImageVersion = [v if isinstance(v, UcoUnsignedShort) else UcoUnsignedShort(v) for v in self.minorImageVersion]

        if not isinstance(self.minorLinkerVersion, list):
            self.minorLinkerVersion = [self.minorLinkerVersion] if self.minorLinkerVersion is not None else []
        self.minorLinkerVersion = [v if isinstance(v, UcoByte) else UcoByte(v) for v in self.minorLinkerVersion]

        if not isinstance(self.minorOSVersion, list):
            self.minorOSVersion = [self.minorOSVersion] if self.minorOSVersion is not None else []
        self.minorOSVersion = [v if isinstance(v, UcoUnsignedShort) else UcoUnsignedShort(v) for v in self.minorOSVersion]

        if not isinstance(self.minorSubsystemVersion, list):
            self.minorSubsystemVersion = [self.minorSubsystemVersion] if self.minorSubsystemVersion is not None else []
        self.minorSubsystemVersion = [v if isinstance(v, UcoUnsignedShort) else UcoUnsignedShort(v) for v in self.minorSubsystemVersion]

        if not isinstance(self.numberOfRVAAndSizes, list):
            self.numberOfRVAAndSizes = [self.numberOfRVAAndSizes] if self.numberOfRVAAndSizes is not None else []
        self.numberOfRVAAndSizes = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.numberOfRVAAndSizes]

        if not isinstance(self.sectionAlignment, list):
            self.sectionAlignment = [self.sectionAlignment] if self.sectionAlignment is not None else []
        self.sectionAlignment = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.sectionAlignment]

        if not isinstance(self.sizeOfCode, list):
            self.sizeOfCode = [self.sizeOfCode] if self.sizeOfCode is not None else []
        self.sizeOfCode = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.sizeOfCode]

        if not isinstance(self.sizeOfHeaders, list):
            self.sizeOfHeaders = [self.sizeOfHeaders] if self.sizeOfHeaders is not None else []
        self.sizeOfHeaders = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.sizeOfHeaders]

        if not isinstance(self.sizeOfHeapCommit, list):
            self.sizeOfHeapCommit = [self.sizeOfHeapCommit] if self.sizeOfHeapCommit is not None else []
        self.sizeOfHeapCommit = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.sizeOfHeapCommit]

        if not isinstance(self.sizeOfHeapReserve, list):
            self.sizeOfHeapReserve = [self.sizeOfHeapReserve] if self.sizeOfHeapReserve is not None else []
        self.sizeOfHeapReserve = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.sizeOfHeapReserve]

        if not isinstance(self.sizeOfImage, list):
            self.sizeOfImage = [self.sizeOfImage] if self.sizeOfImage is not None else []
        self.sizeOfImage = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.sizeOfImage]

        if not isinstance(self.sizeOfInitializedData, list):
            self.sizeOfInitializedData = [self.sizeOfInitializedData] if self.sizeOfInitializedData is not None else []
        self.sizeOfInitializedData = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.sizeOfInitializedData]

        if not isinstance(self.sizeOfStackCommit, list):
            self.sizeOfStackCommit = [self.sizeOfStackCommit] if self.sizeOfStackCommit is not None else []
        self.sizeOfStackCommit = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.sizeOfStackCommit]

        if not isinstance(self.sizeOfStackReserve, list):
            self.sizeOfStackReserve = [self.sizeOfStackReserve] if self.sizeOfStackReserve is not None else []
        self.sizeOfStackReserve = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.sizeOfStackReserve]

        if not isinstance(self.sizeOfUninitializedData, list):
            self.sizeOfUninitializedData = [self.sizeOfUninitializedData] if self.sizeOfUninitializedData is not None else []
        self.sizeOfUninitializedData = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.sizeOfUninitializedData]

        if not isinstance(self.subsystem, list):
            self.subsystem = [self.subsystem] if self.subsystem is not None else []
        self.subsystem = [v if isinstance(v, UcoUnsignedShort) else UcoUnsignedShort(v) for v in self.subsystem]

        if not isinstance(self.win32VersionValue, list):
            self.win32VersionValue = [self.win32VersionValue] if self.win32VersionValue is not None else []
        self.win32VersionValue = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.win32VersionValue]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsPESection(UcoInherentCharacterizationThing):
    """
    A Windows PE section is a grouping of characteristics unique to a specific default or custom-defined region of a
    Windows PE (Portable Executable) file, consisting of an individual portion of the actual executable content of the
    file delineated according to unique purpose and memory protection requirements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsPESection"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsPESection"
    class_name: ClassVar[str] = "WindowsPESection"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsPESection

    entropy: Optional[Decimal] = None
    hashes: Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]] = empty_list()
    name: Optional[str] = None
    size: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.entropy is not None and not isinstance(self.entropy, Decimal):
            self.entropy = Decimal(self.entropy)

        self._normalize_inlined_as_list(slot_name="hashes", slot_type=Hash, key_name="hashMethod", keyed=False)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsPrefetch(ObservableObject):
    """
    The Windows prefetch contains entries in a Windows prefetch file (used to speed up application startup starting
    with Windows XP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsPrefetch"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsPrefetch"
    class_name: ClassVar[str] = "WindowsPrefetch"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsPrefetch

    id: Union[str, WindowsPrefetchId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsPrefetchId):
            self.id = WindowsPrefetchId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsPrefetchFacet(Facet):
    """
    A Windows prefetch facet is a grouping of characteristics unique to entries in the Windows prefetch file (used to
    speed up application startup starting with Windows XP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsPrefetchFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsPrefetchFacet"
    class_name: ClassVar[str] = "WindowsPrefetchFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsPrefetchFacet

    accessedDirectory: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    accessedFile: Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]] = empty_list()
    applicationFileName: Optional[str] = None
    firstRun: Optional[Union[str, XSDDateTime]] = None
    lastRun: Optional[Union[str, XSDDateTime]] = None
    prefetchHash: Optional[str] = None
    timesExecuted: Optional[int] = None
    volume: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.accessedDirectory, list):
            self.accessedDirectory = [self.accessedDirectory] if self.accessedDirectory is not None else []
        self.accessedDirectory = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.accessedDirectory]

        if not isinstance(self.accessedFile, list):
            self.accessedFile = [self.accessedFile] if self.accessedFile is not None else []
        self.accessedFile = [v if isinstance(v, ObservableObjectId) else ObservableObjectId(v) for v in self.accessedFile]

        if self.applicationFileName is not None and not isinstance(self.applicationFileName, str):
            self.applicationFileName = str(self.applicationFileName)

        if self.firstRun is not None and not isinstance(self.firstRun, XSDDateTime):
            self.firstRun = XSDDateTime(self.firstRun)

        if self.lastRun is not None and not isinstance(self.lastRun, XSDDateTime):
            self.lastRun = XSDDateTime(self.lastRun)

        if self.prefetchHash is not None and not isinstance(self.prefetchHash, str):
            self.prefetchHash = str(self.prefetchHash)

        if self.timesExecuted is not None and not isinstance(self.timesExecuted, int):
            self.timesExecuted = int(self.timesExecuted)

        if self.volume is not None and not isinstance(self.volume, ObservableObjectId):
            self.volume = ObservableObjectId(self.volume)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsProcess(Process):
    """
    A Windows process is a program running on a Windows operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsProcess"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsProcess"
    class_name: ClassVar[str] = "WindowsProcess"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsProcess

    id: Union[str, WindowsProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsProcessId):
            self.id = WindowsProcessId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsProcessFacet(Facet):
    """
    A Windows process facet is a grouping of characteristics unique to a program running on a Windows operating system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsProcessFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsProcessFacet"
    class_name: ClassVar[str] = "WindowsProcessFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsProcessFacet

    aslrEnabled: Optional[Union[bool, Bool]] = None
    depEnabled: Optional[Union[bool, Bool]] = None
    ownerSID: Optional[str] = None
    priority: Optional[str] = None
    startupInfo: Optional[Union[dict, Dictionary]] = None
    windowTitle: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.aslrEnabled is not None and not isinstance(self.aslrEnabled, Bool):
            self.aslrEnabled = Bool(self.aslrEnabled)

        if self.depEnabled is not None and not isinstance(self.depEnabled, Bool):
            self.depEnabled = Bool(self.depEnabled)

        if self.ownerSID is not None and not isinstance(self.ownerSID, str):
            self.ownerSID = str(self.ownerSID)

        if self.priority is not None and not isinstance(self.priority, str):
            self.priority = str(self.priority)

        if self.startupInfo is not None and not isinstance(self.startupInfo, Dictionary):
            self.startupInfo = Dictionary(**as_dict(self.startupInfo))

        if self.windowTitle is not None and not isinstance(self.windowTitle, str):
            self.windowTitle = str(self.windowTitle)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsRegistryHive(ObservableObject):
    """
    The Windows registry hive is a particular logical group of keys, subkeys, and values in a Windows registry (a
    hierarchical database that stores low-level settings for the Microsoft Windows operating system and for
    applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsRegistryHive"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsRegistryHive"
    class_name: ClassVar[str] = "WindowsRegistryHive"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsRegistryHive

    id: Union[str, WindowsRegistryHiveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsRegistryHiveId):
            self.id = WindowsRegistryHiveId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsRegistryHiveFacet(Facet):
    """
    A Windows registry hive facet is a grouping of characteristics unique to a particular logical group of keys,
    subkeys, and values in a Windows registry (a hierarchical database that stores low-level settings for the
    Microsoft Windows operating system and for applications that opt to use the registry). [based on
    https://en.wikipedia.org/wiki/Windows_Registry]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsRegistryHiveFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsRegistryHiveFacet"
    class_name: ClassVar[str] = "WindowsRegistryHiveFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsRegistryHiveFacet

    hiveType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.hiveType is not None and not isinstance(self.hiveType, str):
            self.hiveType = str(self.hiveType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsRegistryKey(ObservableObject):
    """
    A Windows registry key is a particular key within a Windows registry (a hierarchical database that stores
    low-level settings for the Microsoft Windows operating system and for applications that opt to use the registry).
    [based on https://en.wikipedia.org/wiki/Windows_Registry]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsRegistryKey"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsRegistryKey"
    class_name: ClassVar[str] = "WindowsRegistryKey"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsRegistryKey

    id: Union[str, WindowsRegistryKeyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsRegistryKeyId):
            self.id = WindowsRegistryKeyId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsRegistryKeyFacet(Facet):
    """
    A Windows registry key facet is a grouping of characteristics unique to a particular key within a Windows registry
    (A hierarchical database that stores low-level settings for the Microsoft Windows operating system and for
    applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsRegistryKeyFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsRegistryKeyFacet"
    class_name: ClassVar[str] = "WindowsRegistryKeyFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsRegistryKeyFacet

    numberOfSubkeys: Optional[int] = None
    observable_creator: Optional[Union[str, ObservableObjectId]] = None
    observable_key: Optional[str] = None
    observable_modifiedTime: Optional[Union[str, XSDDateTime]] = None
    registryValues: Optional[Union[Union[dict, "WindowsRegistryValue"], list[Union[dict, "WindowsRegistryValue"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.numberOfSubkeys is not None and not isinstance(self.numberOfSubkeys, int):
            self.numberOfSubkeys = int(self.numberOfSubkeys)

        if self.observable_creator is not None and not isinstance(self.observable_creator, ObservableObjectId):
            self.observable_creator = ObservableObjectId(self.observable_creator)

        if self.observable_key is not None and not isinstance(self.observable_key, str):
            self.observable_key = str(self.observable_key)

        if self.observable_modifiedTime is not None and not isinstance(self.observable_modifiedTime, XSDDateTime):
            self.observable_modifiedTime = XSDDateTime(self.observable_modifiedTime)

        if not isinstance(self.registryValues, list):
            self.registryValues = [self.registryValues] if self.registryValues is not None else []
        self.registryValues = [v if isinstance(v, WindowsRegistryValue) else WindowsRegistryValue(**as_dict(v)) for v in self.registryValues]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsRegistryValue(UcoInherentCharacterizationThing):
    """
    A Windows registry value is a grouping of characteristics unique to a particular value within a Windows registry
    (a hierarchical database that stores low-level settings for the Microsoft Windows operating system and for
    applications that opt to use the registry. [based on https://en.wikipedia.org/wiki/Windows_Registry]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsRegistryValue"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsRegistryValue"
    class_name: ClassVar[str] = "WindowsRegistryValue"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsRegistryValue

    data: Optional[str] = None
    dataType: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.data is not None and not isinstance(self.data, str):
            self.data = str(self.data)

        if self.dataType is not None and not isinstance(self.dataType, str):
            self.dataType = str(self.dataType)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsService(ObservableObject):
    """
    A Windows service is a specific Windows service (a computer program that operates in the background of a Windows
    operating system, similar to the way a UNIX daemon runs on UNIX). [based on
    https://en.wikipedia.org/wiki/Windows_service]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsService"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsService"
    class_name: ClassVar[str] = "WindowsService"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsService

    id: Union[str, WindowsServiceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsServiceId):
            self.id = WindowsServiceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsServiceFacet(Facet):
    """
    A Windows service facet is a grouping of characteristics unique to a specific Windows service (a computer program
    that operates in the background of a Windows operating system, similar to the way a UNIX daemon runs on UNIX).
    [based on https://en.wikipedia.org/wiki/Windows_service]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsServiceFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsServiceFacet"
    class_name: ClassVar[str] = "WindowsServiceFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsServiceFacet

    descriptions: Optional[Union[str, list[str]]] = empty_list()
    displayName: Optional[str] = None
    groupName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceStatus: Optional[str] = None
    serviceType: Optional[str] = None
    startCommandLine: Optional[str] = None
    startType: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.descriptions, list):
            self.descriptions = [self.descriptions] if self.descriptions is not None else []
        self.descriptions = [v if isinstance(v, str) else str(v) for v in self.descriptions]

        if self.displayName is not None and not isinstance(self.displayName, str):
            self.displayName = str(self.displayName)

        if self.groupName is not None and not isinstance(self.groupName, str):
            self.groupName = str(self.groupName)

        if self.serviceName is not None and not isinstance(self.serviceName, str):
            self.serviceName = str(self.serviceName)

        if self.serviceStatus is not None and not isinstance(self.serviceStatus, str):
            self.serviceStatus = str(self.serviceStatus)

        if self.serviceType is not None and not isinstance(self.serviceType, str):
            self.serviceType = str(self.serviceType)

        if self.startCommandLine is not None and not isinstance(self.startCommandLine, str):
            self.startCommandLine = str(self.startCommandLine)

        if self.startType is not None and not isinstance(self.startType, str):
            self.startType = str(self.startType)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsSystemRestore(ObservableObject):
    """
    A Windows system restore is a capture of a Windows computer's state (including system files, installed
    applications, Windows Registry, and system settings) at a particular point in time such that the computer can be
    reverted to that state in the event of system malfunctions or other problems. [based on
    https://en.wikipedia.org/wiki/System_Restore]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsSystemRestore"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsSystemRestore"
    class_name: ClassVar[str] = "WindowsSystemRestore"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsSystemRestore

    id: Union[str, WindowsSystemRestoreId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsSystemRestoreId):
            self.id = WindowsSystemRestoreId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsTask(ObservableObject):
    """
    A Windows task is a process that is scheduled to execute on a Windows operating system by the Windows Task
    Scheduler. [based on http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsTask"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsTask"
    class_name: ClassVar[str] = "WindowsTask"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsTask

    id: Union[str, WindowsTaskId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsTaskId):
            self.id = WindowsTaskId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsTaskFacet(Facet):
    """
    A Windows Task facet is a grouping of characteristics unique to a Windows Task (a process that is scheduled to
    execute on a Windows operating system by the Windows Task Scheduler). [based on
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsTaskFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsTaskFacet"
    class_name: ClassVar[str] = "WindowsTaskFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsTaskFacet

    account: Optional[Union[str, ObservableObjectId]] = None
    accountLogonType: Optional[str] = None
    accountRunLevel: Optional[str] = None
    actionList: Optional[Union[Union[dict, TaskActionType], list[Union[dict, TaskActionType]]]] = empty_list()
    application: Optional[Union[str, ObservableObjectId]] = None
    exitCode: Optional[int] = None
    flags: Optional[Union[str, list[str]]] = empty_list()
    imageName: Optional[str] = None
    maxRunTime: Optional[int] = None
    mostRecentRunTime: Optional[Union[str, XSDDateTime]] = None
    nextRunTime: Optional[Union[str, XSDDateTime]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    parameters: Optional[str] = None
    priority: Optional[Union[str, "TaskPriorityVocab", int]] = None
    status: Optional[Union[str, "TaskStatusVocab"]] = None
    taskComment: Optional[str] = None
    taskCreator: Optional[str] = None
    triggerList: Optional[Union[Union[dict, TriggerType], list[Union[dict, TriggerType]]]] = empty_list()
    workItemData: Optional[Union[str, ObservableObjectId]] = None
    workingDirectory: Optional[Union[str, ObservableObjectId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.account is not None and not isinstance(self.account, ObservableObjectId):
            self.account = ObservableObjectId(self.account)

        if self.accountLogonType is not None and not isinstance(self.accountLogonType, str):
            self.accountLogonType = str(self.accountLogonType)

        if self.accountRunLevel is not None and not isinstance(self.accountRunLevel, str):
            self.accountRunLevel = str(self.accountRunLevel)

        if not isinstance(self.actionList, list):
            self.actionList = [self.actionList] if self.actionList is not None else []
        self.actionList = [v if isinstance(v, TaskActionType) else TaskActionType(**as_dict(v)) for v in self.actionList]

        if self.application is not None and not isinstance(self.application, ObservableObjectId):
            self.application = ObservableObjectId(self.application)

        if self.exitCode is not None and not isinstance(self.exitCode, int):
            self.exitCode = int(self.exitCode)

        if not isinstance(self.flags, list):
            self.flags = [self.flags] if self.flags is not None else []
        self.flags = [v if isinstance(v, str) else str(v) for v in self.flags]

        if self.imageName is not None and not isinstance(self.imageName, str):
            self.imageName = str(self.imageName)

        if self.maxRunTime is not None and not isinstance(self.maxRunTime, int):
            self.maxRunTime = int(self.maxRunTime)

        if self.mostRecentRunTime is not None and not isinstance(self.mostRecentRunTime, XSDDateTime):
            self.mostRecentRunTime = XSDDateTime(self.mostRecentRunTime)

        if self.nextRunTime is not None and not isinstance(self.nextRunTime, XSDDateTime):
            self.nextRunTime = XSDDateTime(self.nextRunTime)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.parameters is not None and not isinstance(self.parameters, str):
            self.parameters = str(self.parameters)

        if self.priority is not None and not isinstance(self.priority, (TaskPriorityVocab, int, str)):
            value = self.priority
            for _coerce in (lambda: TaskPriorityVocab(value), lambda: int(value), lambda: str(value)):
                try:
                    self.priority = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[TaskPriorityVocab, int, str] could be constructed from {value!r} for slot priority")

        if self.status is not None and not isinstance(self.status, TaskStatusVocab):
            self.status = TaskStatusVocab(self.status)

        if self.taskComment is not None and not isinstance(self.taskComment, str):
            self.taskComment = str(self.taskComment)

        if self.taskCreator is not None and not isinstance(self.taskCreator, str):
            self.taskCreator = str(self.taskCreator)

        if not isinstance(self.triggerList, list):
            self.triggerList = [self.triggerList] if self.triggerList is not None else []
        self.triggerList = [v if isinstance(v, TriggerType) else TriggerType(**as_dict(v)) for v in self.triggerList]

        if self.workItemData is not None and not isinstance(self.workItemData, ObservableObjectId):
            self.workItemData = ObservableObjectId(self.workItemData)

        if self.workingDirectory is not None and not isinstance(self.workingDirectory, ObservableObjectId):
            self.workingDirectory = ObservableObjectId(self.workingDirectory)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsThread(ProcessThread):
    """
    A Windows thread is a single thread of execution within a Windows process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsThread"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsThread"
    class_name: ClassVar[str] = "WindowsThread"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsThread

    id: Union[str, WindowsThreadId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsThreadId):
            self.id = WindowsThreadId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsThreadFacet(Facet):
    """
    A Windows thread facet is a grouping os characteristics unique to a single thread of execution within a Windows
    process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsThreadFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsThreadFacet"
    class_name: ClassVar[str] = "WindowsThreadFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsThreadFacet

    creationFlags: Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]] = empty_list()
    creationTime: Optional[Union[str, XSDDateTime]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    observable_context: Optional[str] = None
    parameterAddress: Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]] = empty_list()
    priority: Optional[int] = None
    runningStatus: Optional[str] = None
    securityAttributes: Optional[str] = None
    stackSize: Optional[Union[Union[int, UcoNonNegativeInteger], list[Union[int, UcoNonNegativeInteger]]]] = empty_list()
    startAddress: Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]] = empty_list()
    threadID: Optional[Union[Union[int, UcoNonNegativeInteger], list[Union[int, UcoNonNegativeInteger]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.creationFlags, list):
            self.creationFlags = [self.creationFlags] if self.creationFlags is not None else []
        self.creationFlags = [v if isinstance(v, UcoUnsignedInt) else UcoUnsignedInt(v) for v in self.creationFlags]

        if self.creationTime is not None and not isinstance(self.creationTime, XSDDateTime):
            self.creationTime = XSDDateTime(self.creationTime)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.observable_context is not None and not isinstance(self.observable_context, str):
            self.observable_context = str(self.observable_context)

        if not isinstance(self.parameterAddress, list):
            self.parameterAddress = [self.parameterAddress] if self.parameterAddress is not None else []
        self.parameterAddress = [v if isinstance(v, UcoHexBinary) else UcoHexBinary(v) for v in self.parameterAddress]

        if self.priority is not None and not isinstance(self.priority, int):
            self.priority = int(self.priority)

        if self.runningStatus is not None and not isinstance(self.runningStatus, str):
            self.runningStatus = str(self.runningStatus)

        if self.securityAttributes is not None and not isinstance(self.securityAttributes, str):
            self.securityAttributes = str(self.securityAttributes)

        if not isinstance(self.stackSize, list):
            self.stackSize = [self.stackSize] if self.stackSize is not None else []
        self.stackSize = [v if isinstance(v, UcoNonNegativeInteger) else UcoNonNegativeInteger(v) for v in self.stackSize]

        if not isinstance(self.startAddress, list):
            self.startAddress = [self.startAddress] if self.startAddress is not None else []
        self.startAddress = [v if isinstance(v, UcoHexBinary) else UcoHexBinary(v) for v in self.startAddress]

        if not isinstance(self.threadID, list):
            self.threadID = [self.threadID] if self.threadID is not None else []
        self.threadID = [v if isinstance(v, UcoNonNegativeInteger) else UcoNonNegativeInteger(v) for v in self.threadID]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsVolumeFacet(Facet):
    """
    A Windows volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a
    single Windows file system. [based on https://en.wikipedia.org/wiki/Volume_(computing)]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsVolumeFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsVolumeFacet"
    class_name: ClassVar[str] = "WindowsVolumeFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsVolumeFacet

    driveLetter: Optional[str] = None
    driveType: Optional[Union[str, "WindowsDriveTypeVocab"]] = None
    windowsVolumeAttributes: Optional[Union[Union[str, "WindowsVolumeAttributeVocab"], list[Union[str, "WindowsVolumeAttributeVocab"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.driveLetter is not None and not isinstance(self.driveLetter, str):
            self.driveLetter = str(self.driveLetter)

        if self.driveType is not None and not isinstance(self.driveType, (WindowsDriveTypeVocab, str)):
            value = self.driveType
            for _coerce in (lambda: WindowsDriveTypeVocab(value), lambda: str(value)):
                try:
                    self.driveType = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[WindowsDriveTypeVocab, str] could be constructed from {value!r} for slot driveType")

        if not isinstance(self.windowsVolumeAttributes, list):
            self.windowsVolumeAttributes = [self.windowsVolumeAttributes] if self.windowsVolumeAttributes is not None else []
        self.windowsVolumeAttributes = [v if isinstance(v, WindowsVolumeAttributeVocab) else WindowsVolumeAttributeVocab(v) for v in self.windowsVolumeAttributes]

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WindowsWaitableTime(ObservableObject):
    """
    A Windows waitable timer is a synchronization object within the Windows operating system whose state is set to
    signaled when a specified due time arrives. There are two types of waitable timers that can be created:
    manual-reset and synchronization. A timer of either type can also be a periodic timer. [based on
    https://docs.microsoft.com/en-us/windows/win32/sync/waitable-timer-objects]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WindowsWaitableTime"]
    class_class_curie: ClassVar[str] = "uco-observable:WindowsWaitableTime"
    class_name: ClassVar[str] = "WindowsWaitableTime"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WindowsWaitableTime

    id: Union[str, WindowsWaitableTimeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WindowsWaitableTimeId):
            self.id = WindowsWaitableTimeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WirelessNetworkConnection(NetworkConnection):
    """
    A wireless network connection is a connection (completed or attempted) across an IEEE 802.11 standards-confromant
    digital network (a group of two or more computer systems linked together). [based on
    https://www.webopedia.com/TERM/N/network.html]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WirelessNetworkConnection"]
    class_class_curie: ClassVar[str] = "uco-observable:WirelessNetworkConnection"
    class_name: ClassVar[str] = "WirelessNetworkConnection"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WirelessNetworkConnection

    id: Union[str, WirelessNetworkConnectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WirelessNetworkConnectionId):
            self.id = WirelessNetworkConnectionId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WirelessNetworkConnectionFacet(Facet):
    """
    A wireless network connection facet is a grouping of characteristics unique to a connection (completed or
    attempted) across an IEEE 802.11 standards-conformant digital network (a group of two or more computer systems
    linked together). [based on https://www.webopedia.com/TERM/N/network.html]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WirelessNetworkConnectionFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:WirelessNetworkConnectionFacet"
    class_name: ClassVar[str] = "WirelessNetworkConnectionFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WirelessNetworkConnectionFacet

    baseStation: Optional[str] = None
    password: Optional[str] = None
    ssid: Optional[str] = None
    wirelessNetworkSecurityMode: Optional[Union[str, "WirelessNetworkSecurityModeVocab"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.baseStation is not None and not isinstance(self.baseStation, str):
            self.baseStation = str(self.baseStation)

        if self.password is not None and not isinstance(self.password, str):
            self.password = str(self.password)

        if self.ssid is not None and not isinstance(self.ssid, str):
            self.ssid = str(self.ssid)

        if self.wirelessNetworkSecurityMode is not None and not isinstance(self.wirelessNetworkSecurityMode, (WirelessNetworkSecurityModeVocab, str)):
            value = self.wirelessNetworkSecurityMode
            for _coerce in (lambda: WirelessNetworkSecurityModeVocab(value), lambda: str(value)):
                try:
                    self.wirelessNetworkSecurityMode = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[WirelessNetworkSecurityModeVocab, str] could be constructed from {value!r} for slot wirelessNetworkSecurityMode")

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class WriteBlocker(Device):
    """
    A write blocker is a device that allows read-only access to storage mediums in order to preserve the integrity of
    the data being analyzed. Examples include Tableau, Cellibrite, Talon, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["WriteBlocker"]
    class_class_curie: ClassVar[str] = "uco-observable:WriteBlocker"
    class_name: ClassVar[str] = "WriteBlocker"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.WriteBlocker

    id: Union[str, WriteBlockerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WriteBlockerId):
            self.id = WriteBlockerId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class X509Certificate(ObservableObject):
    """
    A X.509 certificate is a public key digital identity certificate conformant to the X.509 PKI (Public Key
    Infrastructure) standard.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["X509Certificate"]
    class_class_curie: ClassVar[str] = "uco-observable:X509Certificate"
    class_name: ClassVar[str] = "X509Certificate"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.X509Certificate

    id: Union[str, X509CertificateId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, X509CertificateId):
            self.id = X509CertificateId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class X509CertificateFacet(Facet):
    """
    A X.509 certificate facet is a grouping of characteristics unique to a public key digital identity certificate
    conformant to the X.509 PKI (Public Key Infrastructure) standard.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["X509CertificateFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:X509CertificateFacet"
    class_name: ClassVar[str] = "X509CertificateFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.X509CertificateFacet

    isSelfSigned: Optional[Union[bool, Bool]] = None
    issuer: Optional[str] = None
    issuerHash: Optional[Union[dict, Hash]] = None
    observable_version: Optional[str] = None
    serialNumber: Optional[str] = None
    signature: Optional[str] = None
    signatureAlgorithm: Optional[str] = None
    subject: Optional[str] = None
    subjectHash: Optional[Union[dict, Hash]] = None
    subjectPublicKeyAlgorithm: Optional[str] = None
    subjectPublicKeyExponent: Optional[int] = None
    subjectPublicKeyModulus: Optional[str] = None
    thumbprintHash: Optional[Union[dict, Hash]] = None
    validityNotAfter: Optional[Union[str, XSDDateTime]] = None
    validityNotBefore: Optional[Union[str, XSDDateTime]] = None
    x509v3extensions: Optional[Union[dict, "X509V3ExtensionsFacet"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.isSelfSigned is not None and not isinstance(self.isSelfSigned, Bool):
            self.isSelfSigned = Bool(self.isSelfSigned)

        if self.issuer is not None and not isinstance(self.issuer, str):
            self.issuer = str(self.issuer)

        if self.issuerHash is not None and not isinstance(self.issuerHash, Hash):
            self.issuerHash = Hash(**as_dict(self.issuerHash))

        if self.observable_version is not None and not isinstance(self.observable_version, str):
            self.observable_version = str(self.observable_version)

        if self.serialNumber is not None and not isinstance(self.serialNumber, str):
            self.serialNumber = str(self.serialNumber)

        if self.signature is not None and not isinstance(self.signature, str):
            self.signature = str(self.signature)

        if self.signatureAlgorithm is not None and not isinstance(self.signatureAlgorithm, str):
            self.signatureAlgorithm = str(self.signatureAlgorithm)

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self.subjectHash is not None and not isinstance(self.subjectHash, Hash):
            self.subjectHash = Hash(**as_dict(self.subjectHash))

        if self.subjectPublicKeyAlgorithm is not None and not isinstance(self.subjectPublicKeyAlgorithm, str):
            self.subjectPublicKeyAlgorithm = str(self.subjectPublicKeyAlgorithm)

        if self.subjectPublicKeyExponent is not None and not isinstance(self.subjectPublicKeyExponent, int):
            self.subjectPublicKeyExponent = int(self.subjectPublicKeyExponent)

        if self.subjectPublicKeyModulus is not None and not isinstance(self.subjectPublicKeyModulus, str):
            self.subjectPublicKeyModulus = str(self.subjectPublicKeyModulus)

        if self.thumbprintHash is not None and not isinstance(self.thumbprintHash, Hash):
            self.thumbprintHash = Hash(**as_dict(self.thumbprintHash))

        if self.validityNotAfter is not None and not isinstance(self.validityNotAfter, XSDDateTime):
            self.validityNotAfter = XSDDateTime(self.validityNotAfter)

        if self.validityNotBefore is not None and not isinstance(self.validityNotBefore, XSDDateTime):
            self.validityNotBefore = XSDDateTime(self.validityNotBefore)

        if self.x509v3extensions is not None and not isinstance(self.x509v3extensions, X509V3ExtensionsFacet):
            self.x509v3extensions = X509V3ExtensionsFacet(**as_dict(self.x509v3extensions))

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class X509V3Certificate(ObservableObject):
    """
    An X.509 v3 certificate is a public key digital identity certificate conformant to the X.509 v3 PKI (Public Key
    Infrastructure) standard.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["X509V3Certificate"]
    class_class_curie: ClassVar[str] = "uco-observable:X509V3Certificate"
    class_name: ClassVar[str] = "X509V3Certificate"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.X509V3Certificate

    id: Union[str, X509V3CertificateId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, X509V3CertificateId):
            self.id = X509V3CertificateId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


@dataclass(repr=False)
class X509V3ExtensionsFacet(Facet):
    """
    An X.509 v3 certificate extensions facet is a grouping of characteristics unique to a public key digital identity
    certificate conformant to the X.509 v3 PKI (Public Key Infrastructure) standard.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UCO_OBSERVABLE["X509V3ExtensionsFacet"]
    class_class_curie: ClassVar[str] = "uco-observable:X509V3ExtensionsFacet"
    class_name: ClassVar[str] = "X509V3ExtensionsFacet"
    class_model_uri: ClassVar[URIRef] = UCO_LINKML.X509V3ExtensionsFacet

    authorityKeyIdentifier: Optional[str] = None
    basicConstraints: Optional[str] = None
    certificatePolicies: Optional[str] = None
    crlDistributionPoints: Optional[str] = None
    extendedKeyUsage: Optional[str] = None
    inhibitAnyPolicy: Optional[str] = None
    issuerAlternativeName: Optional[str] = None
    keyUsage: Optional[str] = None
    nameConstraints: Optional[str] = None
    policyConstraints: Optional[str] = None
    policyMappings: Optional[str] = None
    privateKeyUsagePeriodNotAfter: Optional[Union[str, XSDDateTime]] = None
    privateKeyUsagePeriodNotBefore: Optional[Union[str, XSDDateTime]] = None
    subjectAlternativeName: Optional[str] = None
    subjectDirectoryAttributes: Optional[str] = None
    subjectKeyIdentifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.authorityKeyIdentifier is not None and not isinstance(self.authorityKeyIdentifier, str):
            self.authorityKeyIdentifier = str(self.authorityKeyIdentifier)

        if self.basicConstraints is not None and not isinstance(self.basicConstraints, str):
            self.basicConstraints = str(self.basicConstraints)

        if self.certificatePolicies is not None and not isinstance(self.certificatePolicies, str):
            self.certificatePolicies = str(self.certificatePolicies)

        if self.crlDistributionPoints is not None and not isinstance(self.crlDistributionPoints, str):
            self.crlDistributionPoints = str(self.crlDistributionPoints)

        if self.extendedKeyUsage is not None and not isinstance(self.extendedKeyUsage, str):
            self.extendedKeyUsage = str(self.extendedKeyUsage)

        if self.inhibitAnyPolicy is not None and not isinstance(self.inhibitAnyPolicy, str):
            self.inhibitAnyPolicy = str(self.inhibitAnyPolicy)

        if self.issuerAlternativeName is not None and not isinstance(self.issuerAlternativeName, str):
            self.issuerAlternativeName = str(self.issuerAlternativeName)

        if self.keyUsage is not None and not isinstance(self.keyUsage, str):
            self.keyUsage = str(self.keyUsage)

        if self.nameConstraints is not None and not isinstance(self.nameConstraints, str):
            self.nameConstraints = str(self.nameConstraints)

        if self.policyConstraints is not None and not isinstance(self.policyConstraints, str):
            self.policyConstraints = str(self.policyConstraints)

        if self.policyMappings is not None and not isinstance(self.policyMappings, str):
            self.policyMappings = str(self.policyMappings)

        if self.privateKeyUsagePeriodNotAfter is not None and not isinstance(self.privateKeyUsagePeriodNotAfter, XSDDateTime):
            self.privateKeyUsagePeriodNotAfter = XSDDateTime(self.privateKeyUsagePeriodNotAfter)

        if self.privateKeyUsagePeriodNotBefore is not None and not isinstance(self.privateKeyUsagePeriodNotBefore, XSDDateTime):
            self.privateKeyUsagePeriodNotBefore = XSDDateTime(self.privateKeyUsagePeriodNotBefore)

        if self.subjectAlternativeName is not None and not isinstance(self.subjectAlternativeName, str):
            self.subjectAlternativeName = str(self.subjectAlternativeName)

        if self.subjectDirectoryAttributes is not None and not isinstance(self.subjectDirectoryAttributes, str):
            self.subjectDirectoryAttributes = str(self.subjectDirectoryAttributes)

        if self.subjectKeyIdentifier is not None and not isinstance(self.subjectKeyIdentifier, str):
            self.subjectKeyIdentifier = str(self.subjectKeyIdentifier)

        super().__post_init__(**kwargs)
        self.type = str(self.class_class_curie if self.class_class_curie is not None else self.class_class_uri)


# Enumerations
class ObjectStatusVocab(EnumDefinitionImpl):
    """
    UCO 1.5.0 declares the vocabulary uco-core:ObjectStatusVocab without a definition.
    """
    Draft = PermissibleValue(text="Draft")
    Final = PermissibleValue(text="Final")
    Deprecated = PermissibleValue(text="Deprecated")

    _defn = EnumDefinition(
        name="ObjectStatusVocab",
        description="UCO 1.5.0 declares the vocabulary uco-core:ObjectStatusVocab without a definition.",
    )

class AccountTypeVocab(EnumDefinitionImpl):
    """
    UCO 1.5.0 declares the vocabulary uco-vocabulary:AccountTypeVocab without a definition.
    """
    ldap = PermissibleValue(text="ldap")
    nis = PermissibleValue(text="nis")
    openid = PermissibleValue(text="openid")
    radius = PermissibleValue(text="radius")
    tacacs = PermissibleValue(text="tacacs")
    unix = PermissibleValue(text="unix")
    windows_domain = PermissibleValue(text="windows_domain")
    windows_local = PermissibleValue(text="windows_local")

    _defn = EnumDefinition(
        name="AccountTypeVocab",
        description="UCO 1.5.0 declares the vocabulary uco-vocabulary:AccountTypeVocab without a definition.",
    )

class ActionArgumentNameVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary for common arguments of cyber actions.
    """
    API = PermissibleValue(text="API")
    Command = PermissibleValue(text="Command")
    Flags = PermissibleValue(text="Flags")
    Hostname = PermissibleValue(text="Hostname")
    Options = PermissibleValue(text="Options")
    Password = PermissibleValue(text="Password")
    Protection = PermissibleValue(text="Protection")
    Reason = PermissibleValue(text="Reason")
    Server = PermissibleValue(text="Server")
    Username = PermissibleValue(text="Username")

    _defn = EnumDefinition(
        name="ActionArgumentNameVocab",
        description="Defines an open-vocabulary for common arguments of cyber actions.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "APC Address",
            PermissibleValue(text="APC Address"))
        setattr(cls, "APC Mode",
            PermissibleValue(text="APC Mode"))
        setattr(cls, "Access Mode",
            PermissibleValue(text="Access Mode"))
        setattr(cls, "Application Name",
            PermissibleValue(text="Application Name"))
        setattr(cls, "Base Address",
            PermissibleValue(text="Base Address"))
        setattr(cls, "Callback Address",
            PermissibleValue(text="Callback Address"))
        setattr(cls, "Code Address",
            PermissibleValue(text="Code Address"))
        setattr(cls, "Control Code",
            PermissibleValue(text="Control Code"))
        setattr(cls, "Control Parameter",
            PermissibleValue(text="Control Parameter"))
        setattr(cls, "Creation Flags",
            PermissibleValue(text="Creation Flags"))
        setattr(cls, "Database Name",
            PermissibleValue(text="Database Name"))
        setattr(cls, "Delay Time (ms)",
            PermissibleValue(text="Delay Time (ms)"))
        setattr(cls, "Destination Address",
            PermissibleValue(text="Destination Address"))
        setattr(cls, "Error Control",
            PermissibleValue(text="Error Control"))
        setattr(cls, "File Information Class",
            PermissibleValue(text="File Information Class"))
        setattr(cls, "Function Address",
            PermissibleValue(text="Function Address"))
        setattr(cls, "Function Name",
            PermissibleValue(text="Function Name"))
        setattr(cls, "Function Ordinal",
            PermissibleValue(text="Function Ordinal"))
        setattr(cls, "Hook Type",
            PermissibleValue(text="Hook Type"))
        setattr(cls, "Host Name",
            PermissibleValue(text="Host Name"))
        setattr(cls, "Initial Owner",
            PermissibleValue(text="Initial Owner"))
        setattr(cls, "Mapping Offset",
            PermissibleValue(text="Mapping Offset"))
        setattr(cls, "Number of Bytes Per Send",
            PermissibleValue(text="Number of Bytes Per Send"))
        setattr(cls, "Parameter Address",
            PermissibleValue(text="Parameter Address"))
        setattr(cls, "Privilege Name",
            PermissibleValue(text="Privilege Name"))
        setattr(cls, "Proxy Bypass",
            PermissibleValue(text="Proxy Bypass"))
        setattr(cls, "Proxy Name",
            PermissibleValue(text="Proxy Name"))
        setattr(cls, "Request Size",
            PermissibleValue(text="Request Size"))
        setattr(cls, "Requested Version",
            PermissibleValue(text="Requested Version"))
        setattr(cls, "Service Name",
            PermissibleValue(text="Service Name"))
        setattr(cls, "Service State",
            PermissibleValue(text="Service State"))
        setattr(cls, "Service Type",
            PermissibleValue(text="Service Type"))
        setattr(cls, "Share Mode",
            PermissibleValue(text="Share Mode"))
        setattr(cls, "Shutdown Flag",
            PermissibleValue(text="Shutdown Flag"))
        setattr(cls, "Size (bytes)",
            PermissibleValue(text="Size (bytes)"))
        setattr(cls, "Sleep Time (ms)",
            PermissibleValue(text="Sleep Time (ms)"))
        setattr(cls, "Source Address",
            PermissibleValue(text="Source Address"))
        setattr(cls, "Starting Address",
            PermissibleValue(text="Starting Address"))
        setattr(cls, "System Metric Index",
            PermissibleValue(text="System Metric Index"))
        setattr(cls, "Target PID",
            PermissibleValue(text="Target PID"))
        setattr(cls, "Transfer Flags",
            PermissibleValue(text="Transfer Flags"))

class ActionNameVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of common specific cyber action names.
    """
    _defn = EnumDefinition(
        name="ActionNameVocab",
        description="Defines an open-vocabulary of common specific cyber action names.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Accept Socket Connection",
            PermissibleValue(text="Accept Socket Connection"))
        setattr(cls, "Add Connection to Network Share",
            PermissibleValue(text="Add Connection to Network Share"))
        setattr(cls, "Add Network Share",
            PermissibleValue(text="Add Network Share"))
        setattr(cls, "Add Scheduled Task",
            PermissibleValue(text="Add Scheduled Task"))
        setattr(cls, "Add System Call Hook",
            PermissibleValue(text="Add System Call Hook"))
        setattr(cls, "Add User",
            PermissibleValue(text="Add User"))
        setattr(cls, "Add Windows Hook",
            PermissibleValue(text="Add Windows Hook"))
        setattr(cls, "Allocate Virtual Memory in Process",
            PermissibleValue(text="Allocate Virtual Memory in Process"))
        setattr(cls, "Bind Address to Socket",
            PermissibleValue(text="Bind Address to Socket"))
        setattr(cls, "Change Service Configuration",
            PermissibleValue(text="Change Service Configuration"))
        setattr(cls, "Check for Remote Debugger",
            PermissibleValue(text="Check for Remote Debugger"))
        setattr(cls, "Close Port",
            PermissibleValue(text="Close Port"))
        setattr(cls, "Close Registry Key",
            PermissibleValue(text="Close Registry Key"))
        setattr(cls, "Close Socket",
            PermissibleValue(text="Close Socket"))
        setattr(cls, "Configure Service",
            PermissibleValue(text="Configure Service"))
        setattr(cls, "Connect to IP",
            PermissibleValue(text="Connect to IP"))
        setattr(cls, "Connect to Named Pipe",
            PermissibleValue(text="Connect to Named Pipe"))
        setattr(cls, "Connect to Network Share",
            PermissibleValue(text="Connect to Network Share"))
        setattr(cls, "Connect to Socket",
            PermissibleValue(text="Connect to Socket"))
        setattr(cls, "Connect to URL",
            PermissibleValue(text="Connect to URL"))
        setattr(cls, "Control Driver",
            PermissibleValue(text="Control Driver"))
        setattr(cls, "Control Service",
            PermissibleValue(text="Control Service"))
        setattr(cls, "Copy File",
            PermissibleValue(text="Copy File"))
        setattr(cls, "Create Dialog Box",
            PermissibleValue(text="Create Dialog Box"))
        setattr(cls, "Create Directory",
            PermissibleValue(text="Create Directory"))
        setattr(cls, "Create Event",
            PermissibleValue(text="Create Event"))
        setattr(cls, "Create File",
            PermissibleValue(text="Create File"))
        setattr(cls, "Create File Alternate Data Stream",
            PermissibleValue(text="Create File Alternate Data Stream"))
        setattr(cls, "Create File Mapping",
            PermissibleValue(text="Create File Mapping"))
        setattr(cls, "Create File Symbolic Link",
            PermissibleValue(text="Create File Symbolic Link"))
        setattr(cls, "Create Hidden File",
            PermissibleValue(text="Create Hidden File"))
        setattr(cls, "Create Mailslot",
            PermissibleValue(text="Create Mailslot"))
        setattr(cls, "Create Module",
            PermissibleValue(text="Create Module"))
        setattr(cls, "Create Mutex",
            PermissibleValue(text="Create Mutex"))
        setattr(cls, "Create Named Pipe",
            PermissibleValue(text="Create Named Pipe"))
        setattr(cls, "Create Process",
            PermissibleValue(text="Create Process"))
        setattr(cls, "Create Process as User",
            PermissibleValue(text="Create Process as User"))
        setattr(cls, "Create Registry Key",
            PermissibleValue(text="Create Registry Key"))
        setattr(cls, "Create Registry Key Value",
            PermissibleValue(text="Create Registry Key Value"))
        setattr(cls, "Create Remote Thread in Process",
            PermissibleValue(text="Create Remote Thread in Process"))
        setattr(cls, "Create Service",
            PermissibleValue(text="Create Service"))
        setattr(cls, "Create Socket",
            PermissibleValue(text="Create Socket"))
        setattr(cls, "Create Symbolic Link",
            PermissibleValue(text="Create Symbolic Link"))
        setattr(cls, "Create Thread",
            PermissibleValue(text="Create Thread"))
        setattr(cls, "Create Window",
            PermissibleValue(text="Create Window"))
        setattr(cls, "Delete Directory",
            PermissibleValue(text="Delete Directory"))
        setattr(cls, "Delete File",
            PermissibleValue(text="Delete File"))
        setattr(cls, "Delete Named Pipe",
            PermissibleValue(text="Delete Named Pipe"))
        setattr(cls, "Delete Network Share",
            PermissibleValue(text="Delete Network Share"))
        setattr(cls, "Delete Registry Key",
            PermissibleValue(text="Delete Registry Key"))
        setattr(cls, "Delete Registry Key Value",
            PermissibleValue(text="Delete Registry Key Value"))
        setattr(cls, "Delete Service",
            PermissibleValue(text="Delete Service"))
        setattr(cls, "Delete User",
            PermissibleValue(text="Delete User"))
        setattr(cls, "Disconnect from Named Pipe",
            PermissibleValue(text="Disconnect from Named Pipe"))
        setattr(cls, "Disconnect from Network Share",
            PermissibleValue(text="Disconnect from Network Share"))
        setattr(cls, "Disconnect from Socket",
            PermissibleValue(text="Disconnect from Socket"))
        setattr(cls, "Download File",
            PermissibleValue(text="Download File"))
        setattr(cls, "Enumerate DLLs",
            PermissibleValue(text="Enumerate DLLs"))
        setattr(cls, "Enumerate Network Shares",
            PermissibleValue(text="Enumerate Network Shares"))
        setattr(cls, "Enumerate Processes",
            PermissibleValue(text="Enumerate Processes"))
        setattr(cls, "Enumerate Protocols",
            PermissibleValue(text="Enumerate Protocols"))
        setattr(cls, "Enumerate Registry Key Subkeys",
            PermissibleValue(text="Enumerate Registry Key Subkeys"))
        setattr(cls, "Enumerate Registry Key Values",
            PermissibleValue(text="Enumerate Registry Key Values"))
        setattr(cls, "Enumerate Services",
            PermissibleValue(text="Enumerate Services"))
        setattr(cls, "Enumerate System Handles",
            PermissibleValue(text="Enumerate System Handles"))
        setattr(cls, "Enumerate Threads",
            PermissibleValue(text="Enumerate Threads"))
        setattr(cls, "Enumerate Threads in Process",
            PermissibleValue(text="Enumerate Threads in Process"))
        setattr(cls, "Enumerate Users",
            PermissibleValue(text="Enumerate Users"))
        setattr(cls, "Enumerate Windows",
            PermissibleValue(text="Enumerate Windows"))
        setattr(cls, "Find File",
            PermissibleValue(text="Find File"))
        setattr(cls, "Find Window",
            PermissibleValue(text="Find Window"))
        setattr(cls, "Flush Process Instruction Cache",
            PermissibleValue(text="Flush Process Instruction Cache"))
        setattr(cls, "Free Library",
            PermissibleValue(text="Free Library"))
        setattr(cls, "Free Process Virtual Memory",
            PermissibleValue(text="Free Process Virtual Memory"))
        setattr(cls, "Get Disk Free Space",
            PermissibleValue(text="Get Disk Free Space"))
        setattr(cls, "Get Disk Type",
            PermissibleValue(text="Get Disk Type"))
        setattr(cls, "Get Elapsed System Up Time",
            PermissibleValue(text="Get Elapsed System Up Time"))
        setattr(cls, "Get File Attributes",
            PermissibleValue(text="Get File Attributes"))
        setattr(cls, "Get Function Address",
            PermissibleValue(text="Get Function Address"))
        setattr(cls, "Get Host By Address",
            PermissibleValue(text="Get Host By Address"))
        setattr(cls, "Get Host By Name",
            PermissibleValue(text="Get Host By Name"))
        setattr(cls, "Get Host Name",
            PermissibleValue(text="Get Host Name"))
        setattr(cls, "Get Library File Name",
            PermissibleValue(text="Get Library File Name"))
        setattr(cls, "Get Library Handle",
            PermissibleValue(text="Get Library Handle"))
        setattr(cls, "Get NetBIOS Name",
            PermissibleValue(text="Get NetBIOS Name"))
        setattr(cls, "Get Process Current Directory",
            PermissibleValue(text="Get Process Current Directory"))
        setattr(cls, "Get Process Environment Variable",
            PermissibleValue(text="Get Process Environment Variable"))
        setattr(cls, "Get Process Startup Information",
            PermissibleValue(text="Get Process Startup Information"))
        setattr(cls, "Get Processes Snapshot",
            PermissibleValue(text="Get Processes Snapshot"))
        setattr(cls, "Get Registry Key Attributes",
            PermissibleValue(text="Get Registry Key Attributes"))
        setattr(cls, "Get Service Status",
            PermissibleValue(text="Get Service Status"))
        setattr(cls, "Get System Global Flags",
            PermissibleValue(text="Get System Global Flags"))
        setattr(cls, "Get System Host Name",
            PermissibleValue(text="Get System Host Name"))
        setattr(cls, "Get System Local Time",
            PermissibleValue(text="Get System Local Time"))
        setattr(cls, "Get System NetBIOS Name",
            PermissibleValue(text="Get System NetBIOS Name"))
        setattr(cls, "Get System Network Parameters",
            PermissibleValue(text="Get System Network Parameters"))
        setattr(cls, "Get System Time",
            PermissibleValue(text="Get System Time"))
        setattr(cls, "Get Thread Context",
            PermissibleValue(text="Get Thread Context"))
        setattr(cls, "Get Thread Username",
            PermissibleValue(text="Get Thread Username"))
        setattr(cls, "Get User Attributes",
            PermissibleValue(text="Get User Attributes"))
        setattr(cls, "Get Username",
            PermissibleValue(text="Get Username"))
        setattr(cls, "Get Windows Directory",
            PermissibleValue(text="Get Windows Directory"))
        setattr(cls, "Get Windows System Directory",
            PermissibleValue(text="Get Windows System Directory"))
        setattr(cls, "Get Windows Temporary Files Directory",
            PermissibleValue(text="Get Windows Temporary Files Directory"))
        setattr(cls, "Hide Window",
            PermissibleValue(text="Hide Window"))
        setattr(cls, "Impersonate Process",
            PermissibleValue(text="Impersonate Process"))
        setattr(cls, "Impersonate Thread",
            PermissibleValue(text="Impersonate Thread"))
        setattr(cls, "Inject Memory Page",
            PermissibleValue(text="Inject Memory Page"))
        setattr(cls, "Kill Process",
            PermissibleValue(text="Kill Process"))
        setattr(cls, "Kill Thread",
            PermissibleValue(text="Kill Thread"))
        setattr(cls, "Kill Window",
            PermissibleValue(text="Kill Window"))
        setattr(cls, "Listen on Port",
            PermissibleValue(text="Listen on Port"))
        setattr(cls, "Listen on Socket",
            PermissibleValue(text="Listen on Socket"))
        setattr(cls, "Load Driver",
            PermissibleValue(text="Load Driver"))
        setattr(cls, "Load Library",
            PermissibleValue(text="Load Library"))
        setattr(cls, "Load Module",
            PermissibleValue(text="Load Module"))
        setattr(cls, "Load and Call Driver",
            PermissibleValue(text="Load and Call Driver"))
        setattr(cls, "Lock File",
            PermissibleValue(text="Lock File"))
        setattr(cls, "Logon as User",
            PermissibleValue(text="Logon as User"))
        setattr(cls, "Map File",
            PermissibleValue(text="Map File"))
        setattr(cls, "Map Library",
            PermissibleValue(text="Map Library"))
        setattr(cls, "Map View of File",
            PermissibleValue(text="Map View of File"))
        setattr(cls, "Modify File",
            PermissibleValue(text="Modify File"))
        setattr(cls, "Modify Named Pipe",
            PermissibleValue(text="Modify Named Pipe"))
        setattr(cls, "Modify Process",
            PermissibleValue(text="Modify Process"))
        setattr(cls, "Modify Registry Key",
            PermissibleValue(text="Modify Registry Key"))
        setattr(cls, "Modify Registry Key Value",
            PermissibleValue(text="Modify Registry Key Value"))
        setattr(cls, "Modify Service",
            PermissibleValue(text="Modify Service"))
        setattr(cls, "Monitor Registry Key",
            PermissibleValue(text="Monitor Registry Key"))
        setattr(cls, "Move File",
            PermissibleValue(text="Move File"))
        setattr(cls, "Open File",
            PermissibleValue(text="Open File"))
        setattr(cls, "Open File Mapping",
            PermissibleValue(text="Open File Mapping"))
        setattr(cls, "Open Mutex",
            PermissibleValue(text="Open Mutex"))
        setattr(cls, "Open Port",
            PermissibleValue(text="Open Port"))
        setattr(cls, "Open Process",
            PermissibleValue(text="Open Process"))
        setattr(cls, "Open Registry Key",
            PermissibleValue(text="Open Registry Key"))
        setattr(cls, "Open Service",
            PermissibleValue(text="Open Service"))
        setattr(cls, "Open Service Control Manager",
            PermissibleValue(text="Open Service Control Manager"))
        setattr(cls, "Protect Virtual Memory",
            PermissibleValue(text="Protect Virtual Memory"))
        setattr(cls, "Query DNS",
            PermissibleValue(text="Query DNS"))
        setattr(cls, "Query Disk Attributes",
            PermissibleValue(text="Query Disk Attributes"))
        setattr(cls, "Query Process Virtual Memory",
            PermissibleValue(text="Query Process Virtual Memory"))
        setattr(cls, "Queue APC in Thread",
            PermissibleValue(text="Queue APC in Thread"))
        setattr(cls, "Read File",
            PermissibleValue(text="Read File"))
        setattr(cls, "Read From Named Pipe",
            PermissibleValue(text="Read From Named Pipe"))
        setattr(cls, "Read From Process Memory",
            PermissibleValue(text="Read From Process Memory"))
        setattr(cls, "Read Registry Key Value",
            PermissibleValue(text="Read Registry Key Value"))
        setattr(cls, "Receive Data on Socket",
            PermissibleValue(text="Receive Data on Socket"))
        setattr(cls, "Receive Email Message",
            PermissibleValue(text="Receive Email Message"))
        setattr(cls, "Release Mutex",
            PermissibleValue(text="Release Mutex"))
        setattr(cls, "Rename File",
            PermissibleValue(text="Rename File"))
        setattr(cls, "Revert Thread to Self",
            PermissibleValue(text="Revert Thread to Self"))
        setattr(cls, "Send Control Code to File",
            PermissibleValue(text="Send Control Code to File"))
        setattr(cls, "Send Control Code to Pipe",
            PermissibleValue(text="Send Control Code to Pipe"))
        setattr(cls, "Send Control Code to Service",
            PermissibleValue(text="Send Control Code to Service"))
        setattr(cls, "Send DNS Query",
            PermissibleValue(text="Send DNS Query"))
        setattr(cls, "Send Data on Socket",
            PermissibleValue(text="Send Data on Socket"))
        setattr(cls, "Send Data to Address on Socket",
            PermissibleValue(text="Send Data to Address on Socket"))
        setattr(cls, "Send Email Message",
            PermissibleValue(text="Send Email Message"))
        setattr(cls, "Send ICMP Request",
            PermissibleValue(text="Send ICMP Request"))
        setattr(cls, "Send Reverse DNS Query",
            PermissibleValue(text="Send Reverse DNS Query"))
        setattr(cls, "Set File Attributes",
            PermissibleValue(text="Set File Attributes"))
        setattr(cls, "Set NetBIOS Name",
            PermissibleValue(text="Set NetBIOS Name"))
        setattr(cls, "Set Process Current Directory",
            PermissibleValue(text="Set Process Current Directory"))
        setattr(cls, "Set Process Environment Variable",
            PermissibleValue(text="Set Process Environment Variable"))
        setattr(cls, "Set System Global Flags",
            PermissibleValue(text="Set System Global Flags"))
        setattr(cls, "Set System Host Name",
            PermissibleValue(text="Set System Host Name"))
        setattr(cls, "Set System Time",
            PermissibleValue(text="Set System Time"))
        setattr(cls, "Set Thread Context",
            PermissibleValue(text="Set Thread Context"))
        setattr(cls, "Show Window",
            PermissibleValue(text="Show Window"))
        setattr(cls, "Shutdown System",
            PermissibleValue(text="Shutdown System"))
        setattr(cls, "Sleep Process",
            PermissibleValue(text="Sleep Process"))
        setattr(cls, "Sleep System",
            PermissibleValue(text="Sleep System"))
        setattr(cls, "Start Service",
            PermissibleValue(text="Start Service"))
        setattr(cls, "Unload Driver",
            PermissibleValue(text="Unload Driver"))
        setattr(cls, "Unload Module",
            PermissibleValue(text="Unload Module"))
        setattr(cls, "Unlock File",
            PermissibleValue(text="Unlock File"))
        setattr(cls, "Unmap File",
            PermissibleValue(text="Unmap File"))
        setattr(cls, "Upload File",
            PermissibleValue(text="Upload File"))
        setattr(cls, "Write to File",
            PermissibleValue(text="Write to File"))
        setattr(cls, "Write to Process Virtual Memory",
            PermissibleValue(text="Write to Process Virtual Memory"))

class ActionRelationshipTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary for capturing types of relationships between actions.
    """
    Dependent_On = PermissibleValue(text="Dependent_On")
    Equivalent_To = PermissibleValue(text="Equivalent_To")
    Followed_By = PermissibleValue(text="Followed_By")
    Initiated = PermissibleValue(text="Initiated")
    Initiated_By = PermissibleValue(text="Initiated_By")
    Preceded_By = PermissibleValue(text="Preceded_By")
    Related_To = PermissibleValue(text="Related_To")

    _defn = EnumDefinition(
        name="ActionRelationshipTypeVocab",
        description="Defines an open-vocabulary for capturing types of relationships between actions.",
    )

class ActionStatusTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of action status types.
    """
    Error = PermissibleValue(text="Error")
    Fail = PermissibleValue(text="Fail")
    Ongoing = PermissibleValue(text="Ongoing")
    Pending = PermissibleValue(text="Pending")
    Success = PermissibleValue(text="Success")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="ActionStatusTypeVocab",
        description="Defines an open-vocabulary of action status types.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Complete/Finish",
            PermissibleValue(text="Complete/Finish"))

class ActionTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of common general action types.
    """
    Accept = PermissibleValue(text="Accept")
    Access = PermissibleValue(text="Access")
    Add = PermissibleValue(text="Add")
    Alert = PermissibleValue(text="Alert")
    Allocate = PermissibleValue(text="Allocate")
    Archive = PermissibleValue(text="Archive")
    Assign = PermissibleValue(text="Assign")
    Audit = PermissibleValue(text="Audit")
    Backup = PermissibleValue(text="Backup")
    Bind = PermissibleValue(text="Bind")
    Block = PermissibleValue(text="Block")
    Call = PermissibleValue(text="Call")
    Change = PermissibleValue(text="Change")
    Check = PermissibleValue(text="Check")
    Clean = PermissibleValue(text="Clean")
    Click = PermissibleValue(text="Click")
    Close = PermissibleValue(text="Close")
    Compare = PermissibleValue(text="Compare")
    Compress = PermissibleValue(text="Compress")
    Configure = PermissibleValue(text="Configure")
    Connect = PermissibleValue(text="Connect")
    Control = PermissibleValue(text="Control")
    Create = PermissibleValue(text="Create")
    Decode = PermissibleValue(text="Decode")
    Decompress = PermissibleValue(text="Decompress")
    Decrypt = PermissibleValue(text="Decrypt")
    Deny = PermissibleValue(text="Deny")
    Depress = PermissibleValue(text="Depress")
    Detect = PermissibleValue(text="Detect")
    Disconnect = PermissibleValue(text="Disconnect")
    Download = PermissibleValue(text="Download")
    Draw = PermissibleValue(text="Draw")
    Drop = PermissibleValue(text="Drop")
    Encode = PermissibleValue(text="Encode")
    Encrypt = PermissibleValue(text="Encrypt")
    Enumerate = PermissibleValue(text="Enumerate")
    Execute = PermissibleValue(text="Execute")
    Extract = PermissibleValue(text="Extract")
    Filter = PermissibleValue(text="Filter")
    Find = PermissibleValue(text="Find")
    Flush = PermissibleValue(text="Flush")
    Fork = PermissibleValue(text="Fork")
    Free = PermissibleValue(text="Free")
    Get = PermissibleValue(text="Get")
    Hide = PermissibleValue(text="Hide")
    Hook = PermissibleValue(text="Hook")
    Impersonate = PermissibleValue(text="Impersonate")
    Initialize = PermissibleValue(text="Initialize")
    Inject = PermissibleValue(text="Inject")
    Install = PermissibleValue(text="Install")
    Interleave = PermissibleValue(text="Interleave")
    Join = PermissibleValue(text="Join")
    Kill = PermissibleValue(text="Kill")
    Listen = PermissibleValue(text="Listen")
    Load = PermissibleValue(text="Load")
    Lock = PermissibleValue(text="Lock")
    Map = PermissibleValue(text="Map")
    Merge = PermissibleValue(text="Merge")
    Modify = PermissibleValue(text="Modify")
    Monitor = PermissibleValue(text="Monitor")
    Move = PermissibleValue(text="Move")
    Open = PermissibleValue(text="Open")
    Pack = PermissibleValue(text="Pack")
    Pause = PermissibleValue(text="Pause")
    Press = PermissibleValue(text="Press")
    Protect = PermissibleValue(text="Protect")
    Quarantine = PermissibleValue(text="Quarantine")
    Query = PermissibleValue(text="Query")
    Queue = PermissibleValue(text="Queue")
    Raise = PermissibleValue(text="Raise")
    Read = PermissibleValue(text="Read")
    Receive = PermissibleValue(text="Receive")
    Release = PermissibleValue(text="Release")
    Rename = PermissibleValue(text="Rename")
    Replicate = PermissibleValue(text="Replicate")
    Restore = PermissibleValue(text="Restore")
    Resume = PermissibleValue(text="Resume")
    Revert = PermissibleValue(text="Revert")
    Run = PermissibleValue(text="Run")
    Save = PermissibleValue(text="Save")
    Scan = PermissibleValue(text="Scan")
    Schedule = PermissibleValue(text="Schedule")
    Search = PermissibleValue(text="Search")
    Send = PermissibleValue(text="Send")
    Set = PermissibleValue(text="Set")
    Shutdown = PermissibleValue(text="Shutdown")
    Sleep = PermissibleValue(text="Sleep")
    Snapshot = PermissibleValue(text="Snapshot")
    Start = PermissibleValue(text="Start")
    Stop = PermissibleValue(text="Stop")
    Suspend = PermissibleValue(text="Suspend")
    Synchronize = PermissibleValue(text="Synchronize")
    Throw = PermissibleValue(text="Throw")
    Transmit = PermissibleValue(text="Transmit")
    Unblock = PermissibleValue(text="Unblock")
    Unhide = PermissibleValue(text="Unhide")
    Unhook = PermissibleValue(text="Unhook")
    Uninstall = PermissibleValue(text="Uninstall")
    Unload = PermissibleValue(text="Unload")
    Unlock = PermissibleValue(text="Unlock")
    Unmap = PermissibleValue(text="Unmap")
    Unpack = PermissibleValue(text="Unpack")
    Update = PermissibleValue(text="Update")
    Upgrade = PermissibleValue(text="Upgrade")
    Upload = PermissibleValue(text="Upload")
    Write = PermissibleValue(text="Write")

    _defn = EnumDefinition(
        name="ActionTypeVocab",
        description="Defines an open-vocabulary of common general action types.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Copy/Duplicate",
            PermissibleValue(text="Copy/Duplicate"))
        setattr(cls, "Login/Logon",
            PermissibleValue(text="Login/Logon"))
        setattr(cls, "Logout/Logoff",
            PermissibleValue(text="Logout/Logoff"))
        setattr(cls, "Remove/Delete",
            PermissibleValue(text="Remove/Delete"))
        setattr(cls, "Wipe/Destroy/Purge",
            PermissibleValue(text="Wipe/Destroy/Purge"))

class BitnessVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of word sizes that define classes of operating systems.
    """
    _defn = EnumDefinition(
        name="BitnessVocab",
        description="Defines an open-vocabulary of word sizes that define classes of operating systems.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "32",
            PermissibleValue(text="32"))
        setattr(cls, "64",
            PermissibleValue(text="64"))

class CharacterEncodingVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of character encodings.
    """
    ASCII = PermissibleValue(text="ASCII")

    _defn = EnumDefinition(
        name="CharacterEncodingVocab",
        description="Defines an open-vocabulary of character encodings.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "UTF-16",
            PermissibleValue(text="UTF-16"))
        setattr(cls, "UTF-32",
            PermissibleValue(text="UTF-32"))
        setattr(cls, "UTF-8",
            PermissibleValue(text="UTF-8"))
        setattr(cls, "Windows-1250",
            PermissibleValue(text="Windows-1250"))
        setattr(cls, "Windows-1251",
            PermissibleValue(text="Windows-1251"))
        setattr(cls, "Windows-1252",
            PermissibleValue(text="Windows-1252"))
        setattr(cls, "Windows-1253",
            PermissibleValue(text="Windows-1253"))
        setattr(cls, "Windows-1254",
            PermissibleValue(text="Windows-1254"))
        setattr(cls, "Windows-1255",
            PermissibleValue(text="Windows-1255"))
        setattr(cls, "Windows-1256",
            PermissibleValue(text="Windows-1256"))
        setattr(cls, "Windows-1257",
            PermissibleValue(text="Windows-1257"))
        setattr(cls, "Windows-1258",
            PermissibleValue(text="Windows-1258"))

class ContactAddressScopeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of scopes for address entries of digital contacts.
    """
    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")

    _defn = EnumDefinition(
        name="ContactAddressScopeVocab",
        description="Defines an open-vocabulary of scopes for address entries of digital contacts.",
    )

class ContactEmailScopeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of scopes for email entries of digital contacts.
    """
    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    cloud = PermissibleValue(text="cloud")

    _defn = EnumDefinition(
        name="ContactEmailScopeVocab",
        description="Defines an open-vocabulary of scopes for email entries of digital contacts.",
    )

class ContactPhoneScopeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of scopes for phone entries of digital contacts.
    """
    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    mobile = PermissibleValue(text="mobile")
    main = PermissibleValue(text="main")
    pager = PermissibleValue(text="pager")

    _defn = EnumDefinition(
        name="ContactPhoneScopeVocab",
        description="Defines an open-vocabulary of scopes for phone entries of digital contacts.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "home fax",
            PermissibleValue(text="home fax"))
        setattr(cls, "work fax",
            PermissibleValue(text="work fax"))

class ContactSIPScopeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of scopes for Session Initiation Protocol (SIP) entries of digital contacts.
    """
    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")

    _defn = EnumDefinition(
        name="ContactSIPScopeVocab",
        description="""Defines an open-vocabulary of scopes for Session Initiation Protocol (SIP) entries of digital contacts.""",
    )

class ContactURLScopeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of scopes for URL entries of digital contacts.
    """
    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    homepage = PermissibleValue(text="homepage")

    _defn = EnumDefinition(
        name="ContactURLScopeVocab",
        description="Defines an open-vocabulary of scopes for URL entries of digital contacts.",
    )

class DiskTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of disk types.
    """
    CDRom = PermissibleValue(text="CDRom")
    Fixed = PermissibleValue(text="Fixed")
    RAMDisk = PermissibleValue(text="RAMDisk")
    Remote = PermissibleValue(text="Remote")
    Removable = PermissibleValue(text="Removable")

    _defn = EnumDefinition(
        name="DiskTypeVocab",
        description="Defines an open-vocabulary of disk types.",
    )

class EndiannessTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of byte ordering methods.
    """
    _defn = EnumDefinition(
        name="EndiannessTypeVocab",
        description="Defines an open-vocabulary of byte ordering methods.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Big-endian",
            PermissibleValue(text="Big-endian"))
        setattr(cls, "Little-endian",
            PermissibleValue(text="Little-endian"))
        setattr(cls, "Middle-endian",
            PermissibleValue(text="Middle-endian"))

class HashNameVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of hashing algorithm names.
    """
    MD5 = PermissibleValue(text="MD5")
    MD6 = PermissibleValue(text="MD6")
    SHA1 = PermissibleValue(text="SHA1")
    SHA224 = PermissibleValue(text="SHA224")
    SHA256 = PermissibleValue(text="SHA256")
    SHA384 = PermissibleValue(text="SHA384")
    SHA512 = PermissibleValue(text="SHA512")
    SSDEEP = PermissibleValue(text="SSDEEP")

    _defn = EnumDefinition(
        name="HashNameVocab",
        description="Defines an open-vocabulary of hashing algorithm names.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "SHA3-224",
            PermissibleValue(text="SHA3-224"))
        setattr(cls, "SHA3-256",
            PermissibleValue(text="SHA3-256"))
        setattr(cls, "SHA3-384",
            PermissibleValue(text="SHA3-384"))
        setattr(cls, "SHA3-512",
            PermissibleValue(text="SHA3-512"))

class LibraryTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of library types.
    """
    Dynamic = PermissibleValue(text="Dynamic")
    Other = PermissibleValue(text="Other")
    Remote = PermissibleValue(text="Remote")
    Shared = PermissibleValue(text="Shared")
    Static = PermissibleValue(text="Static")

    _defn = EnumDefinition(
        name="LibraryTypeVocab",
        description="Defines an open-vocabulary of library types.",
    )

class MemoryBlockTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of types of memory blocks.
    """
    Initialized = PermissibleValue(text="Initialized")
    Overlay = PermissibleValue(text="Overlay")
    Uninitialized = PermissibleValue(text="Uninitialized")

    _defn = EnumDefinition(
        name="MemoryBlockTypeVocab",
        description="Defines an open-vocabulary of types of memory blocks.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bit-mapped",
            PermissibleValue(text="Bit-mapped"))
        setattr(cls, "Byte-mapped",
            PermissibleValue(text="Byte-mapped"))

class ObservableObjectRelationshipVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of inter-observable object relationships.
    """
    Allocated = PermissibleValue(text="Allocated")
    Allocated_By = PermissibleValue(text="Allocated_By")
    Attachment_Of = PermissibleValue(text="Attachment_Of")
    Bound = PermissibleValue(text="Bound")
    Bound_By = PermissibleValue(text="Bound_By")
    Characterized_By = PermissibleValue(text="Characterized_By")
    Characterizes = PermissibleValue(text="Characterizes")
    Child_Of = PermissibleValue(text="Child_Of")
    Closed = PermissibleValue(text="Closed")
    Closed_By = PermissibleValue(text="Closed_By")
    Compressed = PermissibleValue(text="Compressed")
    Compressed_By = PermissibleValue(text="Compressed_By")
    Compressed_From = PermissibleValue(text="Compressed_From")
    Compressed_Into = PermissibleValue(text="Compressed_Into")
    Connected_From = PermissibleValue(text="Connected_From")
    Connected_To = PermissibleValue(text="Connected_To")
    Contained_Within = PermissibleValue(text="Contained_Within")
    Contains = PermissibleValue(text="Contains")
    Copied = PermissibleValue(text="Copied")
    Copied_By = PermissibleValue(text="Copied_By")
    Copied_From = PermissibleValue(text="Copied_From")
    Copied_To = PermissibleValue(text="Copied_To")
    Created = PermissibleValue(text="Created")
    Created_By = PermissibleValue(text="Created_By")
    Decoded = PermissibleValue(text="Decoded")
    Decoded_By = PermissibleValue(text="Decoded_By")
    Decompressed = PermissibleValue(text="Decompressed")
    Decompressed_By = PermissibleValue(text="Decompressed_By")
    Decrypted = PermissibleValue(text="Decrypted")
    Decrypted_By = PermissibleValue(text="Decrypted_By")
    Deleted = PermissibleValue(text="Deleted")
    Deleted_By = PermissibleValue(text="Deleted_By")
    Deleted_From = PermissibleValue(text="Deleted_From")
    Downloaded = PermissibleValue(text="Downloaded")
    Downloaded_By = PermissibleValue(text="Downloaded_By")
    Downloaded_From = PermissibleValue(text="Downloaded_From")
    Downloaded_To = PermissibleValue(text="Downloaded_To")
    Dropped = PermissibleValue(text="Dropped")
    Dropped_By = PermissibleValue(text="Dropped_By")
    Encoded = PermissibleValue(text="Encoded")
    Encoded_By = PermissibleValue(text="Encoded_By")
    Encrypted = PermissibleValue(text="Encrypted")
    Encrypted_By = PermissibleValue(text="Encrypted_By")
    Encrypted_From = PermissibleValue(text="Encrypted_From")
    Encrypted_To = PermissibleValue(text="Encrypted_To")
    Extracted_From = PermissibleValue(text="Extracted_From")
    FQDN_Of = PermissibleValue(text="FQDN_Of")
    Freed = PermissibleValue(text="Freed")
    Freed_By = PermissibleValue(text="Freed_By")
    Had_Attachment = PermissibleValue(text="Had_Attachment")
    Hooked = PermissibleValue(text="Hooked")
    Hooked_By = PermissibleValue(text="Hooked_By")
    Initialized_By = PermissibleValue(text="Initialized_By")
    Initialized_To = PermissibleValue(text="Initialized_To")
    Injected = PermissibleValue(text="Injected")
    Injected_As = PermissibleValue(text="Injected_As")
    Injected_By = PermissibleValue(text="Injected_By")
    Injected_Into = PermissibleValue(text="Injected_Into")
    Installed = PermissibleValue(text="Installed")
    Installed_By = PermissibleValue(text="Installed_By")
    Joined = PermissibleValue(text="Joined")
    Joined_By = PermissibleValue(text="Joined_By")
    Killed = PermissibleValue(text="Killed")
    Killed_By = PermissibleValue(text="Killed_By")
    Listened_On = PermissibleValue(text="Listened_On")
    Listened_On_By = PermissibleValue(text="Listened_On_By")
    Loaded_From = PermissibleValue(text="Loaded_From")
    Loaded_Into = PermissibleValue(text="Loaded_Into")
    Locked = PermissibleValue(text="Locked")
    Locked_By = PermissibleValue(text="Locked_By")
    Mapped_By = PermissibleValue(text="Mapped_By")
    Mapped_Into = PermissibleValue(text="Mapped_Into")
    Merged = PermissibleValue(text="Merged")
    Merged_By = PermissibleValue(text="Merged_By")
    Modified_Properties_Of = PermissibleValue(text="Modified_Properties_Of")
    Monitored = PermissibleValue(text="Monitored")
    Monitored_By = PermissibleValue(text="Monitored_By")
    Moved = PermissibleValue(text="Moved")
    Moved_By = PermissibleValue(text="Moved_By")
    Moved_From = PermissibleValue(text="Moved_From")
    Moved_To = PermissibleValue(text="Moved_To")
    Opened = PermissibleValue(text="Opened")
    Opened_By = PermissibleValue(text="Opened_By")
    Packed = PermissibleValue(text="Packed")
    Packed_By = PermissibleValue(text="Packed_By")
    Packed_From = PermissibleValue(text="Packed_From")
    Packed_Into = PermissibleValue(text="Packed_Into")
    Parent_Of = PermissibleValue(text="Parent_Of")
    Paused = PermissibleValue(text="Paused")
    Paused_By = PermissibleValue(text="Paused_By")
    Previously_Contained = PermissibleValue(text="Previously_Contained")
    Properties_Modified_By = PermissibleValue(text="Properties_Modified_By")
    Properties_Queried = PermissibleValue(text="Properties_Queried")
    Properties_Queried_By = PermissibleValue(text="Properties_Queried_By")
    Read_From = PermissibleValue(text="Read_From")
    Read_From_By = PermissibleValue(text="Read_From_By")
    Received = PermissibleValue(text="Received")
    Received_By = PermissibleValue(text="Received_By")
    Received_From = PermissibleValue(text="Received_From")
    Received_Via_Upload = PermissibleValue(text="Received_Via_Upload")
    Redirects_To = PermissibleValue(text="Redirects_To")
    Related_To = PermissibleValue(text="Related_To")
    Renamed = PermissibleValue(text="Renamed")
    Renamed_By = PermissibleValue(text="Renamed_By")
    Renamed_From = PermissibleValue(text="Renamed_From")
    Renamed_To = PermissibleValue(text="Renamed_To")
    Resolved_To = PermissibleValue(text="Resolved_To")
    Resumed = PermissibleValue(text="Resumed")
    Resumed_By = PermissibleValue(text="Resumed_By")
    Root_Domain_Of = PermissibleValue(text="Root_Domain_Of")
    Searched_For = PermissibleValue(text="Searched_For")
    Searched_For_By = PermissibleValue(text="Searched_For_By")
    Sent = PermissibleValue(text="Sent")
    Sent_By = PermissibleValue(text="Sent_By")
    Sent_To = PermissibleValue(text="Sent_To")
    Sent_Via_Upload = PermissibleValue(text="Sent_Via_Upload")
    Set_From = PermissibleValue(text="Set_From")
    Set_To = PermissibleValue(text="Set_To")
    Signed_By = PermissibleValue(text="Signed_By")
    Suspended = PermissibleValue(text="Suspended")
    Suspended_By = PermissibleValue(text="Suspended_By")
    Unhooked = PermissibleValue(text="Unhooked")
    Unhooked_By = PermissibleValue(text="Unhooked_By")
    Unlocked = PermissibleValue(text="Unlocked")
    Unlocked_By = PermissibleValue(text="Unlocked_By")
    Unpacked = PermissibleValue(text="Unpacked")
    Unpacked_By = PermissibleValue(text="Unpacked_By")
    Uploaded = PermissibleValue(text="Uploaded")
    Uploaded_By = PermissibleValue(text="Uploaded_By")
    Uploaded_From = PermissibleValue(text="Uploaded_From")
    Uploaded_To = PermissibleValue(text="Uploaded_To")
    Used = PermissibleValue(text="Used")
    Used_By = PermissibleValue(text="Used_By")
    Values_Enumerated = PermissibleValue(text="Values_Enumerated")
    Values_Enumerated_By = PermissibleValue(text="Values_Enumerated_By")
    Written_To_By = PermissibleValue(text="Written_To_By")
    Wrote_To = PermissibleValue(text="Wrote_To")

    _defn = EnumDefinition(
        name="ObservableObjectRelationshipVocab",
        description="Defines an open-vocabulary of inter-observable object relationships.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Sub-domain_Of",
            PermissibleValue(text="Sub-domain_Of"))
        setattr(cls, "Supra-domain_Of",
            PermissibleValue(text="Supra-domain_Of"))

class ObservableObjectStateVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of observable object states.
    """
    Active = PermissibleValue(text="Active")
    Closed = PermissibleValue(text="Closed")
    Exists = PermissibleValue(text="Exists")
    Inactive = PermissibleValue(text="Inactive")
    Locked = PermissibleValue(text="Locked")
    Open = PermissibleValue(text="Open")
    Started = PermissibleValue(text="Started")
    Stopped = PermissibleValue(text="Stopped")
    Unlocked = PermissibleValue(text="Unlocked")

    _defn = EnumDefinition(
        name="ObservableObjectStateVocab",
        description="Defines an open-vocabulary of observable object states.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Does Not Exist",
            PermissibleValue(text="Does Not Exist"))

class PartitionTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of partition types. See http://www.win.tue.nl/~aeb/partitions/partition_types-1.html
    for more information about the various partition types.
    """
    PARTITION_ENTRY_UNUSED = PermissibleValue(text="PARTITION_ENTRY_UNUSED")
    PARTITION_EXTENDED = PermissibleValue(text="PARTITION_EXTENDED")
    PARTITION_FAT32 = PermissibleValue(text="PARTITION_FAT32")
    PARTITION_FAT32_XINT13 = PermissibleValue(text="PARTITION_FAT32_XINT13")
    PARTITION_FAT_12 = PermissibleValue(text="PARTITION_FAT_12")
    PARTITION_FAT_16 = PermissibleValue(text="PARTITION_FAT_16")
    PARTITION_HUGE = PermissibleValue(text="PARTITION_HUGE")
    PARTITION_IFS = PermissibleValue(text="PARTITION_IFS")
    PARTITION_LDM = PermissibleValue(text="PARTITION_LDM")
    PARTITION_NTFT = PermissibleValue(text="PARTITION_NTFT")
    PARTITION_OS2BOOTMGR = PermissibleValue(text="PARTITION_OS2BOOTMGR")
    PARTITION_PREP = PermissibleValue(text="PARTITION_PREP")
    PARTITION_UNIX = PermissibleValue(text="PARTITION_UNIX")
    PARTITION_XENIX_1 = PermissibleValue(text="PARTITION_XENIX_1")
    PARTITION_XENIX_2 = PermissibleValue(text="PARTITION_XENIX_2")
    PARTITION_XINT13 = PermissibleValue(text="PARTITION_XINT13")
    PARTITION_XINT13_EXTENDED = PermissibleValue(text="PARTITION_XINT13_EXTENDED")
    UNKNOWN = PermissibleValue(text="UNKNOWN")
    VALID_NTFT = PermissibleValue(text="VALID_NTFT")

    _defn = EnumDefinition(
        name="PartitionTypeVocab",
        description="""Defines an open-vocabulary of partition types. See http://www.win.tue.nl/~aeb/partitions/partition_types-1.html for more information about the various partition types.""",
    )

class ProcessorArchVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of computer processor architectures.
    """
    ARM = PermissibleValue(text="ARM")
    Alpha = PermissibleValue(text="Alpha")
    MIPS = PermissibleValue(text="MIPS")
    Other = PermissibleValue(text="Other")
    PowerPC = PermissibleValue(text="PowerPC")
    SPARC = PermissibleValue(text="SPARC")

    _defn = EnumDefinition(
        name="ProcessorArchVocab",
        description="Defines an open-vocabulary of computer processor architectures.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "IA-64",
            PermissibleValue(text="IA-64"))
        setattr(cls, "Motorola 68k",
            PermissibleValue(text="Motorola 68k"))
        setattr(cls, "eSi-RISC",
            PermissibleValue(text="eSi-RISC"))
        setattr(cls, "x86-32",
            PermissibleValue(text="x86-32"))
        setattr(cls, "x86-64",
            PermissibleValue(text="x86-64"))
        setattr(cls, "z/Architecture",
            PermissibleValue(text="z/Architecture"))

class RecoveredObjectStatusVocab(EnumDefinitionImpl):
    """
    Defines the vocabulary for Recovered Object status of data.
    """
    recovered = PermissibleValue(text="recovered")
    overwritten = PermissibleValue(text="overwritten")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="RecoveredObjectStatusVocab",
        description="Defines the vocabulary for Recovered Object status of data.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "partially recovered",
            PermissibleValue(text="partially recovered"))

class RegionalRegistryTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of Regional Internet Registries (RIRs) names, represented via their respective acronyms.
    """
    APNIC = PermissibleValue(text="APNIC")
    ARIN = PermissibleValue(text="ARIN")
    AfriNIC = PermissibleValue(text="AfriNIC")
    LACNIC = PermissibleValue(text="LACNIC")

    _defn = EnumDefinition(
        name="RegionalRegistryTypeVocab",
        description="""Defines an open-vocabulary of Regional Internet Registries (RIRs) names, represented via their respective acronyms.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "RIPE NCC",
            PermissibleValue(text="RIPE NCC"))

class RegistryDatatypeVocab(EnumDefinitionImpl):
    """
    UCO 1.5.0 declares the vocabulary uco-vocabulary:RegistryDatatypeVocab without a definition.
    """
    reg_binary = PermissibleValue(text="reg_binary")
    reg_dword = PermissibleValue(text="reg_dword")
    reg_dword_big_endian = PermissibleValue(text="reg_dword_big_endian")
    reg_expand_sz = PermissibleValue(text="reg_expand_sz")
    reg_full_resource_descriptor = PermissibleValue(text="reg_full_resource_descriptor")
    reg_invalid_type = PermissibleValue(text="reg_invalid_type")
    reg_link = PermissibleValue(text="reg_link")
    reg_multi_sz = PermissibleValue(text="reg_multi_sz")
    reg_none = PermissibleValue(text="reg_none")
    reg_qword = PermissibleValue(text="reg_qword")
    reg_resource_list = PermissibleValue(text="reg_resource_list")
    reg_resource_requirements_list = PermissibleValue(text="reg_resource_requirements_list")
    reg_sz = PermissibleValue(text="reg_sz")

    _defn = EnumDefinition(
        name="RegistryDatatypeVocab",
        description="UCO 1.5.0 declares the vocabulary uco-vocabulary:RegistryDatatypeVocab without a definition.",
    )

class SIMFormVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of common SIM card form factors.
    """
    _defn = EnumDefinition(
        name="SIMFormVocab",
        description="Defines an open-vocabulary of common SIM card form factors.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Full-size SIM",
            PermissibleValue(text="Full-size SIM"))
        setattr(cls, "Micro SIM",
            PermissibleValue(text="Micro SIM"))
        setattr(cls, "Nano SIM",
            PermissibleValue(text="Nano SIM"))

class SIMTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of common SIM card types.
    """
    SIM = PermissibleValue(text="SIM")
    UICC = PermissibleValue(text="UICC")
    USIM = PermissibleValue(text="USIM")

    _defn = EnumDefinition(
        name="SIMTypeVocab",
        description="Defines an open-vocabulary of common SIM card types.",
    )

class TaskActionTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of task action types. See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa380596(v=vs.85).aspx.
    """
    TASK_ACTION_COM_HANDLER = PermissibleValue(text="TASK_ACTION_COM_HANDLER")
    TASK_ACTION_EXEC = PermissibleValue(text="TASK_ACTION_EXEC")
    TASK_ACTION_SEND_EMAIL = PermissibleValue(text="TASK_ACTION_SEND_EMAIL")
    TASK_ACTION_SHOW_MESSAGE = PermissibleValue(text="TASK_ACTION_SHOW_MESSAGE")

    _defn = EnumDefinition(
        name="TaskActionTypeVocab",
        description="""Defines an open-vocabulary of task action types. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa380596(v=vs.85).aspx.""",
    )

class TaskFlagVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of the run flags for a task scheduler task. See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381283(v=vs.85).aspx See Also:
    http://msdn.microsoft.com/en-us/library/microsoft.office.excel.server.addins.computecluster.taskscheduler.taskflags(v=office.12).aspx.
    """
    TASK_FLAG_DELETE_WHEN_DONE = PermissibleValue(text="TASK_FLAG_DELETE_WHEN_DONE")
    TASK_FLAG_DISABLED = PermissibleValue(text="TASK_FLAG_DISABLED")
    TASK_FLAG_DONT_START_IF_ON_BATTERIES = PermissibleValue(text="TASK_FLAG_DONT_START_IF_ON_BATTERIES")
    TASK_FLAG_HIDDEN = PermissibleValue(text="TASK_FLAG_HIDDEN")
    TASK_FLAG_INTERACTIVE = PermissibleValue(text="TASK_FLAG_INTERACTIVE")
    TASK_FLAG_KILL_IF_GOING_ON_BATTERIES = PermissibleValue(text="TASK_FLAG_KILL_IF_GOING_ON_BATTERIES")
    TASK_FLAG_KILL_ON_IDLE_END = PermissibleValue(text="TASK_FLAG_KILL_ON_IDLE_END")
    TASK_FLAG_RESTART_ON_IDLE_RESUME = PermissibleValue(text="TASK_FLAG_RESTART_ON_IDLE_RESUME")
    TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET = PermissibleValue(text="TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET")
    TASK_FLAG_RUN_ONLY_IF_LOGGED_ON = PermissibleValue(text="TASK_FLAG_RUN_ONLY_IF_LOGGED_ON")
    TASK_FLAG_START_ONLY_IF_IDLE = PermissibleValue(text="TASK_FLAG_START_ONLY_IF_IDLE")
    TASK_FLAG_SYSTEM_REQUIRED = PermissibleValue(text="TASK_FLAG_SYSTEM_REQUIRED")
    TASK_FLAG_ZERO = PermissibleValue(text="TASK_FLAG_ZERO")

    _defn = EnumDefinition(
        name="TaskFlagVocab",
        description="""Defines an open-vocabulary of the run flags for a task scheduler task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381283(v=vs.85).aspx See Also: http://msdn.microsoft.com/en-us/library/microsoft.office.excel.server.addins.computecluster.taskscheduler.taskflags(v=office.12).aspx.""",
    )

class TaskPriorityVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of the priority levels of task scheduler tasks. See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa383512(v=vs.85).aspx.
    """
    ABOVE_NORMAL_PRIORITY_CLASS = PermissibleValue(text="ABOVE_NORMAL_PRIORITY_CLASS")
    BELOW_NORMAL_PRIORITY_CLASS = PermissibleValue(text="BELOW_NORMAL_PRIORITY_CLASS")
    HIGH_PRIORITY_CLASS = PermissibleValue(text="HIGH_PRIORITY_CLASS")
    IDLE_PRIORITY_CLASS = PermissibleValue(text="IDLE_PRIORITY_CLASS")
    NORMAL_PRIORITY_CLASS = PermissibleValue(text="NORMAL_PRIORITY_CLASS")
    REALTIME_PRIORITY_CLASS = PermissibleValue(text="REALTIME_PRIORITY_CLASS")

    _defn = EnumDefinition(
        name="TaskPriorityVocab",
        description="""Defines an open-vocabulary of the priority levels of task scheduler tasks. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa383512(v=vs.85).aspx.""",
    )

class TaskStatusVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of the possible statuses of a scheduled task. See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa383604(v=vs.85).aspx See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381263(v=vs.85).aspx See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381833(v=vs.85).aspx See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa383617(v=vs.85).aspx.
    """
    SCHED_E_ACCOUNT_DBASE_CORRUPT = PermissibleValue(text="SCHED_E_ACCOUNT_DBASE_CORRUPT")
    SCHED_E_ACCOUNT_INFORMATION_NOT_SET = PermissibleValue(text="SCHED_E_ACCOUNT_INFORMATION_NOT_SET")
    SCHED_E_ACCOUNT_NAME_NOT_FOUND = PermissibleValue(text="SCHED_E_ACCOUNT_NAME_NOT_FOUND")
    SCHED_E_CANNOT_OPEN_TASK = PermissibleValue(text="SCHED_E_CANNOT_OPEN_TASK")
    SCHED_E_INVALID_TASK = PermissibleValue(text="SCHED_E_INVALID_TASK")
    SCHED_E_NO_SECURITY_SERVICES = PermissibleValue(text="SCHED_E_NO_SECURITY_SERVICES")
    SCHED_E_SERVICE_NOT_INSTALLED = PermissibleValue(text="SCHED_E_SERVICE_NOT_INSTALLED")
    SCHED_E_SERVICE_NOT_RUNNING = PermissibleValue(text="SCHED_E_SERVICE_NOT_RUNNING")
    SCHED_E_TASK_NOT_READY = PermissibleValue(text="SCHED_E_TASK_NOT_READY")
    SCHED_E_TASK_NOT_RUNNING = PermissibleValue(text="SCHED_E_TASK_NOT_RUNNING")
    SCHED_E_TRIGGER_NOT_FOUND = PermissibleValue(text="SCHED_E_TRIGGER_NOT_FOUND")
    SCHED_E_UNKNOWN_OBJECT_VERSION = PermissibleValue(text="SCHED_E_UNKNOWN_OBJECT_VERSION")
    SCHED_E_UNSUPPORTED_ACCOUNT_OPTION = PermissibleValue(text="SCHED_E_UNSUPPORTED_ACCOUNT_OPTION")
    SCHED_S_EVENT_TRIGGER = PermissibleValue(text="SCHED_S_EVENT_TRIGGER")
    SCHED_S_TASK_DISABLED = PermissibleValue(text="SCHED_S_TASK_DISABLED")
    SCHED_S_TASK_HAS_NOT_RUN = PermissibleValue(text="SCHED_S_TASK_HAS_NOT_RUN")
    SCHED_S_TASK_NOT_SCHEDULED = PermissibleValue(text="SCHED_S_TASK_NOT_SCHEDULED")
    SCHED_S_TASK_NO_MORE_RUNS = PermissibleValue(text="SCHED_S_TASK_NO_MORE_RUNS")
    SCHED_S_TASK_NO_VALID_TRIGGERS = PermissibleValue(text="SCHED_S_TASK_NO_VALID_TRIGGERS")
    SCHED_S_TASK_READY = PermissibleValue(text="SCHED_S_TASK_READY")
    SCHED_S_TASK_RUNNING = PermissibleValue(text="SCHED_S_TASK_RUNNING")
    SCHED_S_TASK_TERMINATED = PermissibleValue(text="SCHED_S_TASK_TERMINATED")
    TASK_STATE_QUEUED = PermissibleValue(text="TASK_STATE_QUEUED")
    TASK_STATE_UNKNOWN = PermissibleValue(text="TASK_STATE_UNKNOWN")

    _defn = EnumDefinition(
        name="TaskStatusVocab",
        description="""Defines an open-vocabulary of the possible statuses of a scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa383604(v=vs.85).aspx See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381263(v=vs.85).aspx See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381833(v=vs.85).aspx See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa383617(v=vs.85).aspx.""",
    )

class ThreadRunningStatusVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of the various states that a thread may be in before, during, or after execution. See
    http://msdn.microsoft.com/en-us/library/system.diagnostics.threadstate(v=vs.110).aspx.
    """
    Initialized = PermissibleValue(text="Initialized")
    Ready = PermissibleValue(text="Ready")
    Running = PermissibleValue(text="Running")
    Standby = PermissibleValue(text="Standby")
    Terminated = PermissibleValue(text="Terminated")
    Transition = PermissibleValue(text="Transition")
    Unknown = PermissibleValue(text="Unknown")
    Waiting = PermissibleValue(text="Waiting")

    _defn = EnumDefinition(
        name="ThreadRunningStatusVocab",
        description="""Defines an open-vocabulary of the various states that a thread may be in before, during, or after execution. See http://msdn.microsoft.com/en-us/library/system.diagnostics.threadstate(v=vs.110).aspx.""",
    )

class TimestampPrecisionVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of timestamp precision granularities.
    """
    day = PermissibleValue(text="day")
    hour = PermissibleValue(text="hour")
    minute = PermissibleValue(text="minute")
    month = PermissibleValue(text="month")
    second = PermissibleValue(text="second")
    year = PermissibleValue(text="year")

    _defn = EnumDefinition(
        name="TimestampPrecisionVocab",
        description="Defines an open-vocabulary of timestamp precision granularities.",
    )

class TrendVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of trend values.
    """
    Decreasing = PermissibleValue(text="Decreasing")
    Increasing = PermissibleValue(text="Increasing")

    _defn = EnumDefinition(
        name="TrendVocab",
        description="Defines an open-vocabulary of trend values.",
    )

class TriggerFrequencyVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of the frequency types that a trigger may use. See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa383620(v=vs.85).aspx and
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa383987(v=vs.85).aspx.
    """
    TASK_EVENT_TRIGGER_AT_LOGON = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_LOGON")
    TASK_EVENT_TRIGGER_AT_SYSTEMSTART = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_SYSTEMSTART")
    TASK_EVENT_TRIGGER_ON_IDLE = PermissibleValue(text="TASK_EVENT_TRIGGER_ON_IDLE")
    TASK_TIME_TRIGGER_DAILY = PermissibleValue(text="TASK_TIME_TRIGGER_DAILY")
    TASK_TIME_TRIGGER_MONTHLYDATE = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDATE")
    TASK_TIME_TRIGGER_MONTHLYDOW = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDOW")
    TASK_TIME_TRIGGER_ONCE = PermissibleValue(text="TASK_TIME_TRIGGER_ONCE")
    TASK_TIME_TRIGGER_WEEKLY = PermissibleValue(text="TASK_TIME_TRIGGER_WEEKLY")

    _defn = EnumDefinition(
        name="TriggerFrequencyVocab",
        description="""Defines an open-vocabulary of the frequency types that a trigger may use. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa383620(v=vs.85).aspx and http://msdn.microsoft.com/en-us/library/windows/desktop/aa383987(v=vs.85).aspx.""",
    )

class TriggerTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of the types of triggers associated with a task.
    """
    TASK_TRIGGER_BOOT = PermissibleValue(text="TASK_TRIGGER_BOOT")
    TASK_TRIGGER_EVENT = PermissibleValue(text="TASK_TRIGGER_EVENT")
    TASK_TRIGGER_IDLE = PermissibleValue(text="TASK_TRIGGER_IDLE")
    TASK_TRIGGER_LOGON = PermissibleValue(text="TASK_TRIGGER_LOGON")
    TASK_TRIGGER_REGISTRATION = PermissibleValue(text="TASK_TRIGGER_REGISTRATION")
    TASK_TRIGGER_SESSION_STATE_CHANGE = PermissibleValue(text="TASK_TRIGGER_SESSION_STATE_CHANGE")
    TASK_TRIGGER_TIME = PermissibleValue(text="TASK_TRIGGER_TIME")

    _defn = EnumDefinition(
        name="TriggerTypeVocab",
        description="Defines an open-vocabulary of the types of triggers associated with a task.",
    )

class URLTransitionTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of types of URL transitions.
    """
    link = PermissibleValue(text="link")
    typed = PermissibleValue(text="typed")
    auto_bookmark = PermissibleValue(text="auto_bookmark")
    auto_subframe = PermissibleValue(text="auto_subframe")
    manual_subframe = PermissibleValue(text="manual_subframe")
    generated = PermissibleValue(text="generated")
    auto_toplevel = PermissibleValue(text="auto_toplevel")
    form_submit = PermissibleValue(text="form_submit")
    reload = PermissibleValue(text="reload")
    keyword = PermissibleValue(text="keyword")
    keyword_generated = PermissibleValue(text="keyword_generated")

    _defn = EnumDefinition(
        name="URLTransitionTypeVocab",
        description="Defines an open-vocabulary of types of URL transitions.",
    )

class UnixProcessStateVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of Unix process states
    """
    Dead = PermissibleValue(text="Dead")
    InterruptibleSleep = PermissibleValue(text="InterruptibleSleep")
    Paging = PermissibleValue(text="Paging")
    Running = PermissibleValue(text="Running")
    Stopped = PermissibleValue(text="Stopped")
    UninterruptibleSleep = PermissibleValue(text="UninterruptibleSleep")
    Zombie = PermissibleValue(text="Zombie")

    _defn = EnumDefinition(
        name="UnixProcessStateVocab",
        description="Defines an open-vocabulary of Unix process states",
    )

class WhoisContactTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of types of registrar contacts listed in a whois entry.
    """
    ADMIN = PermissibleValue(text="ADMIN")
    BILLING = PermissibleValue(text="BILLING")
    TECHNICAL = PermissibleValue(text="TECHNICAL")

    _defn = EnumDefinition(
        name="WhoisContactTypeVocab",
        description="Defines an open-vocabulary of types of registrar contacts listed in a whois entry.",
    )

class WhoisDNSSECTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of acceptable values for the DNSSEC field in a Whois entry.
    """
    Signed = PermissibleValue(text="Signed")
    Unsigned = PermissibleValue(text="Unsigned")

    _defn = EnumDefinition(
        name="WhoisDNSSECTypeVocab",
        description="Defines an open-vocabulary of acceptable values for the DNSSEC field in a Whois entry.",
    )

class WhoisStatusTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of all valid statuses for a domain within a whois entry.
    """
    ADD_PERIOD = PermissibleValue(text="ADD_PERIOD")
    AUTO_RENEW_PERIOD = PermissibleValue(text="AUTO_RENEW_PERIOD")
    CLIENT_DELETE_PROHIBITED = PermissibleValue(text="CLIENT_DELETE_PROHIBITED")
    CLIENT_HOLD = PermissibleValue(text="CLIENT_HOLD")
    CLIENT_RENEW_PROHIBITED = PermissibleValue(text="CLIENT_RENEW_PROHIBITED")
    CLIENT_TRANSFER_PROHIBITED = PermissibleValue(text="CLIENT_TRANSFER_PROHIBITED")
    CLIENT_UPDATE_PROHIBITED = PermissibleValue(text="CLIENT_UPDATE_PROHIBITED")
    DELETE_PROHIBITED = PermissibleValue(text="DELETE_PROHIBITED")
    HOLD = PermissibleValue(text="HOLD")
    INACTIVE = PermissibleValue(text="INACTIVE")
    OK = PermissibleValue(text="OK")
    PENDING_DELETE_RESTORABLE = PermissibleValue(text="PENDING_DELETE_RESTORABLE")
    PENDING_DELETE_SCHEDULED_FOR_RELEASE = PermissibleValue(text="PENDING_DELETE_SCHEDULED_FOR_RELEASE")
    PENDING_RESTORE = PermissibleValue(text="PENDING_RESTORE")
    RENEW_PERIOD = PermissibleValue(text="RENEW_PERIOD")
    RENEW_PROHIBITED = PermissibleValue(text="RENEW_PROHIBITED")
    TRANSFER_PERIOD = PermissibleValue(text="TRANSFER_PERIOD")
    TRANSFER_PROHIBITED = PermissibleValue(text="TRANSFER_PROHIBITED")
    UPDATE_PROHIBITED = PermissibleValue(text="UPDATE_PROHIBITED")

    _defn = EnumDefinition(
        name="WhoisStatusTypeVocab",
        description="Defines an open-vocabulary of all valid statuses for a domain within a whois entry.",
    )

class WindowsDriveTypeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of possible drive types, as enumerated by the WINAPI GetDriveType function:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa364939(v=vs.85).aspx.
    """
    DRIVE_CDROM = PermissibleValue(text="DRIVE_CDROM")
    DRIVE_FIXED = PermissibleValue(text="DRIVE_FIXED")
    DRIVE_NO_ROOT_DIR = PermissibleValue(text="DRIVE_NO_ROOT_DIR")
    DRIVE_RAMDISK = PermissibleValue(text="DRIVE_RAMDISK")
    DRIVE_REMOTE = PermissibleValue(text="DRIVE_REMOTE")
    DRIVE_REMOVABLE = PermissibleValue(text="DRIVE_REMOVABLE")
    DRIVE_UNKNOWN = PermissibleValue(text="DRIVE_UNKNOWN")

    _defn = EnumDefinition(
        name="WindowsDriveTypeVocab",
        description="""Defines an open-vocabulary of possible drive types, as enumerated by the WINAPI GetDriveType function: http://msdn.microsoft.com/en-us/library/windows/desktop/aa364939(v=vs.85).aspx.""",
    )

class WindowsVolumeAttributeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of attributes that may be returned by the diskpart attributes command:
    http://technet.microsoft.com/en-us/library/cc766465(v=ws.10).aspx.
    """
    Hidden = PermissibleValue(text="Hidden")
    NoDefaultDriveLetter = PermissibleValue(text="NoDefaultDriveLetter")
    ReadOnly = PermissibleValue(text="ReadOnly")
    ShadowCopy = PermissibleValue(text="ShadowCopy")

    _defn = EnumDefinition(
        name="WindowsVolumeAttributeVocab",
        description="""Defines an open-vocabulary of attributes that may be returned by the diskpart attributes command: http://technet.microsoft.com/en-us/library/cc766465(v=ws.10).aspx.""",
    )

class WirelessNetworkSecurityModeVocab(EnumDefinitionImpl):
    """
    Defines an open-vocabulary of security modes that may be configured for wireless network connections.
    """
    WEP = PermissibleValue(text="WEP")
    WPA = PermissibleValue(text="WPA")

    _defn = EnumDefinition(
        name="WirelessNetworkSecurityModeVocab",
        description="""Defines an open-vocabulary of security modes that may be configured for wireless network connections.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(text="None"))
        setattr(cls, "WPA2-PSK",
            PermissibleValue(text="WPA2-PSK"))
        setattr(cls, "WPA2-Enterprise",
            PermissibleValue(text="WPA2-Enterprise"))
        setattr(cls, "WPA3-PSK",
            PermissibleValue(text="WPA3-PSK"))
        setattr(cls, "WPA3-Enterprise",
            PermissibleValue(text="WPA3-Enterprise"))

class NetworkSocketAddressFamily(EnumDefinitionImpl):
    """
    UCO 1.5.0 declares the vocabulary uco-observable:NetworkSocketAddressFamily without a definition.
    """
    af_appletalk = PermissibleValue(text="af_appletalk")
    af_bth = PermissibleValue(text="af_bth")
    af_inet = PermissibleValue(text="af_inet")
    af_inet6 = PermissibleValue(text="af_inet6")
    af_ipx = PermissibleValue(text="af_ipx")
    af_irda = PermissibleValue(text="af_irda")
    af_netbios = PermissibleValue(text="af_netbios")
    af_unspec = PermissibleValue(text="af_unspec")

    _defn = EnumDefinition(
        name="NetworkSocketAddressFamily",
        description="UCO 1.5.0 declares the vocabulary uco-observable:NetworkSocketAddressFamily without a definition.",
    )

class NetworkSocketProtocolFamily(EnumDefinitionImpl):
    """
    UCO 1.5.0 declares the vocabulary uco-observable:NetworkSocketProtocolFamily without a definition.
    """
    pf_appletalk = PermissibleValue(text="pf_appletalk")
    pf_ash = PermissibleValue(text="pf_ash")
    pf_atmpvc = PermissibleValue(text="pf_atmpvc")
    pf_atmsvc = PermissibleValue(text="pf_atmsvc")
    pf_ax25 = PermissibleValue(text="pf_ax25")
    pf_bluetooth = PermissibleValue(text="pf_bluetooth")
    pf_bridge = PermissibleValue(text="pf_bridge")
    pf_decnet = PermissibleValue(text="pf_decnet")
    pf_econet = PermissibleValue(text="pf_econet")
    pf_inet = PermissibleValue(text="pf_inet")
    pf_inet6 = PermissibleValue(text="pf_inet6")
    pf_ipx = PermissibleValue(text="pf_ipx")
    pf_irda = PermissibleValue(text="pf_irda")
    pf_key = PermissibleValue(text="pf_key")
    pf_netbeui = PermissibleValue(text="pf_netbeui")
    pf_netlink = PermissibleValue(text="pf_netlink")
    pf_netrom = PermissibleValue(text="pf_netrom")
    pf_packet = PermissibleValue(text="pf_packet")
    pf_pppox = PermissibleValue(text="pf_pppox")
    pf_rose = PermissibleValue(text="pf_rose")
    pf_route = PermissibleValue(text="pf_route")
    pf_security = PermissibleValue(text="pf_security")
    pf_sna = PermissibleValue(text="pf_sna")
    pf_wanpipe = PermissibleValue(text="pf_wanpipe")
    pf_x25 = PermissibleValue(text="pf_x25")

    _defn = EnumDefinition(
        name="NetworkSocketProtocolFamily",
        description="UCO 1.5.0 declares the vocabulary uco-observable:NetworkSocketProtocolFamily without a definition.",
    )

class NetworkSocketType(EnumDefinitionImpl):
    """
    UCO 1.5.0 declares the vocabulary uco-observable:NetworkSocketType without a definition.
    """
    sock_dgram = PermissibleValue(text="sock_dgram")
    sock_raw = PermissibleValue(text="sock_raw")
    sock_rdm = PermissibleValue(text="sock_rdm")
    sock_seqpacket = PermissibleValue(text="sock_seqpacket")
    sock_stream = PermissibleValue(text="sock_stream")

    _defn = EnumDefinition(
        name="NetworkSocketType",
        description="UCO 1.5.0 declares the vocabulary uco-observable:NetworkSocketType without a definition.",
    )

class RegistryDatatype(EnumDefinitionImpl):
    """
    UCO 1.5.0 declares the vocabulary uco-observable:RegistryDatatype without a definition.
    """
    reg_binary = PermissibleValue(text="reg_binary")
    reg_dword = PermissibleValue(text="reg_dword")
    reg_dword_big_endian = PermissibleValue(text="reg_dword_big_endian")
    reg_expand_sz = PermissibleValue(text="reg_expand_sz")
    reg_full_resource_descriptor = PermissibleValue(text="reg_full_resource_descriptor")
    reg_invalid_type = PermissibleValue(text="reg_invalid_type")
    reg_link = PermissibleValue(text="reg_link")
    reg_multi_sz = PermissibleValue(text="reg_multi_sz")
    reg_none = PermissibleValue(text="reg_none")
    reg_qword = PermissibleValue(text="reg_qword")
    reg_resource_list = PermissibleValue(text="reg_resource_list")
    reg_resource_requirements_list = PermissibleValue(text="reg_resource_requirements_list")
    reg_sz = PermissibleValue(text="reg_sz")

    _defn = EnumDefinition(
        name="RegistryDatatype",
        description="UCO 1.5.0 declares the vocabulary uco-observable:RegistryDatatype without a definition.",
    )

class WindowsPEBinaryType(EnumDefinitionImpl):
    """
    UCO 1.5.0 declares the vocabulary uco-observable:WindowsPEBinaryType without a definition.
    """
    dll = PermissibleValue(text="dll")
    exe = PermissibleValue(text="exe")
    sys = PermissibleValue(text="sys")

    _defn = EnumDefinition(
        name="WindowsPEBinaryType",
        description="UCO 1.5.0 declares the vocabulary uco-observable:WindowsPEBinaryType without a definition.",
    )

class WindowsServiceStartType(EnumDefinitionImpl):
    """
    UCO 1.5.0 declares the vocabulary uco-observable:WindowsServiceStartType without a definition.
    """
    service_auto_start = PermissibleValue(text="service_auto_start")
    service_boot_start = PermissibleValue(text="service_boot_start")
    service_demand_start = PermissibleValue(text="service_demand_start")
    service_disabled = PermissibleValue(text="service_disabled")
    service_system_alert = PermissibleValue(text="service_system_alert")

    _defn = EnumDefinition(
        name="WindowsServiceStartType",
        description="UCO 1.5.0 declares the vocabulary uco-observable:WindowsServiceStartType without a definition.",
    )

class WindowsServiceStatus(EnumDefinitionImpl):
    """
    UCO 1.5.0 declares the vocabulary uco-observable:WindowsServiceStatus without a definition.
    """
    service_continue_pending = PermissibleValue(text="service_continue_pending")
    service_pause_pending = PermissibleValue(text="service_pause_pending")
    service_paused = PermissibleValue(text="service_paused")
    service_running = PermissibleValue(text="service_running")
    service_start_pending = PermissibleValue(text="service_start_pending")
    service_stop_pending = PermissibleValue(text="service_stop_pending")
    service_stopped = PermissibleValue(text="service_stopped")

    _defn = EnumDefinition(
        name="WindowsServiceStatus",
        description="UCO 1.5.0 declares the vocabulary uco-observable:WindowsServiceStatus without a definition.",
    )

class WindowsServiceType(EnumDefinitionImpl):
    """
    UCO 1.5.0 declares the vocabulary uco-observable:WindowsServiceType without a definition.
    """
    service_file_system_driver = PermissibleValue(text="service_file_system_driver")
    service_kernel_driver = PermissibleValue(text="service_kernel_driver")
    service_win32_own_process = PermissibleValue(text="service_win32_own_process")
    service_win32_share_process = PermissibleValue(text="service_win32_share_process")

    _defn = EnumDefinition(
        name="WindowsServiceType",
        description="UCO 1.5.0 declares the vocabulary uco-observable:WindowsServiceType without a definition.",
    )

# Slots
class slots:
    pass

slots.graph = Slot(uri=UCO_LINKML.graph, name="graph", curie=UCO_LINKML.curie('graph'),
                   model_uri=UCO_LINKML.graph, domain=None, range=Optional[Union[Union[dict, UcoThing], list[Union[dict, UcoThing]]]])

slots.co_size = Slot(uri=COLL.size, name="co_size", curie=COLL.curie('size'),
                   model_uri=UCO_LINKML.co_size, domain=None, range=Optional[int])

slots.firstItem = Slot(uri=COLL.firstItem, name="firstItem", curie=COLL.curie('firstItem'),
                   model_uri=UCO_LINKML.firstItem, domain=None, range=Optional[Union[dict, ListItem]])

slots.followedBy = Slot(uri=COLL.followedBy, name="followedBy", curie=COLL.curie('followedBy'),
                   model_uri=UCO_LINKML.followedBy, domain=None, range=Optional[Union[Union[dict, CoItem], list[Union[dict, CoItem]]]])

slots.index = Slot(uri=COLL.index, name="index", curie=COLL.curie('index'),
                   model_uri=UCO_LINKML.index, domain=None, range=Optional[int])

slots.item = Slot(uri=COLL.item, name="item", curie=COLL.curie('item'),
                   model_uri=UCO_LINKML.item, domain=None, range=Optional[Union[str, list[str]]])

slots.itemContent = Slot(uri=COLL.itemContent, name="itemContent", curie=COLL.curie('itemContent'),
                   model_uri=UCO_LINKML.itemContent, domain=None, range=Optional[str])

slots.lastItem = Slot(uri=COLL.lastItem, name="lastItem", curie=COLL.curie('lastItem'),
                   model_uri=UCO_LINKML.lastItem, domain=None, range=Optional[Union[dict, ListItem]])

slots.nextItem = Slot(uri=COLL.nextItem, name="nextItem", curie=COLL.curie('nextItem'),
                   model_uri=UCO_LINKML.nextItem, domain=None, range=Optional[Union[dict, CoItem]])

slots.precededBy = Slot(uri=COLL.precededBy, name="precededBy", curie=COLL.curie('precededBy'),
                   model_uri=UCO_LINKML.precededBy, domain=None, range=Optional[Union[dict, CoItem]])

slots.previousItem = Slot(uri=COLL.previousItem, name="previousItem", curie=COLL.curie('previousItem'),
                   model_uri=UCO_LINKML.previousItem, domain=None, range=Optional[Union[dict, CoItem]])

slots.confidence = Slot(uri=UCO_CORE.confidence, name="confidence", curie=UCO_CORE.curie('confidence'),
                   model_uri=UCO_LINKML.confidence, domain=None, range=Union[int, UcoNonNegativeInteger])

slots.constrainingVocabularyName = Slot(uri=UCO_CORE.constrainingVocabularyName, name="constrainingVocabularyName", curie=UCO_CORE.curie('constrainingVocabularyName'),
                   model_uri=UCO_LINKML.constrainingVocabularyName, domain=None, range=Optional[str])

slots.constrainingVocabularyReference = Slot(uri=UCO_CORE.constrainingVocabularyReference, name="constrainingVocabularyReference", curie=UCO_CORE.curie('constrainingVocabularyReference'),
                   model_uri=UCO_LINKML.constrainingVocabularyReference, domain=None, range=Optional[Union[str, URI]])

slots.context = Slot(uri=UCO_CORE.context, name="context", curie=UCO_CORE.curie('context'),
                   model_uri=UCO_LINKML.context, domain=None, range=Optional[Union[str, list[str]]])

slots.createdBy = Slot(uri=UCO_CORE.createdBy, name="createdBy", curie=UCO_CORE.curie('createdBy'),
                   model_uri=UCO_LINKML.createdBy, domain=None, range=Optional[Union[str, IdentityAbstractionId]])

slots.definingContext = Slot(uri=UCO_CORE.definingContext, name="definingContext", curie=UCO_CORE.curie('definingContext'),
                   model_uri=UCO_LINKML.definingContext, domain=None, range=Optional[str])

slots.description = Slot(uri=UCO_CORE.description, name="description", curie=UCO_CORE.curie('description'),
                   model_uri=UCO_LINKML.description, domain=None, range=Optional[Union[str, list[str]]])

slots.endTime = Slot(uri=UCO_CORE.endTime, name="endTime", curie=UCO_CORE.curie('endTime'),
                   model_uri=UCO_LINKML.endTime, domain=None, range=Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]])

slots.entry = Slot(uri=UCO_TYPES.entry, name="entry", curie=UCO_TYPES.curie('entry'),
                   model_uri=UCO_LINKML.entry, domain=None, range=Optional[Union[Union[dict, DictionaryEntry], list[Union[dict, DictionaryEntry]]]])

slots.eventAttribute = Slot(uri=UCO_CORE.eventAttribute, name="eventAttribute", curie=UCO_CORE.curie('eventAttribute'),
                   model_uri=UCO_LINKML.eventAttribute, domain=None, range=Optional[Union[Union[dict, Dictionary], list[Union[dict, Dictionary]]]])

slots.eventContext = Slot(uri=UCO_CORE.eventContext, name="eventContext", curie=UCO_CORE.curie('eventContext'),
                   model_uri=UCO_LINKML.eventContext, domain=None, range=Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]])

slots.eventType = Slot(uri=UCO_CORE.eventType, name="eventType", curie=UCO_CORE.curie('eventType'),
                   model_uri=UCO_LINKML.eventType, domain=None, range=Optional[Union[str, list[str]]])

slots.externalIdentifier = Slot(uri=UCO_CORE.externalIdentifier, name="externalIdentifier", curie=UCO_CORE.curie('externalIdentifier'),
                   model_uri=UCO_LINKML.externalIdentifier, domain=None, range=Optional[str])

slots.externalReference = Slot(uri=UCO_CORE.externalReference, name="externalReference", curie=UCO_CORE.curie('externalReference'),
                   model_uri=UCO_LINKML.externalReference, domain=None, range=Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]])

slots.hasFacet = Slot(uri=UCO_CORE.hasFacet, name="hasFacet", curie=UCO_CORE.curie('hasFacet'),
                   model_uri=UCO_LINKML.hasFacet, domain=None, range=Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]])

slots.id = Slot(uri=UCO_LINKML.id, name="id", curie=UCO_LINKML.curie('id'),
                   model_uri=UCO_LINKML.id, domain=None, range=URIRef)

slots.informalType = Slot(uri=UCO_CORE.informalType, name="informalType", curie=UCO_CORE.curie('informalType'),
                   model_uri=UCO_LINKML.informalType, domain=None, range=Optional[str])

slots.isDirectional = Slot(uri=UCO_CORE.isDirectional, name="isDirectional", curie=UCO_CORE.curie('isDirectional'),
                   model_uri=UCO_LINKML.isDirectional, domain=None, range=Union[bool, Bool])

slots.key = Slot(uri=UCO_TYPES.key, name="key", curie=UCO_TYPES.curie('key'),
                   model_uri=UCO_LINKML.key, domain=None, range=str)

slots.kindOfRelationship = Slot(uri=UCO_CORE.kindOfRelationship, name="kindOfRelationship", curie=UCO_CORE.curie('kindOfRelationship'),
                   model_uri=UCO_LINKML.kindOfRelationship, domain=None, range=Optional[str])

slots.modifiedTime = Slot(uri=UCO_CORE.modifiedTime, name="modifiedTime", curie=UCO_CORE.curie('modifiedTime'),
                   model_uri=UCO_LINKML.modifiedTime, domain=None, range=Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]])

slots.name = Slot(uri=UCO_CORE.name, name="name", curie=UCO_CORE.curie('name'),
                   model_uri=UCO_LINKML.name, domain=None, range=Optional[str])

slots.namingAuthority = Slot(uri=UCO_CORE.namingAuthority, name="namingAuthority", curie=UCO_CORE.curie('namingAuthority'),
                   model_uri=UCO_LINKML.namingAuthority, domain=None, range=Optional[str])

slots.object = Slot(uri=UCO_CORE.object, name="object", curie=UCO_CORE.curie('object'),
                   model_uri=UCO_LINKML.object, domain=None, range=Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]])

slots.objectCreatedTime = Slot(uri=UCO_CORE.objectCreatedTime, name="objectCreatedTime", curie=UCO_CORE.curie('objectCreatedTime'),
                   model_uri=UCO_LINKML.objectCreatedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.objectMarking = Slot(uri=UCO_CORE.objectMarking, name="objectMarking", curie=UCO_CORE.curie('objectMarking'),
                   model_uri=UCO_LINKML.objectMarking, domain=None, range=Optional[Union[Union[str, MarkingDefinitionAbstractionId], list[Union[str, MarkingDefinitionAbstractionId]]]])

slots.objectStatus = Slot(uri=UCO_CORE.objectStatus, name="objectStatus", curie=UCO_CORE.curie('objectStatus'),
                   model_uri=UCO_LINKML.objectStatus, domain=None, range=Optional[Union[str, "ObjectStatusVocab"]])

slots.referenceURL = Slot(uri=UCO_CORE.referenceURL, name="referenceURL", curie=UCO_CORE.curie('referenceURL'),
                   model_uri=UCO_LINKML.referenceURL, domain=None, range=Optional[Union[str, URI]])

slots.source = Slot(uri=UCO_CORE.source, name="source", curie=UCO_CORE.curie('source'),
                   model_uri=UCO_LINKML.source, domain=None, range=Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]])

slots.specVersion = Slot(uri=UCO_CORE.specVersion, name="specVersion", curie=UCO_CORE.curie('specVersion'),
                   model_uri=UCO_LINKML.specVersion, domain=None, range=Optional[str])

slots.startTime = Slot(uri=UCO_CORE.startTime, name="startTime", curie=UCO_CORE.curie('startTime'),
                   model_uri=UCO_LINKML.startTime, domain=None, range=Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]])

slots.statement = Slot(uri=UCO_CORE.statement, name="statement", curie=UCO_CORE.curie('statement'),
                   model_uri=UCO_LINKML.statement, domain=None, range=Optional[Union[str, list[str]]])

slots.tag = Slot(uri=UCO_CORE.tag, name="tag", curie=UCO_CORE.curie('tag'),
                   model_uri=UCO_LINKML.tag, domain=None, range=Optional[Union[str, list[str]]])

slots.target = Slot(uri=UCO_CORE.target, name="target", curie=UCO_CORE.curie('target'),
                   model_uri=UCO_LINKML.target, domain=None, range=Union[str, UcoObjectId])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=UCO_LINKML.type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.types_value = Slot(uri=UCO_TYPES.value, name="types_value", curie=UCO_TYPES.curie('value'),
                   model_uri=UCO_LINKML.types_value, domain=None, range=str)

slots.value = Slot(uri=UCO_CORE.value, name="value", curie=UCO_CORE.curie('value'),
                   model_uri=UCO_LINKML.value, domain=None, range=str)

slots.configurationEntry = Slot(uri=UCO_CONFIGURATION.configurationEntry, name="configurationEntry", curie=UCO_CONFIGURATION.curie('configurationEntry'),
                   model_uri=UCO_LINKML.configurationEntry, domain=None, range=Optional[Union[Union[dict, ConfigurationEntry], list[Union[dict, ConfigurationEntry]]]])

slots.dependencies = Slot(uri=UCO_CONFIGURATION.dependencies, name="dependencies", curie=UCO_CONFIGURATION.curie('dependencies'),
                   model_uri=UCO_LINKML.dependencies, domain=None, range=Optional[Union[Union[dict, Dependency], list[Union[dict, Dependency]]]])

slots.dependencyDescription = Slot(uri=UCO_CONFIGURATION.dependencyDescription, name="dependencyDescription", curie=UCO_CONFIGURATION.curie('dependencyDescription'),
                   model_uri=UCO_LINKML.dependencyDescription, domain=None, range=Optional[str])

slots.dependencyType = Slot(uri=UCO_CONFIGURATION.dependencyType, name="dependencyType", curie=UCO_CONFIGURATION.curie('dependencyType'),
                   model_uri=UCO_LINKML.dependencyType, domain=None, range=Optional[str])

slots.isConfigurationOf = Slot(uri=UCO_CONFIGURATION.isConfigurationOf, name="isConfigurationOf", curie=UCO_CONFIGURATION.curie('isConfigurationOf'),
                   model_uri=UCO_LINKML.isConfigurationOf, domain=None, range=Optional[Union[str, UcoObjectId]])

slots.itemDescription = Slot(uri=UCO_CONFIGURATION.itemDescription, name="itemDescription", curie=UCO_CONFIGURATION.curie('itemDescription'),
                   model_uri=UCO_LINKML.itemDescription, domain=None, range=Optional[str])

slots.itemName = Slot(uri=UCO_CONFIGURATION.itemName, name="itemName", curie=UCO_CONFIGURATION.curie('itemName'),
                   model_uri=UCO_LINKML.itemName, domain=None, range=Optional[str])

slots.itemObject = Slot(uri=UCO_CONFIGURATION.itemObject, name="itemObject", curie=UCO_CONFIGURATION.curie('itemObject'),
                   model_uri=UCO_LINKML.itemObject, domain=None, range=Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]])

slots.itemType = Slot(uri=UCO_CONFIGURATION.itemType, name="itemType", curie=UCO_CONFIGURATION.curie('itemType'),
                   model_uri=UCO_LINKML.itemType, domain=None, range=Optional[str])

slots.itemValue = Slot(uri=UCO_CONFIGURATION.itemValue, name="itemValue", curie=UCO_CONFIGURATION.curie('itemValue'),
                   model_uri=UCO_LINKML.itemValue, domain=None, range=Optional[Union[str, list[str]]])

slots.usageContextAssumptions = Slot(uri=UCO_CONFIGURATION.usageContextAssumptions, name="usageContextAssumptions", curie=UCO_CONFIGURATION.curie('usageContextAssumptions'),
                   model_uri=UCO_LINKML.usageContextAssumptions, domain=None, range=Optional[Union[str, list[str]]])

slots.usesConfiguration = Slot(uri=UCO_CONFIGURATION.usesConfiguration, name="usesConfiguration", curie=UCO_CONFIGURATION.curie('usesConfiguration'),
                   model_uri=UCO_LINKML.usesConfiguration, domain=None, range=Optional[Union[str, ConfigurationId]])

slots.addressType = Slot(uri=UCO_LOCATION.addressType, name="addressType", curie=UCO_LOCATION.curie('addressType'),
                   model_uri=UCO_LINKML.addressType, domain=None, range=Optional[str])

slots.altitude = Slot(uri=UCO_LOCATION.altitude, name="altitude", curie=UCO_LOCATION.curie('altitude'),
                   model_uri=UCO_LINKML.altitude, domain=None, range=Optional[Decimal])

slots.country = Slot(uri=UCO_LOCATION.country, name="country", curie=UCO_LOCATION.curie('country'),
                   model_uri=UCO_LINKML.country, domain=None, range=Optional[str])

slots.hdop = Slot(uri=UCO_LOCATION.hdop, name="hdop", curie=UCO_LOCATION.curie('hdop'),
                   model_uri=UCO_LINKML.hdop, domain=None, range=Optional[Decimal])

slots.latitude = Slot(uri=UCO_LOCATION.latitude, name="latitude", curie=UCO_LOCATION.curie('latitude'),
                   model_uri=UCO_LINKML.latitude, domain=None, range=Optional[Decimal])

slots.locality = Slot(uri=UCO_LOCATION.locality, name="locality", curie=UCO_LOCATION.curie('locality'),
                   model_uri=UCO_LINKML.locality, domain=None, range=Optional[str])

slots.longitude = Slot(uri=UCO_LOCATION.longitude, name="longitude", curie=UCO_LOCATION.curie('longitude'),
                   model_uri=UCO_LINKML.longitude, domain=None, range=Optional[Decimal])

slots.pdop = Slot(uri=UCO_LOCATION.pdop, name="pdop", curie=UCO_LOCATION.curie('pdop'),
                   model_uri=UCO_LINKML.pdop, domain=None, range=Optional[Decimal])

slots.postalCode = Slot(uri=UCO_LOCATION.postalCode, name="postalCode", curie=UCO_LOCATION.curie('postalCode'),
                   model_uri=UCO_LINKML.postalCode, domain=None, range=Optional[str])

slots.region = Slot(uri=UCO_LOCATION.region, name="region", curie=UCO_LOCATION.curie('region'),
                   model_uri=UCO_LINKML.region, domain=None, range=Optional[str])

slots.street = Slot(uri=UCO_LOCATION.street, name="street", curie=UCO_LOCATION.curie('street'),
                   model_uri=UCO_LINKML.street, domain=None, range=Optional[str])

slots.tdop = Slot(uri=UCO_LOCATION.tdop, name="tdop", curie=UCO_LOCATION.curie('tdop'),
                   model_uri=UCO_LINKML.tdop, domain=None, range=Optional[Decimal])

slots.vdop = Slot(uri=UCO_LOCATION.vdop, name="vdop", curie=UCO_LOCATION.curie('vdop'),
                   model_uri=UCO_LINKML.vdop, domain=None, range=Optional[Decimal])

slots.address = Slot(uri=UCO_IDENTITY.address, name="address", curie=UCO_IDENTITY.curie('address'),
                   model_uri=UCO_LINKML.address, domain=None, range=Optional[Union[str, LocationId]])

slots.birthdate = Slot(uri=UCO_IDENTITY.birthdate, name="birthdate", curie=UCO_IDENTITY.curie('birthdate'),
                   model_uri=UCO_LINKML.birthdate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.familyName = Slot(uri=UCO_IDENTITY.familyName, name="familyName", curie=UCO_IDENTITY.curie('familyName'),
                   model_uri=UCO_LINKML.familyName, domain=None, range=Optional[Union[str, list[str]]])

slots.givenName = Slot(uri=UCO_IDENTITY.givenName, name="givenName", curie=UCO_IDENTITY.curie('givenName'),
                   model_uri=UCO_LINKML.givenName, domain=None, range=Optional[Union[str, list[str]]])

slots.honorificPrefix = Slot(uri=UCO_IDENTITY.honorificPrefix, name="honorificPrefix", curie=UCO_IDENTITY.curie('honorificPrefix'),
                   model_uri=UCO_LINKML.honorificPrefix, domain=None, range=Optional[Union[str, list[str]]])

slots.honorificSuffix = Slot(uri=UCO_IDENTITY.honorificSuffix, name="honorificSuffix", curie=UCO_IDENTITY.curie('honorificSuffix'),
                   model_uri=UCO_LINKML.honorificSuffix, domain=None, range=Optional[Union[str, list[str]]])

slots.authorizedIdentities = Slot(uri=UCO_MARKING.authorizedIdentities, name="authorizedIdentities", curie=UCO_MARKING.curie('authorizedIdentities'),
                   model_uri=UCO_LINKML.authorizedIdentities, domain=None, range=Union[str, list[str]])

slots.contentSelectors = Slot(uri=UCO_MARKING.contentSelectors, name="contentSelectors", curie=UCO_MARKING.curie('contentSelectors'),
                   model_uri=UCO_LINKML.contentSelectors, domain=None, range=Optional[Union[str, list[str]]])

slots.definition = Slot(uri=UCO_MARKING.definition, name="definition", curie=UCO_MARKING.curie('definition'),
                   model_uri=UCO_LINKML.definition, domain=None, range=Optional[Union[Union[dict, MarkingModel], list[Union[dict, MarkingModel]]]])

slots.definitionType = Slot(uri=UCO_MARKING.definitionType, name="definitionType", curie=UCO_MARKING.curie('definitionType'),
                   model_uri=UCO_LINKML.definitionType, domain=None, range=Optional[str])

slots.license = Slot(uri=UCO_MARKING.license, name="license", curie=UCO_MARKING.curie('license'),
                   model_uri=UCO_LINKML.license, domain=None, range=str)

slots.marking = Slot(uri=UCO_MARKING.marking, name="marking", curie=UCO_MARKING.curie('marking'),
                   model_uri=UCO_LINKML.marking, domain=None, range=Optional[Union[Union[str, MarkingDefinitionId], list[Union[str, MarkingDefinitionId]]]])

slots.marking_statement = Slot(uri=UCO_MARKING.statement, name="marking_statement", curie=UCO_MARKING.curie('statement'),
                   model_uri=UCO_LINKML.marking_statement, domain=None, range=str)

slots.termsOfUse = Slot(uri=UCO_MARKING.termsOfUse, name="termsOfUse", curie=UCO_MARKING.curie('termsOfUse'),
                   model_uri=UCO_LINKML.termsOfUse, domain=None, range=str)

slots.patternExpression = Slot(uri=UCO_PATTERN.patternExpression, name="patternExpression", curie=UCO_PATTERN.curie('patternExpression'),
                   model_uri=UCO_LINKML.patternExpression, domain=None, range=Optional[str])

slots.buildConfiguration = Slot(uri=UCO_TOOL.buildConfiguration, name="buildConfiguration", curie=UCO_TOOL.curie('buildConfiguration'),
                   model_uri=UCO_LINKML.buildConfiguration, domain=None, range=Optional[Union[str, ConfigurationId]])

slots.buildID = Slot(uri=UCO_TOOL.buildID, name="buildID", curie=UCO_TOOL.curie('buildID'),
                   model_uri=UCO_LINKML.buildID, domain=None, range=Optional[str])

slots.buildInformation = Slot(uri=UCO_TOOL.buildInformation, name="buildInformation", curie=UCO_TOOL.curie('buildInformation'),
                   model_uri=UCO_LINKML.buildInformation, domain=None, range=Optional[Union[dict, BuildInformationType]])

slots.buildLabel = Slot(uri=UCO_TOOL.buildLabel, name="buildLabel", curie=UCO_TOOL.curie('buildLabel'),
                   model_uri=UCO_LINKML.buildLabel, domain=None, range=Optional[str])

slots.buildOutputLog = Slot(uri=UCO_TOOL.buildOutputLog, name="buildOutputLog", curie=UCO_TOOL.curie('buildOutputLog'),
                   model_uri=UCO_LINKML.buildOutputLog, domain=None, range=Optional[str])

slots.buildProject = Slot(uri=UCO_TOOL.buildProject, name="buildProject", curie=UCO_TOOL.curie('buildProject'),
                   model_uri=UCO_LINKML.buildProject, domain=None, range=Optional[str])

slots.buildScript = Slot(uri=UCO_TOOL.buildScript, name="buildScript", curie=UCO_TOOL.curie('buildScript'),
                   model_uri=UCO_LINKML.buildScript, domain=None, range=Optional[str])

slots.buildUtility = Slot(uri=UCO_TOOL.buildUtility, name="buildUtility", curie=UCO_TOOL.curie('buildUtility'),
                   model_uri=UCO_LINKML.buildUtility, domain=None, range=Optional[Union[dict, BuildUtilityType]])

slots.buildUtilityName = Slot(uri=UCO_TOOL.buildUtilityName, name="buildUtilityName", curie=UCO_TOOL.curie('buildUtilityName'),
                   model_uri=UCO_LINKML.buildUtilityName, domain=None, range=Optional[str])

slots.buildVersion = Slot(uri=UCO_TOOL.buildVersion, name="buildVersion", curie=UCO_TOOL.curie('buildVersion'),
                   model_uri=UCO_LINKML.buildVersion, domain=None, range=Optional[str])

slots.compilationDate = Slot(uri=UCO_TOOL.compilationDate, name="compilationDate", curie=UCO_TOOL.curie('compilationDate'),
                   model_uri=UCO_LINKML.compilationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.compilerInformalDescription = Slot(uri=UCO_TOOL.compilerInformalDescription, name="compilerInformalDescription", curie=UCO_TOOL.curie('compilerInformalDescription'),
                   model_uri=UCO_LINKML.compilerInformalDescription, domain=None, range=Optional[str])

slots.compilers = Slot(uri=UCO_TOOL.compilers, name="compilers", curie=UCO_TOOL.curie('compilers'),
                   model_uri=UCO_LINKML.compilers, domain=None, range=Optional[Union[Union[dict, CompilerType], list[Union[dict, CompilerType]]]])

slots.cpeid = Slot(uri=UCO_TOOL.cpeid, name="cpeid", curie=UCO_TOOL.curie('cpeid'),
                   model_uri=UCO_LINKML.cpeid, domain=None, range=Optional[str])

slots.creator = Slot(uri=UCO_TOOL.creator, name="creator", curie=UCO_TOOL.curie('creator'),
                   model_uri=UCO_LINKML.creator, domain=None, range=Optional[Union[str, IdentityId]])

slots.libraries = Slot(uri=UCO_TOOL.libraries, name="libraries", curie=UCO_TOOL.curie('libraries'),
                   model_uri=UCO_LINKML.libraries, domain=None, range=Optional[Union[Union[dict, LibraryType], list[Union[dict, LibraryType]]]])

slots.libraryName = Slot(uri=UCO_TOOL.libraryName, name="libraryName", curie=UCO_TOOL.curie('libraryName'),
                   model_uri=UCO_LINKML.libraryName, domain=None, range=Optional[str])

slots.libraryVersion = Slot(uri=UCO_TOOL.libraryVersion, name="libraryVersion", curie=UCO_TOOL.curie('libraryVersion'),
                   model_uri=UCO_LINKML.libraryVersion, domain=None, range=Optional[str])

slots.references = Slot(uri=UCO_TOOL.references, name="references", curie=UCO_TOOL.curie('references'),
                   model_uri=UCO_LINKML.references, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.servicePack = Slot(uri=UCO_TOOL.servicePack, name="servicePack", curie=UCO_TOOL.curie('servicePack'),
                   model_uri=UCO_LINKML.servicePack, domain=None, range=Optional[str])

slots.swid = Slot(uri=UCO_TOOL.swid, name="swid", curie=UCO_TOOL.curie('swid'),
                   model_uri=UCO_LINKML.swid, domain=None, range=Optional[str])

slots.toolType = Slot(uri=UCO_TOOL.toolType, name="toolType", curie=UCO_TOOL.curie('toolType'),
                   model_uri=UCO_LINKML.toolType, domain=None, range=Optional[str])

slots.version = Slot(uri=UCO_TOOL.version, name="version", curie=UCO_TOOL.curie('version'),
                   model_uri=UCO_LINKML.version, domain=None, range=Optional[str])

slots.hashMethod = Slot(uri=UCO_TYPES.hashMethod, name="hashMethod", curie=UCO_TYPES.curie('hashMethod'),
                   model_uri=UCO_LINKML.hashMethod, domain=None, range=Union[str, "HashNameVocab"])

slots.hashValue = Slot(uri=UCO_TYPES.hashValue, name="hashValue", curie=UCO_TYPES.curie('hashValue'),
                   model_uri=UCO_LINKML.hashValue, domain=None, range=Union[str, UcoHexBinary])

slots.repeatsKey = Slot(uri=UCO_TYPES.repeatsKey, name="repeatsKey", curie=UCO_TYPES.curie('repeatsKey'),
                   model_uri=UCO_LINKML.repeatsKey, domain=ImproperDictionary, range=Optional[Union[str, list[str]]])

slots.threadNextItem = Slot(uri=UCO_TYPES.threadNextItem, name="threadNextItem", curie=UCO_TYPES.curie('threadNextItem'),
                   model_uri=UCO_LINKML.threadNextItem, domain=ThreadItem, range=Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]])

slots.threadOriginItem = Slot(uri=UCO_TYPES.threadOriginItem, name="threadOriginItem", curie=UCO_TYPES.curie('threadOriginItem'),
                   model_uri=UCO_LINKML.threadOriginItem, domain=Thread, range=Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]])

slots.threadPredecessor = Slot(uri=UCO_TYPES.threadPredecessor, name="threadPredecessor", curie=UCO_TYPES.curie('threadPredecessor'),
                   model_uri=UCO_LINKML.threadPredecessor, domain=ThreadItem, range=Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]])

slots.threadPreviousItem = Slot(uri=UCO_TYPES.threadPreviousItem, name="threadPreviousItem", curie=UCO_TYPES.curie('threadPreviousItem'),
                   model_uri=UCO_LINKML.threadPreviousItem, domain=ThreadItem, range=Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]])

slots.threadSuccessor = Slot(uri=UCO_TYPES.threadSuccessor, name="threadSuccessor", curie=UCO_TYPES.curie('threadSuccessor'),
                   model_uri=UCO_LINKML.threadSuccessor, domain=ThreadItem, range=Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]])

slots.threadTerminalItem = Slot(uri=UCO_TYPES.threadTerminalItem, name="threadTerminalItem", curie=UCO_TYPES.curie('threadTerminalItem'),
                   model_uri=UCO_LINKML.threadTerminalItem, domain=Thread, range=Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]])

slots.action = Slot(uri=UCO_ACTION.action, name="action", curie=UCO_ACTION.curie('action'),
                   model_uri=UCO_LINKML.action, domain=None, range=Union[Union[str, ActionId], list[Union[str, ActionId]]])

slots.actionCount = Slot(uri=UCO_ACTION.actionCount, name="actionCount", curie=UCO_ACTION.curie('actionCount'),
                   model_uri=UCO_LINKML.actionCount, domain=None, range=Optional[Union[int, UcoNonNegativeInteger]])

slots.actionStatus = Slot(uri=UCO_ACTION.actionStatus, name="actionStatus", curie=UCO_ACTION.curie('actionStatus'),
                   model_uri=UCO_LINKML.actionStatus, domain=None, range=Optional[Union[str, "ActionStatusTypeVocab"]])

slots.action_endTime = Slot(uri=UCO_ACTION.endTime, name="action_endTime", curie=UCO_ACTION.curie('endTime'),
                   model_uri=UCO_LINKML.action_endTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.action_object = Slot(uri=UCO_ACTION.object, name="action_object", curie=UCO_ACTION.curie('object'),
                   model_uri=UCO_LINKML.action_object, domain=None, range=Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]])

slots.action_startTime = Slot(uri=UCO_ACTION.startTime, name="action_startTime", curie=UCO_ACTION.curie('startTime'),
                   model_uri=UCO_LINKML.action_startTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.action_value = Slot(uri=UCO_ACTION.value, name="action_value", curie=UCO_ACTION.curie('value'),
                   model_uri=UCO_LINKML.action_value, domain=None, range=str)

slots.argumentName = Slot(uri=UCO_ACTION.argumentName, name="argumentName", curie=UCO_ACTION.curie('argumentName'),
                   model_uri=UCO_LINKML.argumentName, domain=None, range=str)

slots.environment = Slot(uri=UCO_ACTION.environment, name="environment", curie=UCO_ACTION.curie('environment'),
                   model_uri=UCO_LINKML.environment, domain=None, range=Optional[Union[str, UcoObjectId]])

slots.error = Slot(uri=UCO_ACTION.error, name="error", curie=UCO_ACTION.curie('error'),
                   model_uri=UCO_LINKML.error, domain=None, range=Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]])

slots.estimatedCost = Slot(uri=UCO_ACTION.estimatedCost, name="estimatedCost", curie=UCO_ACTION.curie('estimatedCost'),
                   model_uri=UCO_LINKML.estimatedCost, domain=None, range=Optional[str])

slots.estimatedEfficacy = Slot(uri=UCO_ACTION.estimatedEfficacy, name="estimatedEfficacy", curie=UCO_ACTION.curie('estimatedEfficacy'),
                   model_uri=UCO_LINKML.estimatedEfficacy, domain=None, range=Optional[str])

slots.estimatedImpact = Slot(uri=UCO_ACTION.estimatedImpact, name="estimatedImpact", curie=UCO_ACTION.curie('estimatedImpact'),
                   model_uri=UCO_LINKML.estimatedImpact, domain=None, range=Optional[str])

slots.instrument = Slot(uri=UCO_ACTION.instrument, name="instrument", curie=UCO_ACTION.curie('instrument'),
                   model_uri=UCO_LINKML.instrument, domain=None, range=Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]])

slots.location = Slot(uri=UCO_ACTION.location, name="location", curie=UCO_ACTION.curie('location'),
                   model_uri=UCO_LINKML.location, domain=None, range=Optional[Union[Union[str, LocationId], list[Union[str, LocationId]]]])

slots.objective = Slot(uri=UCO_ACTION.objective, name="objective", curie=UCO_ACTION.curie('objective'),
                   model_uri=UCO_LINKML.objective, domain=None, range=Optional[str])

slots.participant = Slot(uri=UCO_ACTION.participant, name="participant", curie=UCO_ACTION.curie('participant'),
                   model_uri=UCO_LINKML.participant, domain=None, range=Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]])

slots.performer = Slot(uri=UCO_ACTION.performer, name="performer", curie=UCO_ACTION.curie('performer'),
                   model_uri=UCO_LINKML.performer, domain=None, range=Optional[Union[str, UcoObjectId]])

slots.phase = Slot(uri=UCO_ACTION.phase, name="phase", curie=UCO_ACTION.curie('phase'),
                   model_uri=UCO_LINKML.phase, domain=None, range=Union[Union[dict, ArrayOfAction], list[Union[dict, ArrayOfAction]]])

slots.rate = Slot(uri=UCO_ACTION.rate, name="rate", curie=UCO_ACTION.curie('rate'),
                   model_uri=UCO_LINKML.rate, domain=None, range=Decimal)

slots.result = Slot(uri=UCO_ACTION.result, name="result", curie=UCO_ACTION.curie('result'),
                   model_uri=UCO_LINKML.result, domain=None, range=Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]])

slots.scale = Slot(uri=UCO_ACTION.scale, name="scale", curie=UCO_ACTION.curie('scale'),
                   model_uri=UCO_LINKML.scale, domain=None, range=str)

slots.subaction = Slot(uri=UCO_ACTION.subaction, name="subaction", curie=UCO_ACTION.curie('subaction'),
                   model_uri=UCO_LINKML.subaction, domain=None, range=Optional[Union[Union[str, ActionId], list[Union[str, ActionId]]]])

slots.techniqueID = Slot(uri=UCO_ACTION.techniqueID, name="techniqueID", curie=UCO_ACTION.curie('techniqueID'),
                   model_uri=UCO_LINKML.techniqueID, domain=Technique, range=Optional[Union[str, list[str]]])

slots.trend = Slot(uri=UCO_ACTION.trend, name="trend", curie=UCO_ACTION.curie('trend'),
                   model_uri=UCO_LINKML.trend, domain=None, range=Union[str, "TrendVocab"])

slots.units = Slot(uri=UCO_ACTION.units, name="units", curie=UCO_ACTION.curie('units'),
                   model_uri=UCO_LINKML.units, domain=None, range=str)

slots.class_ = Slot(uri=UCO_ANALYSIS['class'], name="class", curie=UCO_ANALYSIS.curie('class'),
                   model_uri=UCO_LINKML.class_, domain=None, range=Union[str, list[str]])

slots.classification = Slot(uri=UCO_ANALYSIS.classification, name="classification", curie=UCO_ANALYSIS.curie('classification'),
                   model_uri=UCO_LINKML.classification, domain=None, range=Optional[Union[Union[dict, ArtifactClassification], list[Union[dict, ArtifactClassification]]]])

slots.classificationConfidence = Slot(uri=UCO_ANALYSIS.classificationConfidence, name="classificationConfidence", curie=UCO_ANALYSIS.curie('classificationConfidence'),
                   model_uri=UCO_LINKML.classificationConfidence, domain=None, range=Optional[Decimal])

slots.originatingAnalysis = Slot(uri=UCO_ANALYSIS.originatingAnalysis, name="originatingAnalysis", curie=UCO_ANALYSIS.curie('originatingAnalysis'),
                   model_uri=UCO_LINKML.originatingAnalysis, domain=None, range=Optional[Union[str, AnalysisId]])

slots.resultContent = Slot(uri=UCO_ANALYSIS.resultContent, name="resultContent", curie=UCO_ANALYSIS.curie('resultContent'),
                   model_uri=UCO_LINKML.resultContent, domain=None, range=Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]])

slots.ESN = Slot(uri=UCO_OBSERVABLE.ESN, name="ESN", curie=UCO_OBSERVABLE.curie('ESN'),
                   model_uri=UCO_LINKML.ESN, domain=None, range=Optional[str])

slots.ICCID = Slot(uri=UCO_OBSERVABLE.ICCID, name="ICCID", curie=UCO_OBSERVABLE.curie('ICCID'),
                   model_uri=UCO_LINKML.ICCID, domain=None, range=Optional[str])

slots.IMEI = Slot(uri=UCO_OBSERVABLE.IMEI, name="IMEI", curie=UCO_OBSERVABLE.curie('IMEI'),
                   model_uri=UCO_LINKML.IMEI, domain=None, range=Optional[Union[str, list[str]]])

slots.IMSI = Slot(uri=UCO_OBSERVABLE.IMSI, name="IMSI", curie=UCO_OBSERVABLE.curie('IMSI'),
                   model_uri=UCO_LINKML.IMSI, domain=None, range=Optional[str])

slots.MSISDN = Slot(uri=UCO_OBSERVABLE.MSISDN, name="MSISDN", curie=UCO_OBSERVABLE.curie('MSISDN'),
                   model_uri=UCO_LINKML.MSISDN, domain=None, range=Optional[str])

slots.MSISDNType = Slot(uri=UCO_OBSERVABLE.MSISDNType, name="MSISDNType", curie=UCO_OBSERVABLE.curie('MSISDNType'),
                   model_uri=UCO_LINKML.MSISDNType, domain=None, range=Optional[str])

slots.PIN = Slot(uri=UCO_OBSERVABLE.PIN, name="PIN", curie=UCO_OBSERVABLE.curie('PIN'),
                   model_uri=UCO_LINKML.PIN, domain=None, range=Optional[str])

slots.PUK = Slot(uri=UCO_OBSERVABLE.PUK, name="PUK", curie=UCO_OBSERVABLE.curie('PUK'),
                   model_uri=UCO_LINKML.PUK, domain=None, range=Optional[str])

slots.SIMForm = Slot(uri=UCO_OBSERVABLE.SIMForm, name="SIMForm", curie=UCO_OBSERVABLE.curie('SIMForm'),
                   model_uri=UCO_LINKML.SIMForm, domain=None, range=Optional[str])

slots.SIMType = Slot(uri=UCO_OBSERVABLE.SIMType, name="SIMType", curie=UCO_OBSERVABLE.curie('SIMType'),
                   model_uri=UCO_LINKML.SIMType, domain=None, range=Optional[str])

slots.abbreviation = Slot(uri=UCO_OBSERVABLE.abbreviation, name="abbreviation", curie=UCO_OBSERVABLE.curie('abbreviation'),
                   model_uri=UCO_LINKML.abbreviation, domain=None, range=Optional[str])

slots.accessedDirectory = Slot(uri=UCO_OBSERVABLE.accessedDirectory, name="accessedDirectory", curie=UCO_OBSERVABLE.curie('accessedDirectory'),
                   model_uri=UCO_LINKML.accessedDirectory, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.accessedFile = Slot(uri=UCO_OBSERVABLE.accessedFile, name="accessedFile", curie=UCO_OBSERVABLE.curie('accessedFile'),
                   model_uri=UCO_LINKML.accessedFile, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.accessedTime = Slot(uri=UCO_OBSERVABLE.accessedTime, name="accessedTime", curie=UCO_OBSERVABLE.curie('accessedTime'),
                   model_uri=UCO_LINKML.accessedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.account = Slot(uri=UCO_OBSERVABLE.account, name="account", curie=UCO_OBSERVABLE.curie('account'),
                   model_uri=UCO_LINKML.account, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.accountIdentifier = Slot(uri=UCO_OBSERVABLE.accountIdentifier, name="accountIdentifier", curie=UCO_OBSERVABLE.curie('accountIdentifier'),
                   model_uri=UCO_LINKML.accountIdentifier, domain=None, range=Optional[str])

slots.accountIssuer = Slot(uri=UCO_OBSERVABLE.accountIssuer, name="accountIssuer", curie=UCO_OBSERVABLE.curie('accountIssuer'),
                   model_uri=UCO_LINKML.accountIssuer, domain=None, range=Optional[Union[str, UcoObjectId]])

slots.accountLogin = Slot(uri=UCO_OBSERVABLE.accountLogin, name="accountLogin", curie=UCO_OBSERVABLE.curie('accountLogin'),
                   model_uri=UCO_LINKML.accountLogin, domain=None, range=Optional[Union[str, list[str]]])

slots.accountLogonType = Slot(uri=UCO_OBSERVABLE.accountLogonType, name="accountLogonType", curie=UCO_OBSERVABLE.curie('accountLogonType'),
                   model_uri=UCO_LINKML.accountLogonType, domain=None, range=Optional[str])

slots.accountRunLevel = Slot(uri=UCO_OBSERVABLE.accountRunLevel, name="accountRunLevel", curie=UCO_OBSERVABLE.curie('accountRunLevel'),
                   model_uri=UCO_LINKML.accountRunLevel, domain=None, range=Optional[str])

slots.accountType = Slot(uri=UCO_OBSERVABLE.accountType, name="accountType", curie=UCO_OBSERVABLE.curie('accountType'),
                   model_uri=UCO_LINKML.accountType, domain=None, range=Optional[Union[str, "AccountTypeVocab"]])

slots.actionID = Slot(uri=UCO_OBSERVABLE.actionID, name="actionID", curie=UCO_OBSERVABLE.curie('actionID'),
                   model_uri=UCO_LINKML.actionID, domain=None, range=Optional[str])

slots.actionList = Slot(uri=UCO_OBSERVABLE.actionList, name="actionList", curie=UCO_OBSERVABLE.curie('actionList'),
                   model_uri=UCO_LINKML.actionList, domain=None, range=Optional[Union[Union[dict, TaskActionType], list[Union[dict, TaskActionType]]]])

slots.actionType = Slot(uri=UCO_OBSERVABLE.actionType, name="actionType", curie=UCO_OBSERVABLE.curie('actionType'),
                   model_uri=UCO_LINKML.actionType, domain=None, range=Optional[Union[str, "TaskActionTypeVocab"]])

slots.activeDirectoryGroups = Slot(uri=UCO_OBSERVABLE.activeDirectoryGroups, name="activeDirectoryGroups", curie=UCO_OBSERVABLE.curie('activeDirectoryGroups'),
                   model_uri=UCO_LINKML.activeDirectoryGroups, domain=None, range=Optional[Union[str, list[str]]])

slots.adapterName = Slot(uri=UCO_OBSERVABLE.adapterName, name="adapterName", curie=UCO_OBSERVABLE.curie('adapterName'),
                   model_uri=UCO_LINKML.adapterName, domain=None, range=Optional[str])

slots.addressOfEntryPoint = Slot(uri=UCO_OBSERVABLE.addressOfEntryPoint, name="addressOfEntryPoint", curie=UCO_OBSERVABLE.curie('addressOfEntryPoint'),
                   model_uri=UCO_LINKML.addressOfEntryPoint, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.addressValue = Slot(uri=UCO_OBSERVABLE.addressValue, name="addressValue", curie=UCO_OBSERVABLE.curie('addressValue'),
                   model_uri=UCO_LINKML.addressValue, domain=None, range=Optional[str])

slots.advertisingID = Slot(uri=UCO_OBSERVABLE.advertisingID, name="advertisingID", curie=UCO_OBSERVABLE.curie('advertisingID'),
                   model_uri=UCO_LINKML.advertisingID, domain=None, range=Optional[Union[str, list[str]]])

slots.allocationStatus = Slot(uri=UCO_OBSERVABLE.allocationStatus, name="allocationStatus", curie=UCO_OBSERVABLE.curie('allocationStatus'),
                   model_uri=UCO_LINKML.allocationStatus, domain=None, range=Optional[str])

slots.alternateDataStreams = Slot(uri=UCO_OBSERVABLE.alternateDataStreams, name="alternateDataStreams", curie=UCO_OBSERVABLE.curie('alternateDataStreams'),
                   model_uri=UCO_LINKML.alternateDataStreams, domain=None, range=Optional[Union[Union[str, AlternateDataStreamId], list[Union[str, AlternateDataStreamId]]]])

slots.androidFingerprint = Slot(uri=UCO_OBSERVABLE.androidFingerprint, name="androidFingerprint", curie=UCO_OBSERVABLE.curie('androidFingerprint'),
                   model_uri=UCO_LINKML.androidFingerprint, domain=None, range=Optional[str])

slots.androidID = Slot(uri=UCO_OBSERVABLE.androidID, name="androidID", curie=UCO_OBSERVABLE.curie('androidID'),
                   model_uri=UCO_LINKML.androidID, domain=None, range=Optional[Union[str, UcoHexBinary]])

slots.androidVersion = Slot(uri=UCO_OBSERVABLE.androidVersion, name="androidVersion", curie=UCO_OBSERVABLE.curie('androidVersion'),
                   model_uri=UCO_LINKML.androidVersion, domain=None, range=Optional[str])

slots.antennaHeight = Slot(uri=UCO_OBSERVABLE.antennaHeight, name="antennaHeight", curie=UCO_OBSERVABLE.curie('antennaHeight'),
                   model_uri=UCO_LINKML.antennaHeight, domain=None, range=Optional[Decimal])

slots.application = Slot(uri=UCO_OBSERVABLE.application, name="application", curie=UCO_OBSERVABLE.curie('application'),
                   model_uri=UCO_LINKML.application, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.applicationFileName = Slot(uri=UCO_OBSERVABLE.applicationFileName, name="applicationFileName", curie=UCO_OBSERVABLE.curie('applicationFileName'),
                   model_uri=UCO_LINKML.applicationFileName, domain=None, range=Optional[str])

slots.applicationIdentifier = Slot(uri=UCO_OBSERVABLE.applicationIdentifier, name="applicationIdentifier", curie=UCO_OBSERVABLE.curie('applicationIdentifier'),
                   model_uri=UCO_LINKML.applicationIdentifier, domain=None, range=Optional[str])

slots.archiveType = Slot(uri=UCO_OBSERVABLE.archiveType, name="archiveType", curie=UCO_OBSERVABLE.curie('archiveType'),
                   model_uri=UCO_LINKML.archiveType, domain=None, range=Optional[str])

slots.arguments = Slot(uri=UCO_OBSERVABLE.arguments, name="arguments", curie=UCO_OBSERVABLE.curie('arguments'),
                   model_uri=UCO_LINKML.arguments, domain=None, range=Optional[Union[str, list[str]]])

slots.asHandle = Slot(uri=UCO_OBSERVABLE.asHandle, name="asHandle", curie=UCO_OBSERVABLE.curie('asHandle'),
                   model_uri=UCO_LINKML.asHandle, domain=None, range=Optional[str])

slots.aslrEnabled = Slot(uri=UCO_OBSERVABLE.aslrEnabled, name="aslrEnabled", curie=UCO_OBSERVABLE.curie('aslrEnabled'),
                   model_uri=UCO_LINKML.aslrEnabled, domain=None, range=Optional[Union[bool, Bool]])

slots.attendant = Slot(uri=UCO_OBSERVABLE.attendant, name="attendant", curie=UCO_OBSERVABLE.curie('attendant'),
                   model_uri=UCO_LINKML.attendant, domain=None, range=Optional[Union[Union[str, IdentityId], list[Union[str, IdentityId]]]])

slots.audioType = Slot(uri=UCO_OBSERVABLE.audioType, name="audioType", curie=UCO_OBSERVABLE.curie('audioType'),
                   model_uri=UCO_LINKML.audioType, domain=None, range=Optional[str])

slots.authorityKeyIdentifier = Slot(uri=UCO_OBSERVABLE.authorityKeyIdentifier, name="authorityKeyIdentifier", curie=UCO_OBSERVABLE.curie('authorityKeyIdentifier'),
                   model_uri=UCO_LINKML.authorityKeyIdentifier, domain=None, range=Optional[str])

slots.availableRam = Slot(uri=UCO_OBSERVABLE.availableRam, name="availableRam", curie=UCO_OBSERVABLE.curie('availableRam'),
                   model_uri=UCO_LINKML.availableRam, domain=None, range=Optional[int])

slots.azimuth = Slot(uri=UCO_OBSERVABLE.azimuth, name="azimuth", curie=UCO_OBSERVABLE.curie('azimuth'),
                   model_uri=UCO_LINKML.azimuth, domain=None, range=Optional[Decimal])

slots.baseOfCode = Slot(uri=UCO_OBSERVABLE.baseOfCode, name="baseOfCode", curie=UCO_OBSERVABLE.curie('baseOfCode'),
                   model_uri=UCO_LINKML.baseOfCode, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.baseStation = Slot(uri=UCO_OBSERVABLE.baseStation, name="baseStation", curie=UCO_OBSERVABLE.curie('baseStation'),
                   model_uri=UCO_LINKML.baseStation, domain=None, range=Optional[str])

slots.basicConstraints = Slot(uri=UCO_OBSERVABLE.basicConstraints, name="basicConstraints", curie=UCO_OBSERVABLE.curie('basicConstraints'),
                   model_uri=UCO_LINKML.basicConstraints, domain=None, range=Optional[str])

slots.bcc = Slot(uri=UCO_OBSERVABLE.bcc, name="bcc", curie=UCO_OBSERVABLE.curie('bcc'),
                   model_uri=UCO_LINKML.bcc, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.binary = Slot(uri=UCO_OBSERVABLE.binary, name="binary", curie=UCO_OBSERVABLE.curie('binary'),
                   model_uri=UCO_LINKML.binary, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.biosDate = Slot(uri=UCO_OBSERVABLE.biosDate, name="biosDate", curie=UCO_OBSERVABLE.curie('biosDate'),
                   model_uri=UCO_LINKML.biosDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.biosManufacturer = Slot(uri=UCO_OBSERVABLE.biosManufacturer, name="biosManufacturer", curie=UCO_OBSERVABLE.curie('biosManufacturer'),
                   model_uri=UCO_LINKML.biosManufacturer, domain=None, range=Optional[str])

slots.biosReleaseDate = Slot(uri=UCO_OBSERVABLE.biosReleaseDate, name="biosReleaseDate", curie=UCO_OBSERVABLE.curie('biosReleaseDate'),
                   model_uri=UCO_LINKML.biosReleaseDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.biosSerialNumber = Slot(uri=UCO_OBSERVABLE.biosSerialNumber, name="biosSerialNumber", curie=UCO_OBSERVABLE.curie('biosSerialNumber'),
                   model_uri=UCO_LINKML.biosSerialNumber, domain=None, range=Optional[str])

slots.biosVersion = Slot(uri=UCO_OBSERVABLE.biosVersion, name="biosVersion", curie=UCO_OBSERVABLE.curie('biosVersion'),
                   model_uri=UCO_LINKML.biosVersion, domain=None, range=Optional[str])

slots.bitRate = Slot(uri=UCO_OBSERVABLE.bitRate, name="bitRate", curie=UCO_OBSERVABLE.curie('bitRate'),
                   model_uri=UCO_LINKML.bitRate, domain=None, range=Optional[int])

slots.bitness = Slot(uri=UCO_OBSERVABLE.bitness, name="bitness", curie=UCO_OBSERVABLE.curie('bitness'),
                   model_uri=UCO_LINKML.bitness, domain=None, range=Optional[str])

slots.bitsPerPixel = Slot(uri=UCO_OBSERVABLE.bitsPerPixel, name="bitsPerPixel", curie=UCO_OBSERVABLE.curie('bitsPerPixel'),
                   model_uri=UCO_LINKML.bitsPerPixel, domain=None, range=Optional[int])

slots.blockType = Slot(uri=UCO_OBSERVABLE.blockType, name="blockType", curie=UCO_OBSERVABLE.curie('blockType'),
                   model_uri=UCO_LINKML.blockType, domain=None, range=Optional[Union[str, "MemoryBlockTypeVocab"]])

slots.bluetoothDeviceName = Slot(uri=UCO_OBSERVABLE.bluetoothDeviceName, name="bluetoothDeviceName", curie=UCO_OBSERVABLE.curie('bluetoothDeviceName'),
                   model_uri=UCO_LINKML.bluetoothDeviceName, domain=None, range=Optional[str])

slots.body = Slot(uri=UCO_OBSERVABLE.body, name="body", curie=UCO_OBSERVABLE.curie('body'),
                   model_uri=UCO_LINKML.body, domain=None, range=Optional[str])

slots.bodyMultipart = Slot(uri=UCO_OBSERVABLE.bodyMultipart, name="bodyMultipart", curie=UCO_OBSERVABLE.curie('bodyMultipart'),
                   model_uri=UCO_LINKML.bodyMultipart, domain=None, range=Optional[Union[Union[dict, MimePartType], list[Union[dict, MimePartType]]]])

slots.bodyRaw = Slot(uri=UCO_OBSERVABLE.bodyRaw, name="bodyRaw", curie=UCO_OBSERVABLE.curie('bodyRaw'),
                   model_uri=UCO_LINKML.bodyRaw, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.bookmarkPath = Slot(uri=UCO_OBSERVABLE.bookmarkPath, name="bookmarkPath", curie=UCO_OBSERVABLE.curie('bookmarkPath'),
                   model_uri=UCO_LINKML.bookmarkPath, domain=None, range=Optional[str])

slots.browserInformation = Slot(uri=UCO_OBSERVABLE.browserInformation, name="browserInformation", curie=UCO_OBSERVABLE.curie('browserInformation'),
                   model_uri=UCO_LINKML.browserInformation, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.browserUserProfile = Slot(uri=UCO_OBSERVABLE.browserUserProfile, name="browserUserProfile", curie=UCO_OBSERVABLE.curie('browserUserProfile'),
                   model_uri=UCO_LINKML.browserUserProfile, domain=None, range=Optional[str])

slots.byteOrder = Slot(uri=UCO_OBSERVABLE.byteOrder, name="byteOrder", curie=UCO_OBSERVABLE.curie('byteOrder'),
                   model_uri=UCO_LINKML.byteOrder, domain=None, range=Optional[Union[str, "EndiannessTypeVocab"]])

slots.byteStringValue = Slot(uri=UCO_OBSERVABLE.byteStringValue, name="byteStringValue", curie=UCO_OBSERVABLE.curie('byteStringValue'),
                   model_uri=UCO_LINKML.byteStringValue, domain=None, range=Optional[Union[str, UcoBase64Binary]])

slots.callType = Slot(uri=UCO_OBSERVABLE.callType, name="callType", curie=UCO_OBSERVABLE.curie('callType'),
                   model_uri=UCO_LINKML.callType, domain=None, range=Optional[str])

slots.camera = Slot(uri=UCO_OBSERVABLE.camera, name="camera", curie=UCO_OBSERVABLE.curie('camera'),
                   model_uri=UCO_LINKML.camera, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.canEscalatePrivs = Slot(uri=UCO_OBSERVABLE.canEscalatePrivs, name="canEscalatePrivs", curie=UCO_OBSERVABLE.curie('canEscalatePrivs'),
                   model_uri=UCO_LINKML.canEscalatePrivs, domain=None, range=Optional[Union[bool, Bool]])

slots.captureCellSite = Slot(uri=UCO_OBSERVABLE.captureCellSite, name="captureCellSite", curie=UCO_OBSERVABLE.curie('captureCellSite'),
                   model_uri=UCO_LINKML.captureCellSite, domain=None, range=Union[str, CellSiteId])

slots.carrier = Slot(uri=UCO_OBSERVABLE.carrier, name="carrier", curie=UCO_OBSERVABLE.curie('carrier'),
                   model_uri=UCO_LINKML.carrier, domain=None, range=Optional[Union[str, IdentityId]])

slots.categories = Slot(uri=UCO_OBSERVABLE.categories, name="categories", curie=UCO_OBSERVABLE.curie('categories'),
                   model_uri=UCO_LINKML.categories, domain=None, range=Optional[Union[str, list[str]]])

slots.cc = Slot(uri=UCO_OBSERVABLE.cc, name="cc", curie=UCO_OBSERVABLE.curie('cc'),
                   model_uri=UCO_LINKML.cc, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.cellSiteCountryCode = Slot(uri=UCO_OBSERVABLE.cellSiteCountryCode, name="cellSiteCountryCode", curie=UCO_OBSERVABLE.curie('cellSiteCountryCode'),
                   model_uri=UCO_LINKML.cellSiteCountryCode, domain=None, range=Optional[str])

slots.cellSiteIdentifier = Slot(uri=UCO_OBSERVABLE.cellSiteIdentifier, name="cellSiteIdentifier", curie=UCO_OBSERVABLE.curie('cellSiteIdentifier'),
                   model_uri=UCO_LINKML.cellSiteIdentifier, domain=None, range=Optional[str])

slots.cellSiteLocationAreaCode = Slot(uri=UCO_OBSERVABLE.cellSiteLocationAreaCode, name="cellSiteLocationAreaCode", curie=UCO_OBSERVABLE.curie('cellSiteLocationAreaCode'),
                   model_uri=UCO_LINKML.cellSiteLocationAreaCode, domain=None, range=Optional[str])

slots.cellSiteNetworkCode = Slot(uri=UCO_OBSERVABLE.cellSiteNetworkCode, name="cellSiteNetworkCode", curie=UCO_OBSERVABLE.curie('cellSiteNetworkCode'),
                   model_uri=UCO_LINKML.cellSiteNetworkCode, domain=None, range=Optional[str])

slots.cellSiteType = Slot(uri=UCO_OBSERVABLE.cellSiteType, name="cellSiteType", curie=UCO_OBSERVABLE.curie('cellSiteType'),
                   model_uri=UCO_LINKML.cellSiteType, domain=None, range=Optional[str])

slots.certificateIssuer = Slot(uri=UCO_OBSERVABLE.certificateIssuer, name="certificateIssuer", curie=UCO_OBSERVABLE.curie('certificateIssuer'),
                   model_uri=UCO_LINKML.certificateIssuer, domain=None, range=Optional[Union[str, IdentityId]])

slots.certificatePolicies = Slot(uri=UCO_OBSERVABLE.certificatePolicies, name="certificatePolicies", curie=UCO_OBSERVABLE.curie('certificatePolicies'),
                   model_uri=UCO_LINKML.certificatePolicies, domain=None, range=Optional[str])

slots.certificateSubject = Slot(uri=UCO_OBSERVABLE.certificateSubject, name="certificateSubject", curie=UCO_OBSERVABLE.curie('certificateSubject'),
                   model_uri=UCO_LINKML.certificateSubject, domain=None, range=Optional[Union[str, UcoObjectId]])

slots.characteristics = Slot(uri=UCO_OBSERVABLE.characteristics, name="characteristics", curie=UCO_OBSERVABLE.curie('characteristics'),
                   model_uri=UCO_LINKML.characteristics, domain=None, range=Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]])

slots.checksum = Slot(uri=UCO_OBSERVABLE.checksum, name="checksum", curie=UCO_OBSERVABLE.curie('checksum'),
                   model_uri=UCO_LINKML.checksum, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.clockSetting = Slot(uri=UCO_OBSERVABLE.clockSetting, name="clockSetting", curie=UCO_OBSERVABLE.curie('clockSetting'),
                   model_uri=UCO_LINKML.clockSetting, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.clusterSize = Slot(uri=UCO_OBSERVABLE.clusterSize, name="clusterSize", curie=UCO_OBSERVABLE.curie('clusterSize'),
                   model_uri=UCO_LINKML.clusterSize, domain=None, range=Optional[int])

slots.columnName = Slot(uri=UCO_OBSERVABLE.columnName, name="columnName", curie=UCO_OBSERVABLE.curie('columnName'),
                   model_uri=UCO_LINKML.columnName, domain=None, range=Optional[str])

slots.comClassID = Slot(uri=UCO_OBSERVABLE.comClassID, name="comClassID", curie=UCO_OBSERVABLE.curie('comClassID'),
                   model_uri=UCO_LINKML.comClassID, domain=None, range=Optional[str])

slots.comData = Slot(uri=UCO_OBSERVABLE.comData, name="comData", curie=UCO_OBSERVABLE.curie('comData'),
                   model_uri=UCO_LINKML.comData, domain=None, range=Optional[str])

slots.comment = Slot(uri=UCO_OBSERVABLE.comment, name="comment", curie=UCO_OBSERVABLE.curie('comment'),
                   model_uri=UCO_LINKML.comment, domain=None, range=Optional[str])

slots.compressionMethod = Slot(uri=UCO_OBSERVABLE.compressionMethod, name="compressionMethod", curie=UCO_OBSERVABLE.curie('compressionMethod'),
                   model_uri=UCO_LINKML.compressionMethod, domain=None, range=Optional[str])

slots.compressionRatio = Slot(uri=UCO_OBSERVABLE.compressionRatio, name="compressionRatio", curie=UCO_OBSERVABLE.curie('compressionRatio'),
                   model_uri=UCO_LINKML.compressionRatio, domain=None, range=Optional[Decimal])

slots.contact = Slot(uri=UCO_OBSERVABLE.contact, name="contact", curie=UCO_OBSERVABLE.curie('contact'),
                   model_uri=UCO_LINKML.contact, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.contactAddress = Slot(uri=UCO_OBSERVABLE.contactAddress, name="contactAddress", curie=UCO_OBSERVABLE.curie('contactAddress'),
                   model_uri=UCO_LINKML.contactAddress, domain=None, range=Optional[Union[dict, ContactAddress]])

slots.contactAddressScope = Slot(uri=UCO_OBSERVABLE.contactAddressScope, name="contactAddressScope", curie=UCO_OBSERVABLE.curie('contactAddressScope'),
                   model_uri=UCO_LINKML.contactAddressScope, domain=None, range=Optional[Union[str, "ContactAddressScopeVocab"]])

slots.contactAffiliation = Slot(uri=UCO_OBSERVABLE.contactAffiliation, name="contactAffiliation", curie=UCO_OBSERVABLE.curie('contactAffiliation'),
                   model_uri=UCO_LINKML.contactAffiliation, domain=None, range=Optional[Union[Union[dict, ContactAffiliation], list[Union[dict, ContactAffiliation]]]])

slots.contactEmail = Slot(uri=UCO_OBSERVABLE.contactEmail, name="contactEmail", curie=UCO_OBSERVABLE.curie('contactEmail'),
                   model_uri=UCO_LINKML.contactEmail, domain=None, range=Optional[Union[dict, ContactEmail]])

slots.contactEmailScope = Slot(uri=UCO_OBSERVABLE.contactEmailScope, name="contactEmailScope", curie=UCO_OBSERVABLE.curie('contactEmailScope'),
                   model_uri=UCO_LINKML.contactEmailScope, domain=None, range=Optional[Union[str, "ContactEmailScopeVocab"]])

slots.contactGroup = Slot(uri=UCO_OBSERVABLE.contactGroup, name="contactGroup", curie=UCO_OBSERVABLE.curie('contactGroup'),
                   model_uri=UCO_LINKML.contactGroup, domain=None, range=Optional[Union[str, list[str]]])

slots.contactID = Slot(uri=UCO_OBSERVABLE.contactID, name="contactID", curie=UCO_OBSERVABLE.curie('contactID'),
                   model_uri=UCO_LINKML.contactID, domain=None, range=Optional[str])

slots.contactMessaging = Slot(uri=UCO_OBSERVABLE.contactMessaging, name="contactMessaging", curie=UCO_OBSERVABLE.curie('contactMessaging'),
                   model_uri=UCO_LINKML.contactMessaging, domain=None, range=Optional[Union[dict, ContactMessaging]])

slots.contactMessagingPlatform = Slot(uri=UCO_OBSERVABLE.contactMessagingPlatform, name="contactMessagingPlatform", curie=UCO_OBSERVABLE.curie('contactMessagingPlatform'),
                   model_uri=UCO_LINKML.contactMessagingPlatform, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.contactNote = Slot(uri=UCO_OBSERVABLE.contactNote, name="contactNote", curie=UCO_OBSERVABLE.curie('contactNote'),
                   model_uri=UCO_LINKML.contactNote, domain=None, range=Optional[Union[str, list[str]]])

slots.contactOrganization = Slot(uri=UCO_OBSERVABLE.contactOrganization, name="contactOrganization", curie=UCO_OBSERVABLE.curie('contactOrganization'),
                   model_uri=UCO_LINKML.contactOrganization, domain=None, range=Optional[Union[str, OrganizationId]])

slots.contactPhone = Slot(uri=UCO_OBSERVABLE.contactPhone, name="contactPhone", curie=UCO_OBSERVABLE.curie('contactPhone'),
                   model_uri=UCO_LINKML.contactPhone, domain=None, range=Optional[Union[dict, ContactPhone]])

slots.contactPhoneNumber = Slot(uri=UCO_OBSERVABLE.contactPhoneNumber, name="contactPhoneNumber", curie=UCO_OBSERVABLE.curie('contactPhoneNumber'),
                   model_uri=UCO_LINKML.contactPhoneNumber, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.contactPhoneScope = Slot(uri=UCO_OBSERVABLE.contactPhoneScope, name="contactPhoneScope", curie=UCO_OBSERVABLE.curie('contactPhoneScope'),
                   model_uri=UCO_LINKML.contactPhoneScope, domain=None, range=Optional[Union[str, "ContactPhoneScopeVocab"]])

slots.contactProfile = Slot(uri=UCO_OBSERVABLE.contactProfile, name="contactProfile", curie=UCO_OBSERVABLE.curie('contactProfile'),
                   model_uri=UCO_LINKML.contactProfile, domain=None, range=Optional[Union[Union[dict, ContactProfile], list[Union[dict, ContactProfile]]]])

slots.contactProfilePlatform = Slot(uri=UCO_OBSERVABLE.contactProfilePlatform, name="contactProfilePlatform", curie=UCO_OBSERVABLE.curie('contactProfilePlatform'),
                   model_uri=UCO_LINKML.contactProfilePlatform, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.contactSIP = Slot(uri=UCO_OBSERVABLE.contactSIP, name="contactSIP", curie=UCO_OBSERVABLE.curie('contactSIP'),
                   model_uri=UCO_LINKML.contactSIP, domain=None, range=Optional[Union[Union[dict, ContactSIP], list[Union[dict, ContactSIP]]]])

slots.contactSIPScope = Slot(uri=UCO_OBSERVABLE.contactSIPScope, name="contactSIPScope", curie=UCO_OBSERVABLE.curie('contactSIPScope'),
                   model_uri=UCO_LINKML.contactSIPScope, domain=None, range=Optional[Union[str, "ContactSIPScopeVocab"]])

slots.contactURL = Slot(uri=UCO_OBSERVABLE.contactURL, name="contactURL", curie=UCO_OBSERVABLE.curie('contactURL'),
                   model_uri=UCO_LINKML.contactURL, domain=None, range=Optional[Union[dict, ContactURL]])

slots.contactURLScope = Slot(uri=UCO_OBSERVABLE.contactURLScope, name="contactURLScope", curie=UCO_OBSERVABLE.curie('contactURLScope'),
                   model_uri=UCO_LINKML.contactURLScope, domain=None, range=Optional[Union[str, "ContactURLScopeVocab"]])

slots.contentDisposition = Slot(uri=UCO_OBSERVABLE.contentDisposition, name="contentDisposition", curie=UCO_OBSERVABLE.curie('contentDisposition'),
                   model_uri=UCO_LINKML.contentDisposition, domain=None, range=Optional[str])

slots.contentRecoveredStatus = Slot(uri=UCO_OBSERVABLE.contentRecoveredStatus, name="contentRecoveredStatus", curie=UCO_OBSERVABLE.curie('contentRecoveredStatus'),
                   model_uri=UCO_LINKML.contentRecoveredStatus, domain=None, range=Optional[Union[str, "RecoveredObjectStatusVocab"]])

slots.contentType = Slot(uri=UCO_OBSERVABLE.contentType, name="contentType", curie=UCO_OBSERVABLE.curie('contentType'),
                   model_uri=UCO_LINKML.contentType, domain=None, range=Optional[str])

slots.controlCode = Slot(uri=UCO_OBSERVABLE.controlCode, name="controlCode", curie=UCO_OBSERVABLE.curie('controlCode'),
                   model_uri=UCO_LINKML.controlCode, domain=None, range=Optional[str])

slots.cookieDomain = Slot(uri=UCO_OBSERVABLE.cookieDomain, name="cookieDomain", curie=UCO_OBSERVABLE.curie('cookieDomain'),
                   model_uri=UCO_LINKML.cookieDomain, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.cookieName = Slot(uri=UCO_OBSERVABLE.cookieName, name="cookieName", curie=UCO_OBSERVABLE.curie('cookieName'),
                   model_uri=UCO_LINKML.cookieName, domain=None, range=Optional[str])

slots.cookiePath = Slot(uri=UCO_OBSERVABLE.cookiePath, name="cookiePath", curie=UCO_OBSERVABLE.curie('cookiePath'),
                   model_uri=UCO_LINKML.cookiePath, domain=None, range=Optional[str])

slots.cpu = Slot(uri=UCO_OBSERVABLE.cpu, name="cpu", curie=UCO_OBSERVABLE.curie('cpu'),
                   model_uri=UCO_LINKML.cpu, domain=None, range=Optional[str])

slots.cpuFamily = Slot(uri=UCO_OBSERVABLE.cpuFamily, name="cpuFamily", curie=UCO_OBSERVABLE.curie('cpuFamily'),
                   model_uri=UCO_LINKML.cpuFamily, domain=None, range=Optional[str])

slots.creationDate = Slot(uri=UCO_OBSERVABLE.creationDate, name="creationDate", curie=UCO_OBSERVABLE.curie('creationDate'),
                   model_uri=UCO_LINKML.creationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.creationFlags = Slot(uri=UCO_OBSERVABLE.creationFlags, name="creationFlags", curie=UCO_OBSERVABLE.curie('creationFlags'),
                   model_uri=UCO_LINKML.creationFlags, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.creationTime = Slot(uri=UCO_OBSERVABLE.creationTime, name="creationTime", curie=UCO_OBSERVABLE.curie('creationTime'),
                   model_uri=UCO_LINKML.creationTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.creatorUser = Slot(uri=UCO_OBSERVABLE.creatorUser, name="creatorUser", curie=UCO_OBSERVABLE.curie('creatorUser'),
                   model_uri=UCO_LINKML.creatorUser, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.crlDistributionPoints = Slot(uri=UCO_OBSERVABLE.crlDistributionPoints, name="crlDistributionPoints", curie=UCO_OBSERVABLE.curie('crlDistributionPoints'),
                   model_uri=UCO_LINKML.crlDistributionPoints, domain=None, range=Optional[str])

slots.currentSystemDate = Slot(uri=UCO_OBSERVABLE.currentSystemDate, name="currentSystemDate", curie=UCO_OBSERVABLE.curie('currentSystemDate'),
                   model_uri=UCO_LINKML.currentSystemDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.currentWorkingDirectory = Slot(uri=UCO_OBSERVABLE.currentWorkingDirectory, name="currentWorkingDirectory", curie=UCO_OBSERVABLE.curie('currentWorkingDirectory'),
                   model_uri=UCO_LINKML.currentWorkingDirectory, domain=None, range=Optional[str])

slots.cyberAction = Slot(uri=UCO_OBSERVABLE.cyberAction, name="cyberAction", curie=UCO_OBSERVABLE.curie('cyberAction'),
                   model_uri=UCO_LINKML.cyberAction, domain=None, range=Optional[Union[str, ObservableActionId]])

slots.data = Slot(uri=UCO_OBSERVABLE.data, name="data", curie=UCO_OBSERVABLE.curie('data'),
                   model_uri=UCO_LINKML.data, domain=None, range=Optional[str])

slots.dataPayload = Slot(uri=UCO_OBSERVABLE.dataPayload, name="dataPayload", curie=UCO_OBSERVABLE.curie('dataPayload'),
                   model_uri=UCO_LINKML.dataPayload, domain=None, range=Optional[str])

slots.dataPayloadReferenceURL = Slot(uri=UCO_OBSERVABLE.dataPayloadReferenceURL, name="dataPayloadReferenceURL", curie=UCO_OBSERVABLE.curie('dataPayloadReferenceURL'),
                   model_uri=UCO_LINKML.dataPayloadReferenceURL, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.dataType = Slot(uri=UCO_OBSERVABLE.dataType, name="dataType", curie=UCO_OBSERVABLE.curie('dataType'),
                   model_uri=UCO_LINKML.dataType, domain=None, range=Optional[str])

slots.depEnabled = Slot(uri=UCO_OBSERVABLE.depEnabled, name="depEnabled", curie=UCO_OBSERVABLE.curie('depEnabled'),
                   model_uri=UCO_LINKML.depEnabled, domain=None, range=Optional[Union[bool, Bool]])

slots.descriptions = Slot(uri=UCO_OBSERVABLE.descriptions, name="descriptions", curie=UCO_OBSERVABLE.curie('descriptions'),
                   model_uri=UCO_LINKML.descriptions, domain=None, range=Optional[Union[str, list[str]]])

slots.destination = Slot(uri=UCO_OBSERVABLE.destination, name="destination", curie=UCO_OBSERVABLE.curie('destination'),
                   model_uri=UCO_LINKML.destination, domain=None, range=Optional[str])

slots.destinationFlags = Slot(uri=UCO_OBSERVABLE.destinationFlags, name="destinationFlags", curie=UCO_OBSERVABLE.curie('destinationFlags'),
                   model_uri=UCO_LINKML.destinationFlags, domain=None, range=Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]])

slots.destinationPort = Slot(uri=UCO_OBSERVABLE.destinationPort, name="destinationPort", curie=UCO_OBSERVABLE.curie('destinationPort'),
                   model_uri=UCO_LINKML.destinationPort, domain=None, range=Optional[int])

slots.deviceType = Slot(uri=UCO_OBSERVABLE.deviceType, name="deviceType", curie=UCO_OBSERVABLE.curie('deviceType'),
                   model_uri=UCO_LINKML.deviceType, domain=None, range=Optional[str])

slots.dhcpLeaseExpires = Slot(uri=UCO_OBSERVABLE.dhcpLeaseExpires, name="dhcpLeaseExpires", curie=UCO_OBSERVABLE.curie('dhcpLeaseExpires'),
                   model_uri=UCO_LINKML.dhcpLeaseExpires, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dhcpLeaseObtained = Slot(uri=UCO_OBSERVABLE.dhcpLeaseObtained, name="dhcpLeaseObtained", curie=UCO_OBSERVABLE.curie('dhcpLeaseObtained'),
                   model_uri=UCO_LINKML.dhcpLeaseObtained, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dhcpServer = Slot(uri=UCO_OBSERVABLE.dhcpServer, name="dhcpServer", curie=UCO_OBSERVABLE.curie('dhcpServer'),
                   model_uri=UCO_LINKML.dhcpServer, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.diskPartitionType = Slot(uri=UCO_OBSERVABLE.diskPartitionType, name="diskPartitionType", curie=UCO_OBSERVABLE.curie('diskPartitionType'),
                   model_uri=UCO_LINKML.diskPartitionType, domain=None, range=Optional[str])

slots.diskSize = Slot(uri=UCO_OBSERVABLE.diskSize, name="diskSize", curie=UCO_OBSERVABLE.curie('diskSize'),
                   model_uri=UCO_LINKML.diskSize, domain=None, range=Optional[int])

slots.diskType = Slot(uri=UCO_OBSERVABLE.diskType, name="diskType", curie=UCO_OBSERVABLE.curie('diskType'),
                   model_uri=UCO_LINKML.diskType, domain=None, range=Optional[str])

slots.displayName = Slot(uri=UCO_OBSERVABLE.displayName, name="displayName", curie=UCO_OBSERVABLE.curie('displayName'),
                   model_uri=UCO_LINKML.displayName, domain=None, range=Optional[str])

slots.dllCharacteristics = Slot(uri=UCO_OBSERVABLE.dllCharacteristics, name="dllCharacteristics", curie=UCO_OBSERVABLE.curie('dllCharacteristics'),
                   model_uri=UCO_LINKML.dllCharacteristics, domain=None, range=Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]])

slots.dnssec = Slot(uri=UCO_OBSERVABLE.dnssec, name="dnssec", curie=UCO_OBSERVABLE.curie('dnssec'),
                   model_uri=UCO_LINKML.dnssec, domain=None, range=Optional[Union[str, "WhoisDNSSECTypeVocab"]])

slots.documentInformationDictionary = Slot(uri=UCO_OBSERVABLE.documentInformationDictionary, name="documentInformationDictionary", curie=UCO_OBSERVABLE.curie('documentInformationDictionary'),
                   model_uri=UCO_LINKML.documentInformationDictionary, domain=None, range=Optional[Union[dict, ControlledDictionary]])

slots.domain = Slot(uri=UCO_OBSERVABLE.domain, name="domain", curie=UCO_OBSERVABLE.curie('domain'),
                   model_uri=UCO_LINKML.domain, domain=None, range=Optional[Union[str, list[str]]])

slots.domainID = Slot(uri=UCO_OBSERVABLE.domainID, name="domainID", curie=UCO_OBSERVABLE.curie('domainID'),
                   model_uri=UCO_LINKML.domainID, domain=None, range=Optional[str])

slots.domainName = Slot(uri=UCO_OBSERVABLE.domainName, name="domainName", curie=UCO_OBSERVABLE.curie('domainName'),
                   model_uri=UCO_LINKML.domainName, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.driveLetter = Slot(uri=UCO_OBSERVABLE.driveLetter, name="driveLetter", curie=UCO_OBSERVABLE.curie('driveLetter'),
                   model_uri=UCO_LINKML.driveLetter, domain=None, range=Optional[str])

slots.driveType = Slot(uri=UCO_OBSERVABLE.driveType, name="driveType", curie=UCO_OBSERVABLE.curie('driveType'),
                   model_uri=UCO_LINKML.driveType, domain=None, range=Optional[Union[str, "WindowsDriveTypeVocab"]])

slots.dst = Slot(uri=UCO_OBSERVABLE.dst, name="dst", curie=UCO_OBSERVABLE.curie('dst'),
                   model_uri=UCO_LINKML.dst, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.dstBytes = Slot(uri=UCO_OBSERVABLE.dstBytes, name="dstBytes", curie=UCO_OBSERVABLE.curie('dstBytes'),
                   model_uri=UCO_LINKML.dstBytes, domain=None, range=Optional[int])

slots.dstPackets = Slot(uri=UCO_OBSERVABLE.dstPackets, name="dstPackets", curie=UCO_OBSERVABLE.curie('dstPackets'),
                   model_uri=UCO_LINKML.dstPackets, domain=None, range=Optional[int])

slots.dstPayload = Slot(uri=UCO_OBSERVABLE.dstPayload, name="dstPayload", curie=UCO_OBSERVABLE.curie('dstPayload'),
                   model_uri=UCO_LINKML.dstPayload, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.duration = Slot(uri=UCO_OBSERVABLE.duration, name="duration", curie=UCO_OBSERVABLE.curie('duration'),
                   model_uri=UCO_LINKML.duration, domain=None, range=Optional[int])

slots.effectiveGroup = Slot(uri=UCO_OBSERVABLE.effectiveGroup, name="effectiveGroup", curie=UCO_OBSERVABLE.curie('effectiveGroup'),
                   model_uri=UCO_LINKML.effectiveGroup, domain=None, range=Optional[str])

slots.effectiveGroupID = Slot(uri=UCO_OBSERVABLE.effectiveGroupID, name="effectiveGroupID", curie=UCO_OBSERVABLE.curie('effectiveGroupID'),
                   model_uri=UCO_LINKML.effectiveGroupID, domain=None, range=Optional[str])

slots.effectiveUser = Slot(uri=UCO_OBSERVABLE.effectiveUser, name="effectiveUser", curie=UCO_OBSERVABLE.curie('effectiveUser'),
                   model_uri=UCO_LINKML.effectiveUser, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.elevation = Slot(uri=UCO_OBSERVABLE.elevation, name="elevation", curie=UCO_OBSERVABLE.curie('elevation'),
                   model_uri=UCO_LINKML.elevation, domain=None, range=Optional[Decimal])

slots.emailAddress = Slot(uri=UCO_OBSERVABLE.emailAddress, name="emailAddress", curie=UCO_OBSERVABLE.curie('emailAddress'),
                   model_uri=UCO_LINKML.emailAddress, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.encoding = Slot(uri=UCO_OBSERVABLE.encoding, name="encoding", curie=UCO_OBSERVABLE.curie('encoding'),
                   model_uri=UCO_LINKML.encoding, domain=None, range=Optional[str])

slots.encodingMethod = Slot(uri=UCO_OBSERVABLE.encodingMethod, name="encodingMethod", curie=UCO_OBSERVABLE.curie('encodingMethod'),
                   model_uri=UCO_LINKML.encodingMethod, domain=None, range=Optional[str])

slots.encryptionIV = Slot(uri=UCO_OBSERVABLE.encryptionIV, name="encryptionIV", curie=UCO_OBSERVABLE.curie('encryptionIV'),
                   model_uri=UCO_LINKML.encryptionIV, domain=None, range=Optional[Union[str, list[str]]])

slots.encryptionKey = Slot(uri=UCO_OBSERVABLE.encryptionKey, name="encryptionKey", curie=UCO_OBSERVABLE.curie('encryptionKey'),
                   model_uri=UCO_LINKML.encryptionKey, domain=None, range=Optional[Union[str, list[str]]])

slots.encryptionMethod = Slot(uri=UCO_OBSERVABLE.encryptionMethod, name="encryptionMethod", curie=UCO_OBSERVABLE.curie('encryptionMethod'),
                   model_uri=UCO_LINKML.encryptionMethod, domain=None, range=Optional[str])

slots.encryptionMode = Slot(uri=UCO_OBSERVABLE.encryptionMode, name="encryptionMode", curie=UCO_OBSERVABLE.curie('encryptionMode'),
                   model_uri=UCO_LINKML.encryptionMode, domain=None, range=Optional[str])

slots.englishTranslation = Slot(uri=UCO_OBSERVABLE.englishTranslation, name="englishTranslation", curie=UCO_OBSERVABLE.curie('englishTranslation'),
                   model_uri=UCO_LINKML.englishTranslation, domain=None, range=Optional[str])

slots.entropy = Slot(uri=UCO_OBSERVABLE.entropy, name="entropy", curie=UCO_OBSERVABLE.curie('entropy'),
                   model_uri=UCO_LINKML.entropy, domain=None, range=Optional[Decimal])

slots.entryID = Slot(uri=UCO_OBSERVABLE.entryID, name="entryID", curie=UCO_OBSERVABLE.curie('entryID'),
                   model_uri=UCO_LINKML.entryID, domain=None, range=Optional[int])

slots.environmentVariables = Slot(uri=UCO_OBSERVABLE.environmentVariables, name="environmentVariables", curie=UCO_OBSERVABLE.curie('environmentVariables'),
                   model_uri=UCO_LINKML.environmentVariables, domain=None, range=Optional[Union[dict, Dictionary]])

slots.eventID = Slot(uri=UCO_OBSERVABLE.eventID, name="eventID", curie=UCO_OBSERVABLE.curie('eventID'),
                   model_uri=UCO_LINKML.eventID, domain=None, range=Optional[str])

slots.eventRecordDevice = Slot(uri=UCO_OBSERVABLE.eventRecordDevice, name="eventRecordDevice", curie=UCO_OBSERVABLE.curie('eventRecordDevice'),
                   model_uri=UCO_LINKML.eventRecordDevice, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.eventRecordID = Slot(uri=UCO_OBSERVABLE.eventRecordID, name="eventRecordID", curie=UCO_OBSERVABLE.curie('eventRecordID'),
                   model_uri=UCO_LINKML.eventRecordID, domain=None, range=Optional[str])

slots.eventRecordRaw = Slot(uri=UCO_OBSERVABLE.eventRecordRaw, name="eventRecordRaw", curie=UCO_OBSERVABLE.curie('eventRecordRaw'),
                   model_uri=UCO_LINKML.eventRecordRaw, domain=None, range=Optional[str])

slots.eventRecordServiceName = Slot(uri=UCO_OBSERVABLE.eventRecordServiceName, name="eventRecordServiceName", curie=UCO_OBSERVABLE.curie('eventRecordServiceName'),
                   model_uri=UCO_LINKML.eventRecordServiceName, domain=None, range=Optional[str])

slots.eventRecordText = Slot(uri=UCO_OBSERVABLE.eventRecordText, name="eventRecordText", curie=UCO_OBSERVABLE.curie('eventRecordText'),
                   model_uri=UCO_LINKML.eventRecordText, domain=None, range=Optional[str])

slots.eventStatus = Slot(uri=UCO_OBSERVABLE.eventStatus, name="eventStatus", curie=UCO_OBSERVABLE.curie('eventStatus'),
                   model_uri=UCO_LINKML.eventStatus, domain=None, range=Optional[str])

slots.execArguments = Slot(uri=UCO_OBSERVABLE.execArguments, name="execArguments", curie=UCO_OBSERVABLE.curie('execArguments'),
                   model_uri=UCO_LINKML.execArguments, domain=None, range=Optional[str])

slots.execProgramHashes = Slot(uri=UCO_OBSERVABLE.execProgramHashes, name="execProgramHashes", curie=UCO_OBSERVABLE.curie('execProgramHashes'),
                   model_uri=UCO_LINKML.execProgramHashes, domain=None, range=Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]])

slots.execProgramPath = Slot(uri=UCO_OBSERVABLE.execProgramPath, name="execProgramPath", curie=UCO_OBSERVABLE.curie('execProgramPath'),
                   model_uri=UCO_LINKML.execProgramPath, domain=None, range=Optional[str])

slots.execWorkingDirectory = Slot(uri=UCO_OBSERVABLE.execWorkingDirectory, name="execWorkingDirectory", curie=UCO_OBSERVABLE.curie('execWorkingDirectory'),
                   model_uri=UCO_LINKML.execWorkingDirectory, domain=None, range=Optional[str])

slots.exifData = Slot(uri=UCO_OBSERVABLE.exifData, name="exifData", curie=UCO_OBSERVABLE.curie('exifData'),
                   model_uri=UCO_LINKML.exifData, domain=None, range=Optional[Union[Union[dict, ControlledDictionary], list[Union[dict, ControlledDictionary]]]])

slots.exitCode = Slot(uri=UCO_OBSERVABLE.exitCode, name="exitCode", curie=UCO_OBSERVABLE.curie('exitCode'),
                   model_uri=UCO_LINKML.exitCode, domain=None, range=Optional[int])

slots.exitStatus = Slot(uri=UCO_OBSERVABLE.exitStatus, name="exitStatus", curie=UCO_OBSERVABLE.curie('exitStatus'),
                   model_uri=UCO_LINKML.exitStatus, domain=None, range=Optional[int])

slots.exitTime = Slot(uri=UCO_OBSERVABLE.exitTime, name="exitTime", curie=UCO_OBSERVABLE.curie('exitTime'),
                   model_uri=UCO_LINKML.exitTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.expirationDate = Slot(uri=UCO_OBSERVABLE.expirationDate, name="expirationDate", curie=UCO_OBSERVABLE.curie('expirationDate'),
                   model_uri=UCO_LINKML.expirationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.expirationTime = Slot(uri=UCO_OBSERVABLE.expirationTime, name="expirationTime", curie=UCO_OBSERVABLE.curie('expirationTime'),
                   model_uri=UCO_LINKML.expirationTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.extDeletionTime = Slot(uri=UCO_OBSERVABLE.extDeletionTime, name="extDeletionTime", curie=UCO_OBSERVABLE.curie('extDeletionTime'),
                   model_uri=UCO_LINKML.extDeletionTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.extFileType = Slot(uri=UCO_OBSERVABLE.extFileType, name="extFileType", curie=UCO_OBSERVABLE.curie('extFileType'),
                   model_uri=UCO_LINKML.extFileType, domain=None, range=Optional[int])

slots.extFlags = Slot(uri=UCO_OBSERVABLE.extFlags, name="extFlags", curie=UCO_OBSERVABLE.curie('extFlags'),
                   model_uri=UCO_LINKML.extFlags, domain=None, range=Optional[int])

slots.extHardLinkCount = Slot(uri=UCO_OBSERVABLE.extHardLinkCount, name="extHardLinkCount", curie=UCO_OBSERVABLE.curie('extHardLinkCount'),
                   model_uri=UCO_LINKML.extHardLinkCount, domain=None, range=Optional[int])

slots.extInodeChangeTime = Slot(uri=UCO_OBSERVABLE.extInodeChangeTime, name="extInodeChangeTime", curie=UCO_OBSERVABLE.curie('extInodeChangeTime'),
                   model_uri=UCO_LINKML.extInodeChangeTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.extInodeID = Slot(uri=UCO_OBSERVABLE.extInodeID, name="extInodeID", curie=UCO_OBSERVABLE.curie('extInodeID'),
                   model_uri=UCO_LINKML.extInodeID, domain=None, range=Optional[int])

slots.extPermissions = Slot(uri=UCO_OBSERVABLE.extPermissions, name="extPermissions", curie=UCO_OBSERVABLE.curie('extPermissions'),
                   model_uri=UCO_LINKML.extPermissions, domain=None, range=Optional[int])

slots.extSGID = Slot(uri=UCO_OBSERVABLE.extSGID, name="extSGID", curie=UCO_OBSERVABLE.curie('extSGID'),
                   model_uri=UCO_LINKML.extSGID, domain=None, range=Optional[int])

slots.extSUID = Slot(uri=UCO_OBSERVABLE.extSUID, name="extSUID", curie=UCO_OBSERVABLE.curie('extSUID'),
                   model_uri=UCO_LINKML.extSUID, domain=None, range=Optional[int])

slots.extendedKeyUsage = Slot(uri=UCO_OBSERVABLE.extendedKeyUsage, name="extendedKeyUsage", curie=UCO_OBSERVABLE.curie('extendedKeyUsage'),
                   model_uri=UCO_LINKML.extendedKeyUsage, domain=None, range=Optional[str])

slots.extension = Slot(uri=UCO_OBSERVABLE.extension, name="extension", curie=UCO_OBSERVABLE.curie('extension'),
                   model_uri=UCO_LINKML.extension, domain=None, range=Optional[str])

slots.favoritesCount = Slot(uri=UCO_OBSERVABLE.favoritesCount, name="favoritesCount", curie=UCO_OBSERVABLE.curie('favoritesCount'),
                   model_uri=UCO_LINKML.favoritesCount, domain=None, range=Optional[Union[int, UcoNonNegativeInteger]])

slots.fileAlignment = Slot(uri=UCO_OBSERVABLE.fileAlignment, name="fileAlignment", curie=UCO_OBSERVABLE.curie('fileAlignment'),
                   model_uri=UCO_LINKML.fileAlignment, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.fileHeaderHashes = Slot(uri=UCO_OBSERVABLE.fileHeaderHashes, name="fileHeaderHashes", curie=UCO_OBSERVABLE.curie('fileHeaderHashes'),
                   model_uri=UCO_LINKML.fileHeaderHashes, domain=None, range=Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]])

slots.fileName = Slot(uri=UCO_OBSERVABLE.fileName, name="fileName", curie=UCO_OBSERVABLE.curie('fileName'),
                   model_uri=UCO_LINKML.fileName, domain=None, range=Optional[Union[str, list[str]]])

slots.filePath = Slot(uri=UCO_OBSERVABLE.filePath, name="filePath", curie=UCO_OBSERVABLE.curie('filePath'),
                   model_uri=UCO_LINKML.filePath, domain=None, range=Optional[Union[str, list[str]]])

slots.fileSystemType = Slot(uri=UCO_OBSERVABLE.fileSystemType, name="fileSystemType", curie=UCO_OBSERVABLE.curie('fileSystemType'),
                   model_uri=UCO_LINKML.fileSystemType, domain=None, range=Optional[str])

slots.firstLoginTime = Slot(uri=UCO_OBSERVABLE.firstLoginTime, name="firstLoginTime", curie=UCO_OBSERVABLE.curie('firstLoginTime'),
                   model_uri=UCO_LINKML.firstLoginTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.firstName = Slot(uri=UCO_OBSERVABLE.firstName, name="firstName", curie=UCO_OBSERVABLE.curie('firstName'),
                   model_uri=UCO_LINKML.firstName, domain=None, range=Optional[str])

slots.firstRun = Slot(uri=UCO_OBSERVABLE.firstRun, name="firstRun", curie=UCO_OBSERVABLE.curie('firstRun'),
                   model_uri=UCO_LINKML.firstRun, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.firstVisit = Slot(uri=UCO_OBSERVABLE.firstVisit, name="firstVisit", curie=UCO_OBSERVABLE.curie('firstVisit'),
                   model_uri=UCO_LINKML.firstVisit, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.flags = Slot(uri=UCO_OBSERVABLE.flags, name="flags", curie=UCO_OBSERVABLE.curie('flags'),
                   model_uri=UCO_LINKML.flags, domain=None, range=Optional[Union[str, list[str]]])

slots.followersCount = Slot(uri=UCO_OBSERVABLE.followersCount, name="followersCount", curie=UCO_OBSERVABLE.curie('followersCount'),
                   model_uri=UCO_LINKML.followersCount, domain=None, range=Optional[Union[int, UcoNonNegativeInteger]])

slots.format = Slot(uri=UCO_OBSERVABLE.format, name="format", curie=UCO_OBSERVABLE.curie('format'),
                   model_uri=UCO_LINKML.format, domain=None, range=Optional[str])

slots.fragment = Slot(uri=UCO_OBSERVABLE.fragment, name="fragment", curie=UCO_OBSERVABLE.curie('fragment'),
                   model_uri=UCO_LINKML.fragment, domain=None, range=Optional[str])

slots.fragmentIndex = Slot(uri=UCO_OBSERVABLE.fragmentIndex, name="fragmentIndex", curie=UCO_OBSERVABLE.curie('fragmentIndex'),
                   model_uri=UCO_LINKML.fragmentIndex, domain=None, range=Optional[Union[int, list[int]]])

slots.freeSpace = Slot(uri=UCO_OBSERVABLE.freeSpace, name="freeSpace", curie=UCO_OBSERVABLE.curie('freeSpace'),
                   model_uri=UCO_LINKML.freeSpace, domain=None, range=Optional[int])

slots.friendsCount = Slot(uri=UCO_OBSERVABLE.friendsCount, name="friendsCount", curie=UCO_OBSERVABLE.curie('friendsCount'),
                   model_uri=UCO_LINKML.friendsCount, domain=None, range=Optional[Union[int, UcoNonNegativeInteger]])

slots.from_ = Slot(uri=UCO_OBSERVABLE['from'], name="from", curie=UCO_OBSERVABLE.curie('from'),
                   model_uri=UCO_LINKML.from_, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.fromURLVisit = Slot(uri=UCO_OBSERVABLE.fromURLVisit, name="fromURLVisit", curie=UCO_OBSERVABLE.curie('fromURLVisit'),
                   model_uri=UCO_LINKML.fromURLVisit, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.fullValue = Slot(uri=UCO_OBSERVABLE.fullValue, name="fullValue", curie=UCO_OBSERVABLE.curie('fullValue'),
                   model_uri=UCO_LINKML.fullValue, domain=None, range=Optional[str])

slots.geoLocationEntry = Slot(uri=UCO_OBSERVABLE.geoLocationEntry, name="geoLocationEntry", curie=UCO_OBSERVABLE.curie('geoLocationEntry'),
                   model_uri=UCO_LINKML.geoLocationEntry, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.geolocationAddress = Slot(uri=UCO_OBSERVABLE.geolocationAddress, name="geolocationAddress", curie=UCO_OBSERVABLE.curie('geolocationAddress'),
                   model_uri=UCO_LINKML.geolocationAddress, domain=None, range=Optional[Union[str, LocationId]])

slots.gid = Slot(uri=UCO_OBSERVABLE.gid, name="gid", curie=UCO_OBSERVABLE.curie('gid'),
                   model_uri=UCO_LINKML.gid, domain=None, range=Optional[int])

slots.globalFlagList = Slot(uri=UCO_OBSERVABLE.globalFlagList, name="globalFlagList", curie=UCO_OBSERVABLE.curie('globalFlagList'),
                   model_uri=UCO_LINKML.globalFlagList, domain=None, range=Optional[Union[Union[dict, GlobalFlagType], list[Union[dict, GlobalFlagType]]]])

slots.gpu = Slot(uri=UCO_OBSERVABLE.gpu, name="gpu", curie=UCO_OBSERVABLE.curie('gpu'),
                   model_uri=UCO_LINKML.gpu, domain=None, range=Optional[str])

slots.gpuFamily = Slot(uri=UCO_OBSERVABLE.gpuFamily, name="gpuFamily", curie=UCO_OBSERVABLE.curie('gpuFamily'),
                   model_uri=UCO_LINKML.gpuFamily, domain=None, range=Optional[str])

slots.groupName = Slot(uri=UCO_OBSERVABLE.groupName, name="groupName", curie=UCO_OBSERVABLE.curie('groupName'),
                   model_uri=UCO_LINKML.groupName, domain=None, range=Optional[str])

slots.groups = Slot(uri=UCO_OBSERVABLE.groups, name="groups", curie=UCO_OBSERVABLE.curie('groups'),
                   model_uri=UCO_LINKML.groups, domain=None, range=Optional[Union[str, list[str]]])

slots.hasChanged = Slot(uri=UCO_OBSERVABLE.hasChanged, name="hasChanged", curie=UCO_OBSERVABLE.curie('hasChanged'),
                   model_uri=UCO_LINKML.hasChanged, domain=None, range=Optional[Union[bool, Bool]])

slots.hash = Slot(uri=UCO_OBSERVABLE.hash, name="hash", curie=UCO_OBSERVABLE.curie('hash'),
                   model_uri=UCO_LINKML.hash, domain=None, range=Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]])

slots.hashes = Slot(uri=UCO_OBSERVABLE.hashes, name="hashes", curie=UCO_OBSERVABLE.curie('hashes'),
                   model_uri=UCO_LINKML.hashes, domain=None, range=Optional[Union[dict, Hash]])

slots.headerRaw = Slot(uri=UCO_OBSERVABLE.headerRaw, name="headerRaw", curie=UCO_OBSERVABLE.curie('headerRaw'),
                   model_uri=UCO_LINKML.headerRaw, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.hexadecimalValue = Slot(uri=UCO_OBSERVABLE.hexadecimalValue, name="hexadecimalValue", curie=UCO_OBSERVABLE.curie('hexadecimalValue'),
                   model_uri=UCO_LINKML.hexadecimalValue, domain=None, range=Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]])

slots.hiveType = Slot(uri=UCO_OBSERVABLE.hiveType, name="hiveType", curie=UCO_OBSERVABLE.curie('hiveType'),
                   model_uri=UCO_LINKML.hiveType, domain=None, range=Optional[str])

slots.homeDirectory = Slot(uri=UCO_OBSERVABLE.homeDirectory, name="homeDirectory", curie=UCO_OBSERVABLE.curie('homeDirectory'),
                   model_uri=UCO_LINKML.homeDirectory, domain=None, range=Optional[str])

slots.horizontalBeamWidth = Slot(uri=UCO_OBSERVABLE.horizontalBeamWidth, name="horizontalBeamWidth", curie=UCO_OBSERVABLE.curie('horizontalBeamWidth'),
                   model_uri=UCO_LINKML.horizontalBeamWidth, domain=None, range=Optional[Decimal])

slots.host = Slot(uri=UCO_OBSERVABLE.host, name="host", curie=UCO_OBSERVABLE.curie('host'),
                   model_uri=UCO_LINKML.host, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.hostname = Slot(uri=UCO_OBSERVABLE.hostname, name="hostname", curie=UCO_OBSERVABLE.curie('hostname'),
                   model_uri=UCO_LINKML.hostname, domain=None, range=Optional[str])

slots.httpMesageBodyLength = Slot(uri=UCO_OBSERVABLE.httpMesageBodyLength, name="httpMesageBodyLength", curie=UCO_OBSERVABLE.curie('httpMesageBodyLength'),
                   model_uri=UCO_LINKML.httpMesageBodyLength, domain=None, range=Optional[int])

slots.httpMessageBodyData = Slot(uri=UCO_OBSERVABLE.httpMessageBodyData, name="httpMessageBodyData", curie=UCO_OBSERVABLE.curie('httpMessageBodyData'),
                   model_uri=UCO_LINKML.httpMessageBodyData, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.httpRequestHeader = Slot(uri=UCO_OBSERVABLE.httpRequestHeader, name="httpRequestHeader", curie=UCO_OBSERVABLE.curie('httpRequestHeader'),
                   model_uri=UCO_LINKML.httpRequestHeader, domain=None, range=Optional[Union[dict, Dictionary]])

slots.iComHandlerAction = Slot(uri=UCO_OBSERVABLE.iComHandlerAction, name="iComHandlerAction", curie=UCO_OBSERVABLE.curie('iComHandlerAction'),
                   model_uri=UCO_LINKML.iComHandlerAction, domain=None, range=Optional[Union[dict, IComHandlerActionType]])

slots.iEmailAction = Slot(uri=UCO_OBSERVABLE.iEmailAction, name="iEmailAction", curie=UCO_OBSERVABLE.curie('iEmailAction'),
                   model_uri=UCO_LINKML.iEmailAction, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.iExecAction = Slot(uri=UCO_OBSERVABLE.iExecAction, name="iExecAction", curie=UCO_OBSERVABLE.curie('iExecAction'),
                   model_uri=UCO_LINKML.iExecAction, domain=None, range=Optional[Union[dict, IExecActionType]])

slots.iShowMessageAction = Slot(uri=UCO_OBSERVABLE.iShowMessageAction, name="iShowMessageAction", curie=UCO_OBSERVABLE.curie('iShowMessageAction'),
                   model_uri=UCO_LINKML.iShowMessageAction, domain=None, range=Optional[Union[dict, IShowMessageActionType]])

slots.icmpCode = Slot(uri=UCO_OBSERVABLE.icmpCode, name="icmpCode", curie=UCO_OBSERVABLE.curie('icmpCode'),
                   model_uri=UCO_LINKML.icmpCode, domain=None, range=Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]])

slots.icmpType = Slot(uri=UCO_OBSERVABLE.icmpType, name="icmpType", curie=UCO_OBSERVABLE.curie('icmpType'),
                   model_uri=UCO_LINKML.icmpType, domain=None, range=Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]])

slots.imageBase = Slot(uri=UCO_OBSERVABLE.imageBase, name="imageBase", curie=UCO_OBSERVABLE.curie('imageBase'),
                   model_uri=UCO_LINKML.imageBase, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.imageCompressionMethod = Slot(uri=UCO_OBSERVABLE.imageCompressionMethod, name="imageCompressionMethod", curie=UCO_OBSERVABLE.curie('imageCompressionMethod'),
                   model_uri=UCO_LINKML.imageCompressionMethod, domain=None, range=Optional[str])

slots.imageName = Slot(uri=UCO_OBSERVABLE.imageName, name="imageName", curie=UCO_OBSERVABLE.curie('imageName'),
                   model_uri=UCO_LINKML.imageName, domain=None, range=Optional[str])

slots.imageType = Slot(uri=UCO_OBSERVABLE.imageType, name="imageType", curie=UCO_OBSERVABLE.curie('imageType'),
                   model_uri=UCO_LINKML.imageType, domain=None, range=Optional[str])

slots.impHash = Slot(uri=UCO_OBSERVABLE.impHash, name="impHash", curie=UCO_OBSERVABLE.curie('impHash'),
                   model_uri=UCO_LINKML.impHash, domain=None, range=Optional[str])

slots.inReplyTo = Slot(uri=UCO_OBSERVABLE.inReplyTo, name="inReplyTo", curie=UCO_OBSERVABLE.curie('inReplyTo'),
                   model_uri=UCO_LINKML.inReplyTo, domain=None, range=Optional[str])

slots.inetLocation = Slot(uri=UCO_OBSERVABLE.inetLocation, name="inetLocation", curie=UCO_OBSERVABLE.curie('inetLocation'),
                   model_uri=UCO_LINKML.inetLocation, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.inhibitAnyPolicy = Slot(uri=UCO_OBSERVABLE.inhibitAnyPolicy, name="inhibitAnyPolicy", curie=UCO_OBSERVABLE.curie('inhibitAnyPolicy'),
                   model_uri=UCO_LINKML.inhibitAnyPolicy, domain=None, range=Optional[str])

slots.installDate = Slot(uri=UCO_OBSERVABLE.installDate, name="installDate", curie=UCO_OBSERVABLE.curie('installDate'),
                   model_uri=UCO_LINKML.installDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.installedVersionHistory = Slot(uri=UCO_OBSERVABLE.installedVersionHistory, name="installedVersionHistory", curie=UCO_OBSERVABLE.curie('installedVersionHistory'),
                   model_uri=UCO_LINKML.installedVersionHistory, domain=None, range=Optional[Union[Union[dict, ApplicationVersion], list[Union[dict, ApplicationVersion]]]])

slots.interceptedCallState = Slot(uri=UCO_OBSERVABLE.interceptedCallState, name="interceptedCallState", curie=UCO_OBSERVABLE.curie('interceptedCallState'),
                   model_uri=UCO_LINKML.interceptedCallState, domain=None, range=Optional[str])

slots.ip = Slot(uri=UCO_OBSERVABLE.ip, name="ip", curie=UCO_OBSERVABLE.curie('ip'),
                   model_uri=UCO_LINKML.ip, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.ipAddress = Slot(uri=UCO_OBSERVABLE.ipAddress, name="ipAddress", curie=UCO_OBSERVABLE.curie('ipAddress'),
                   model_uri=UCO_LINKML.ipAddress, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.ipGateway = Slot(uri=UCO_OBSERVABLE.ipGateway, name="ipGateway", curie=UCO_OBSERVABLE.curie('ipGateway'),
                   model_uri=UCO_LINKML.ipGateway, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.ipfix = Slot(uri=UCO_OBSERVABLE.ipfix, name="ipfix", curie=UCO_OBSERVABLE.curie('ipfix'),
                   model_uri=UCO_LINKML.ipfix, domain=None, range=Optional[Union[dict, Dictionary]])

slots.isADBRootEnabled = Slot(uri=UCO_OBSERVABLE.isADBRootEnabled, name="isADBRootEnabled", curie=UCO_OBSERVABLE.curie('isADBRootEnabled'),
                   model_uri=UCO_LINKML.isADBRootEnabled, domain=None, range=Optional[Union[bool, Bool]])

slots.isActive = Slot(uri=UCO_OBSERVABLE.isActive, name="isActive", curie=UCO_OBSERVABLE.curie('isActive'),
                   model_uri=UCO_LINKML.isActive, domain=None, range=Optional[Union[bool, Bool]])

slots.isDirectory = Slot(uri=UCO_OBSERVABLE.isDirectory, name="isDirectory", curie=UCO_OBSERVABLE.curie('isDirectory'),
                   model_uri=UCO_LINKML.isDirectory, domain=None, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.isDisabled = Slot(uri=UCO_OBSERVABLE.isDisabled, name="isDisabled", curie=UCO_OBSERVABLE.curie('isDisabled'),
                   model_uri=UCO_LINKML.isDisabled, domain=None, range=Optional[Union[bool, Bool]])

slots.isEnabled = Slot(uri=UCO_OBSERVABLE.isEnabled, name="isEnabled", curie=UCO_OBSERVABLE.curie('isEnabled'),
                   model_uri=UCO_LINKML.isEnabled, domain=None, range=Optional[Union[bool, Bool]])

slots.isEncrypted = Slot(uri=UCO_OBSERVABLE.isEncrypted, name="isEncrypted", curie=UCO_OBSERVABLE.curie('isEncrypted'),
                   model_uri=UCO_LINKML.isEncrypted, domain=None, range=Optional[Union[bool, Bool]])

slots.isHidden = Slot(uri=UCO_OBSERVABLE.isHidden, name="isHidden", curie=UCO_OBSERVABLE.curie('isHidden'),
                   model_uri=UCO_LINKML.isHidden, domain=None, range=Optional[Union[bool, Bool]])

slots.isInjected = Slot(uri=UCO_OBSERVABLE.isInjected, name="isInjected", curie=UCO_OBSERVABLE.curie('isInjected'),
                   model_uri=UCO_LINKML.isInjected, domain=None, range=Optional[Union[bool, Bool]])

slots.isLimitAdTrackingEnabled = Slot(uri=UCO_OBSERVABLE.isLimitAdTrackingEnabled, name="isLimitAdTrackingEnabled", curie=UCO_OBSERVABLE.curie('isLimitAdTrackingEnabled'),
                   model_uri=UCO_LINKML.isLimitAdTrackingEnabled, domain=None, range=Optional[Union[bool, Bool]])

slots.isMapped = Slot(uri=UCO_OBSERVABLE.isMapped, name="isMapped", curie=UCO_OBSERVABLE.curie('isMapped'),
                   model_uri=UCO_LINKML.isMapped, domain=None, range=Optional[Union[bool, Bool]])

slots.isMimeEncoded = Slot(uri=UCO_OBSERVABLE.isMimeEncoded, name="isMimeEncoded", curie=UCO_OBSERVABLE.curie('isMimeEncoded'),
                   model_uri=UCO_LINKML.isMimeEncoded, domain=None, range=Optional[Union[bool, Bool]])

slots.isMultipart = Slot(uri=UCO_OBSERVABLE.isMultipart, name="isMultipart", curie=UCO_OBSERVABLE.curie('isMultipart'),
                   model_uri=UCO_LINKML.isMultipart, domain=None, range=Optional[Union[bool, Bool]])

slots.isNamed = Slot(uri=UCO_OBSERVABLE.isNamed, name="isNamed", curie=UCO_OBSERVABLE.curie('isNamed'),
                   model_uri=UCO_LINKML.isNamed, domain=None, range=Optional[Union[bool, Bool]])

slots.isOptimized = Slot(uri=UCO_OBSERVABLE.isOptimized, name="isOptimized", curie=UCO_OBSERVABLE.curie('isOptimized'),
                   model_uri=UCO_LINKML.isOptimized, domain=None, range=Optional[Union[bool, Bool]])

slots.isPrivate = Slot(uri=UCO_OBSERVABLE.isPrivate, name="isPrivate", curie=UCO_OBSERVABLE.curie('isPrivate'),
                   model_uri=UCO_LINKML.isPrivate, domain=None, range=Optional[Union[bool, Bool]])

slots.isPrivileged = Slot(uri=UCO_OBSERVABLE.isPrivileged, name="isPrivileged", curie=UCO_OBSERVABLE.curie('isPrivileged'),
                   model_uri=UCO_LINKML.isPrivileged, domain=None, range=Optional[Union[bool, Bool]])

slots.isProtected = Slot(uri=UCO_OBSERVABLE.isProtected, name="isProtected", curie=UCO_OBSERVABLE.curie('isProtected'),
                   model_uri=UCO_LINKML.isProtected, domain=None, range=Optional[Union[bool, Bool]])

slots.isRead = Slot(uri=UCO_OBSERVABLE.isRead, name="isRead", curie=UCO_OBSERVABLE.curie('isRead'),
                   model_uri=UCO_LINKML.isRead, domain=None, range=Optional[Union[bool, Bool]])

slots.isSURootEnabled = Slot(uri=UCO_OBSERVABLE.isSURootEnabled, name="isSURootEnabled", curie=UCO_OBSERVABLE.curie('isSURootEnabled'),
                   model_uri=UCO_LINKML.isSURootEnabled, domain=None, range=Optional[Union[bool, Bool]])

slots.isSecure = Slot(uri=UCO_OBSERVABLE.isSecure, name="isSecure", curie=UCO_OBSERVABLE.curie('isSecure'),
                   model_uri=UCO_LINKML.isSecure, domain=None, range=Optional[Union[bool, Bool]])

slots.isSelfSigned = Slot(uri=UCO_OBSERVABLE.isSelfSigned, name="isSelfSigned", curie=UCO_OBSERVABLE.curie('isSelfSigned'),
                   model_uri=UCO_LINKML.isSelfSigned, domain=None, range=Optional[Union[bool, Bool]])

slots.isServiceAccount = Slot(uri=UCO_OBSERVABLE.isServiceAccount, name="isServiceAccount", curie=UCO_OBSERVABLE.curie('isServiceAccount'),
                   model_uri=UCO_LINKML.isServiceAccount, domain=None, range=Optional[Union[bool, Bool]])

slots.isTLD = Slot(uri=UCO_OBSERVABLE.isTLD, name="isTLD", curie=UCO_OBSERVABLE.curie('isTLD'),
                   model_uri=UCO_LINKML.isTLD, domain=None, range=Optional[Union[bool, Bool]])

slots.isVolatile = Slot(uri=UCO_OBSERVABLE.isVolatile, name="isVolatile", curie=UCO_OBSERVABLE.curie('isVolatile'),
                   model_uri=UCO_LINKML.isVolatile, domain=None, range=Optional[Union[bool, Bool]])

slots.issuer = Slot(uri=UCO_OBSERVABLE.issuer, name="issuer", curie=UCO_OBSERVABLE.curie('issuer'),
                   model_uri=UCO_LINKML.issuer, domain=None, range=Optional[str])

slots.issuerAlternativeName = Slot(uri=UCO_OBSERVABLE.issuerAlternativeName, name="issuerAlternativeName", curie=UCO_OBSERVABLE.curie('issuerAlternativeName'),
                   model_uri=UCO_LINKML.issuerAlternativeName, domain=None, range=Optional[str])

slots.issuerHash = Slot(uri=UCO_OBSERVABLE.issuerHash, name="issuerHash", curie=UCO_OBSERVABLE.curie('issuerHash'),
                   model_uri=UCO_LINKML.issuerHash, domain=None, range=Optional[Union[dict, Hash]])

slots.keyUsage = Slot(uri=UCO_OBSERVABLE.keyUsage, name="keyUsage", curie=UCO_OBSERVABLE.curie('keyUsage'),
                   model_uri=UCO_LINKML.keyUsage, domain=None, range=Optional[str])

slots.keypadUnlockCode = Slot(uri=UCO_OBSERVABLE.keypadUnlockCode, name="keypadUnlockCode", curie=UCO_OBSERVABLE.curie('keypadUnlockCode'),
                   model_uri=UCO_LINKML.keypadUnlockCode, domain=None, range=Optional[str])

slots.keywordSearchTerm = Slot(uri=UCO_OBSERVABLE.keywordSearchTerm, name="keywordSearchTerm", curie=UCO_OBSERVABLE.curie('keywordSearchTerm'),
                   model_uri=UCO_LINKML.keywordSearchTerm, domain=None, range=Optional[Union[str, list[str]]])

slots.labels = Slot(uri=UCO_OBSERVABLE.labels, name="labels", curie=UCO_OBSERVABLE.curie('labels'),
                   model_uri=UCO_LINKML.labels, domain=None, range=Optional[Union[str, list[str]]])

slots.language = Slot(uri=UCO_OBSERVABLE.language, name="language", curie=UCO_OBSERVABLE.curie('language'),
                   model_uri=UCO_LINKML.language, domain=None, range=Optional[str])

slots.lastLoginTime = Slot(uri=UCO_OBSERVABLE.lastLoginTime, name="lastLoginTime", curie=UCO_OBSERVABLE.curie('lastLoginTime'),
                   model_uri=UCO_LINKML.lastLoginTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lastName = Slot(uri=UCO_OBSERVABLE.lastName, name="lastName", curie=UCO_OBSERVABLE.curie('lastName'),
                   model_uri=UCO_LINKML.lastName, domain=None, range=Optional[str])

slots.lastRun = Slot(uri=UCO_OBSERVABLE.lastRun, name="lastRun", curie=UCO_OBSERVABLE.curie('lastRun'),
                   model_uri=UCO_LINKML.lastRun, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lastShutdownDate = Slot(uri=UCO_OBSERVABLE.lastShutdownDate, name="lastShutdownDate", curie=UCO_OBSERVABLE.curie('lastShutdownDate'),
                   model_uri=UCO_LINKML.lastShutdownDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lastTimeContacted = Slot(uri=UCO_OBSERVABLE.lastTimeContacted, name="lastTimeContacted", curie=UCO_OBSERVABLE.curie('lastTimeContacted'),
                   model_uri=UCO_LINKML.lastTimeContacted, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lastVisit = Slot(uri=UCO_OBSERVABLE.lastVisit, name="lastVisit", curie=UCO_OBSERVABLE.curie('lastVisit'),
                   model_uri=UCO_LINKML.lastVisit, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.length = Slot(uri=UCO_OBSERVABLE.length, name="length", curie=UCO_OBSERVABLE.curie('length'),
                   model_uri=UCO_LINKML.length, domain=None, range=Optional[int])

slots.libraryType = Slot(uri=UCO_OBSERVABLE.libraryType, name="libraryType", curie=UCO_OBSERVABLE.curie('libraryType'),
                   model_uri=UCO_LINKML.libraryType, domain=None, range=Optional[str])

slots.listedCount = Slot(uri=UCO_OBSERVABLE.listedCount, name="listedCount", curie=UCO_OBSERVABLE.curie('listedCount'),
                   model_uri=UCO_LINKML.listedCount, domain=None, range=Optional[int])

slots.loaderFlags = Slot(uri=UCO_OBSERVABLE.loaderFlags, name="loaderFlags", curie=UCO_OBSERVABLE.curie('loaderFlags'),
                   model_uri=UCO_LINKML.loaderFlags, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.localTime = Slot(uri=UCO_OBSERVABLE.localTime, name="localTime", curie=UCO_OBSERVABLE.curie('localTime'),
                   model_uri=UCO_LINKML.localTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.loginTime = Slot(uri=UCO_OBSERVABLE.loginTime, name="loginTime", curie=UCO_OBSERVABLE.curie('loginTime'),
                   model_uri=UCO_LINKML.loginTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.logoutTime = Slot(uri=UCO_OBSERVABLE.logoutTime, name="logoutTime", curie=UCO_OBSERVABLE.curie('logoutTime'),
                   model_uri=UCO_LINKML.logoutTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lookupDate = Slot(uri=UCO_OBSERVABLE.lookupDate, name="lookupDate", curie=UCO_OBSERVABLE.curie('lookupDate'),
                   model_uri=UCO_LINKML.lookupDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.macAddress = Slot(uri=UCO_OBSERVABLE.macAddress, name="macAddress", curie=UCO_OBSERVABLE.curie('macAddress'),
                   model_uri=UCO_LINKML.macAddress, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.machine = Slot(uri=UCO_OBSERVABLE.machine, name="machine", curie=UCO_OBSERVABLE.curie('machine'),
                   model_uri=UCO_LINKML.machine, domain=None, range=Optional[Union[str, list[str]]])

slots.magic = Slot(uri=UCO_OBSERVABLE.magic, name="magic", curie=UCO_OBSERVABLE.curie('magic'),
                   model_uri=UCO_LINKML.magic, domain=None, range=Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]])

slots.magicNumber = Slot(uri=UCO_OBSERVABLE.magicNumber, name="magicNumber", curie=UCO_OBSERVABLE.curie('magicNumber'),
                   model_uri=UCO_LINKML.magicNumber, domain=None, range=Optional[str])

slots.majorImageVersion = Slot(uri=UCO_OBSERVABLE.majorImageVersion, name="majorImageVersion", curie=UCO_OBSERVABLE.curie('majorImageVersion'),
                   model_uri=UCO_LINKML.majorImageVersion, domain=None, range=Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]])

slots.majorLinkerVersion = Slot(uri=UCO_OBSERVABLE.majorLinkerVersion, name="majorLinkerVersion", curie=UCO_OBSERVABLE.curie('majorLinkerVersion'),
                   model_uri=UCO_LINKML.majorLinkerVersion, domain=None, range=Optional[Union[Union[int, UcoByte], list[Union[int, UcoByte]]]])

slots.majorOSVersion = Slot(uri=UCO_OBSERVABLE.majorOSVersion, name="majorOSVersion", curie=UCO_OBSERVABLE.curie('majorOSVersion'),
                   model_uri=UCO_LINKML.majorOSVersion, domain=None, range=Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]])

slots.majorSubsystemVersion = Slot(uri=UCO_OBSERVABLE.majorSubsystemVersion, name="majorSubsystemVersion", curie=UCO_OBSERVABLE.curie('majorSubsystemVersion'),
                   model_uri=UCO_LINKML.majorSubsystemVersion, domain=None, range=Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]])

slots.manuallyEnteredCount = Slot(uri=UCO_OBSERVABLE.manuallyEnteredCount, name="manuallyEnteredCount", curie=UCO_OBSERVABLE.curie('manuallyEnteredCount'),
                   model_uri=UCO_LINKML.manuallyEnteredCount, domain=None, range=Optional[Union[int, UcoNonNegativeInteger]])

slots.manufacturer = Slot(uri=UCO_OBSERVABLE.manufacturer, name="manufacturer", curie=UCO_OBSERVABLE.curie('manufacturer'),
                   model_uri=UCO_LINKML.manufacturer, domain=None, range=Optional[Union[str, IdentityId]])

slots.maxRunTime = Slot(uri=UCO_OBSERVABLE.maxRunTime, name="maxRunTime", curie=UCO_OBSERVABLE.curie('maxRunTime'),
                   model_uri=UCO_LINKML.maxRunTime, domain=None, range=Optional[int])

slots.messageID = Slot(uri=UCO_OBSERVABLE.messageID, name="messageID", curie=UCO_OBSERVABLE.curie('messageID'),
                   model_uri=UCO_LINKML.messageID, domain=None, range=Optional[str])

slots.messageText = Slot(uri=UCO_OBSERVABLE.messageText, name="messageText", curie=UCO_OBSERVABLE.curie('messageText'),
                   model_uri=UCO_LINKML.messageText, domain=None, range=Optional[str])

slots.messageThread = Slot(uri=UCO_OBSERVABLE.messageThread, name="messageThread", curie=UCO_OBSERVABLE.curie('messageThread'),
                   model_uri=UCO_LINKML.messageThread, domain=None, range=Optional[Union[str, ThreadId]])

slots.messageType = Slot(uri=UCO_OBSERVABLE.messageType, name="messageType", curie=UCO_OBSERVABLE.curie('messageType'),
                   model_uri=UCO_LINKML.messageType, domain=None, range=Optional[str])

slots.messagingAddress = Slot(uri=UCO_OBSERVABLE.messagingAddress, name="messagingAddress", curie=UCO_OBSERVABLE.curie('messagingAddress'),
                   model_uri=UCO_LINKML.messagingAddress, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.metadataChangeTime = Slot(uri=UCO_OBSERVABLE.metadataChangeTime, name="metadataChangeTime", curie=UCO_OBSERVABLE.curie('metadataChangeTime'),
                   model_uri=UCO_LINKML.metadataChangeTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.metadataRecoveredStatus = Slot(uri=UCO_OBSERVABLE.metadataRecoveredStatus, name="metadataRecoveredStatus", curie=UCO_OBSERVABLE.curie('metadataRecoveredStatus'),
                   model_uri=UCO_LINKML.metadataRecoveredStatus, domain=None, range=Optional[Union[str, "RecoveredObjectStatusVocab"]])

slots.mftFileID = Slot(uri=UCO_OBSERVABLE.mftFileID, name="mftFileID", curie=UCO_OBSERVABLE.curie('mftFileID'),
                   model_uri=UCO_LINKML.mftFileID, domain=None, range=Optional[int])

slots.mftFileNameAccessedTime = Slot(uri=UCO_OBSERVABLE.mftFileNameAccessedTime, name="mftFileNameAccessedTime", curie=UCO_OBSERVABLE.curie('mftFileNameAccessedTime'),
                   model_uri=UCO_LINKML.mftFileNameAccessedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mftFileNameCreatedTime = Slot(uri=UCO_OBSERVABLE.mftFileNameCreatedTime, name="mftFileNameCreatedTime", curie=UCO_OBSERVABLE.curie('mftFileNameCreatedTime'),
                   model_uri=UCO_LINKML.mftFileNameCreatedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mftFileNameLength = Slot(uri=UCO_OBSERVABLE.mftFileNameLength, name="mftFileNameLength", curie=UCO_OBSERVABLE.curie('mftFileNameLength'),
                   model_uri=UCO_LINKML.mftFileNameLength, domain=None, range=Optional[int])

slots.mftFileNameModifiedTime = Slot(uri=UCO_OBSERVABLE.mftFileNameModifiedTime, name="mftFileNameModifiedTime", curie=UCO_OBSERVABLE.curie('mftFileNameModifiedTime'),
                   model_uri=UCO_LINKML.mftFileNameModifiedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mftFileNameRecordChangeTime = Slot(uri=UCO_OBSERVABLE.mftFileNameRecordChangeTime, name="mftFileNameRecordChangeTime", curie=UCO_OBSERVABLE.curie('mftFileNameRecordChangeTime'),
                   model_uri=UCO_LINKML.mftFileNameRecordChangeTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mftFlags = Slot(uri=UCO_OBSERVABLE.mftFlags, name="mftFlags", curie=UCO_OBSERVABLE.curie('mftFlags'),
                   model_uri=UCO_LINKML.mftFlags, domain=None, range=Optional[int])

slots.mftParentID = Slot(uri=UCO_OBSERVABLE.mftParentID, name="mftParentID", curie=UCO_OBSERVABLE.curie('mftParentID'),
                   model_uri=UCO_LINKML.mftParentID, domain=None, range=Optional[int])

slots.mftRecordChangeTime = Slot(uri=UCO_OBSERVABLE.mftRecordChangeTime, name="mftRecordChangeTime", curie=UCO_OBSERVABLE.curie('mftRecordChangeTime'),
                   model_uri=UCO_LINKML.mftRecordChangeTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.middleName = Slot(uri=UCO_OBSERVABLE.middleName, name="middleName", curie=UCO_OBSERVABLE.curie('middleName'),
                   model_uri=UCO_LINKML.middleName, domain=None, range=Optional[str])

slots.mimeClass = Slot(uri=UCO_OBSERVABLE.mimeClass, name="mimeClass", curie=UCO_OBSERVABLE.curie('mimeClass'),
                   model_uri=UCO_LINKML.mimeClass, domain=None, range=Optional[str])

slots.mimeType = Slot(uri=UCO_OBSERVABLE.mimeType, name="mimeType", curie=UCO_OBSERVABLE.curie('mimeType'),
                   model_uri=UCO_LINKML.mimeType, domain=None, range=Optional[Union[str, list[str]]])

slots.minorImageVersion = Slot(uri=UCO_OBSERVABLE.minorImageVersion, name="minorImageVersion", curie=UCO_OBSERVABLE.curie('minorImageVersion'),
                   model_uri=UCO_LINKML.minorImageVersion, domain=None, range=Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]])

slots.minorLinkerVersion = Slot(uri=UCO_OBSERVABLE.minorLinkerVersion, name="minorLinkerVersion", curie=UCO_OBSERVABLE.curie('minorLinkerVersion'),
                   model_uri=UCO_LINKML.minorLinkerVersion, domain=None, range=Optional[Union[Union[int, UcoByte], list[Union[int, UcoByte]]]])

slots.minorOSVersion = Slot(uri=UCO_OBSERVABLE.minorOSVersion, name="minorOSVersion", curie=UCO_OBSERVABLE.curie('minorOSVersion'),
                   model_uri=UCO_LINKML.minorOSVersion, domain=None, range=Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]])

slots.minorSubsystemVersion = Slot(uri=UCO_OBSERVABLE.minorSubsystemVersion, name="minorSubsystemVersion", curie=UCO_OBSERVABLE.curie('minorSubsystemVersion'),
                   model_uri=UCO_LINKML.minorSubsystemVersion, domain=None, range=Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]])

slots.mockLocationsAllowed = Slot(uri=UCO_OBSERVABLE.mockLocationsAllowed, name="mockLocationsAllowed", curie=UCO_OBSERVABLE.curie('mockLocationsAllowed'),
                   model_uri=UCO_LINKML.mockLocationsAllowed, domain=None, range=Optional[Union[bool, Bool]])

slots.model = Slot(uri=UCO_OBSERVABLE.model, name="model", curie=UCO_OBSERVABLE.curie('model'),
                   model_uri=UCO_LINKML.model, domain=None, range=Optional[str])

slots.mostRecentRunTime = Slot(uri=UCO_OBSERVABLE.mostRecentRunTime, name="mostRecentRunTime", curie=UCO_OBSERVABLE.curie('mostRecentRunTime'),
                   model_uri=UCO_LINKML.mostRecentRunTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mountPoint = Slot(uri=UCO_OBSERVABLE.mountPoint, name="mountPoint", curie=UCO_OBSERVABLE.curie('mountPoint'),
                   model_uri=UCO_LINKML.mountPoint, domain=None, range=Optional[str])

slots.msProductID = Slot(uri=UCO_OBSERVABLE.msProductID, name="msProductID", curie=UCO_OBSERVABLE.curie('msProductID'),
                   model_uri=UCO_LINKML.msProductID, domain=None, range=Optional[str])

slots.msProductName = Slot(uri=UCO_OBSERVABLE.msProductName, name="msProductName", curie=UCO_OBSERVABLE.curie('msProductName'),
                   model_uri=UCO_LINKML.msProductName, domain=None, range=Optional[str])

slots.mutexName = Slot(uri=UCO_OBSERVABLE.mutexName, name="mutexName", curie=UCO_OBSERVABLE.curie('mutexName'),
                   model_uri=UCO_LINKML.mutexName, domain=None, range=Optional[str])

slots.nameConstraints = Slot(uri=UCO_OBSERVABLE.nameConstraints, name="nameConstraints", curie=UCO_OBSERVABLE.curie('nameConstraints'),
                   model_uri=UCO_LINKML.nameConstraints, domain=None, range=Optional[str])

slots.namePhonetic = Slot(uri=UCO_OBSERVABLE.namePhonetic, name="namePhonetic", curie=UCO_OBSERVABLE.curie('namePhonetic'),
                   model_uri=UCO_LINKML.namePhonetic, domain=None, range=Optional[str])

slots.namePrefix = Slot(uri=UCO_OBSERVABLE.namePrefix, name="namePrefix", curie=UCO_OBSERVABLE.curie('namePrefix'),
                   model_uri=UCO_LINKML.namePrefix, domain=None, range=Optional[str])

slots.nameRecoveredStatus = Slot(uri=UCO_OBSERVABLE.nameRecoveredStatus, name="nameRecoveredStatus", curie=UCO_OBSERVABLE.curie('nameRecoveredStatus'),
                   model_uri=UCO_LINKML.nameRecoveredStatus, domain=None, range=Optional[Union[str, "RecoveredObjectStatusVocab"]])

slots.nameServer = Slot(uri=UCO_OBSERVABLE.nameServer, name="nameServer", curie=UCO_OBSERVABLE.curie('nameServer'),
                   model_uri=UCO_LINKML.nameServer, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.nameSuffix = Slot(uri=UCO_OBSERVABLE.nameSuffix, name="nameSuffix", curie=UCO_OBSERVABLE.curie('nameSuffix'),
                   model_uri=UCO_LINKML.nameSuffix, domain=None, range=Optional[str])

slots.netBIOSName = Slot(uri=UCO_OBSERVABLE.netBIOSName, name="netBIOSName", curie=UCO_OBSERVABLE.curie('netBIOSName'),
                   model_uri=UCO_LINKML.netBIOSName, domain=None, range=Optional[str])

slots.network = Slot(uri=UCO_OBSERVABLE.network, name="network", curie=UCO_OBSERVABLE.curie('network'),
                   model_uri=UCO_LINKML.network, domain=None, range=Optional[str])

slots.networkInterface = Slot(uri=UCO_OBSERVABLE.networkInterface, name="networkInterface", curie=UCO_OBSERVABLE.curie('networkInterface'),
                   model_uri=UCO_LINKML.networkInterface, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.newObject = Slot(uri=UCO_OBSERVABLE.newObject, name="newObject", curie=UCO_OBSERVABLE.curie('newObject'),
                   model_uri=UCO_LINKML.newObject, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.nextRunTime = Slot(uri=UCO_OBSERVABLE.nextRunTime, name="nextRunTime", curie=UCO_OBSERVABLE.curie('nextRunTime'),
                   model_uri=UCO_LINKML.nextRunTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.nickname = Slot(uri=UCO_OBSERVABLE.nickname, name="nickname", curie=UCO_OBSERVABLE.curie('nickname'),
                   model_uri=UCO_LINKML.nickname, domain=None, range=Optional[Union[str, list[str]]])

slots.ntfsHardLinkCount = Slot(uri=UCO_OBSERVABLE.ntfsHardLinkCount, name="ntfsHardLinkCount", curie=UCO_OBSERVABLE.curie('ntfsHardLinkCount'),
                   model_uri=UCO_LINKML.ntfsHardLinkCount, domain=None, range=Optional[int])

slots.ntfsOwnerID = Slot(uri=UCO_OBSERVABLE.ntfsOwnerID, name="ntfsOwnerID", curie=UCO_OBSERVABLE.curie('ntfsOwnerID'),
                   model_uri=UCO_LINKML.ntfsOwnerID, domain=None, range=Optional[str])

slots.ntfsOwnerSID = Slot(uri=UCO_OBSERVABLE.ntfsOwnerSID, name="ntfsOwnerSID", curie=UCO_OBSERVABLE.curie('ntfsOwnerSID'),
                   model_uri=UCO_LINKML.ntfsOwnerSID, domain=None, range=Optional[str])

slots.number = Slot(uri=UCO_OBSERVABLE.number, name="number", curie=UCO_OBSERVABLE.curie('number'),
                   model_uri=UCO_LINKML.number, domain=None, range=Optional[int])

slots.numberOfLaunches = Slot(uri=UCO_OBSERVABLE.numberOfLaunches, name="numberOfLaunches", curie=UCO_OBSERVABLE.curie('numberOfLaunches'),
                   model_uri=UCO_LINKML.numberOfLaunches, domain=None, range=Optional[int])

slots.numberOfRVAAndSizes = Slot(uri=UCO_OBSERVABLE.numberOfRVAAndSizes, name="numberOfRVAAndSizes", curie=UCO_OBSERVABLE.curie('numberOfRVAAndSizes'),
                   model_uri=UCO_LINKML.numberOfRVAAndSizes, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.numberOfSections = Slot(uri=UCO_OBSERVABLE.numberOfSections, name="numberOfSections", curie=UCO_OBSERVABLE.curie('numberOfSections'),
                   model_uri=UCO_LINKML.numberOfSections, domain=None, range=Optional[int])

slots.numberOfSubkeys = Slot(uri=UCO_OBSERVABLE.numberOfSubkeys, name="numberOfSubkeys", curie=UCO_OBSERVABLE.curie('numberOfSubkeys'),
                   model_uri=UCO_LINKML.numberOfSubkeys, domain=None, range=Optional[int])

slots.numberOfSymbols = Slot(uri=UCO_OBSERVABLE.numberOfSymbols, name="numberOfSymbols", curie=UCO_OBSERVABLE.curie('numberOfSymbols'),
                   model_uri=UCO_LINKML.numberOfSymbols, domain=None, range=Optional[int])

slots.numberTimesContacted = Slot(uri=UCO_OBSERVABLE.numberTimesContacted, name="numberTimesContacted", curie=UCO_OBSERVABLE.curie('numberTimesContacted'),
                   model_uri=UCO_LINKML.numberTimesContacted, domain=None, range=Optional[int])

slots.objectGUID = Slot(uri=UCO_OBSERVABLE.objectGUID, name="objectGUID", curie=UCO_OBSERVABLE.curie('objectGUID'),
                   model_uri=UCO_LINKML.objectGUID, domain=None, range=Optional[str])

slots.observableCreatedTime = Slot(uri=UCO_OBSERVABLE.observableCreatedTime, name="observableCreatedTime", curie=UCO_OBSERVABLE.curie('observableCreatedTime'),
                   model_uri=UCO_LINKML.observableCreatedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.observable_context = Slot(uri=UCO_OBSERVABLE.context, name="observable_context", curie=UCO_OBSERVABLE.curie('context'),
                   model_uri=UCO_LINKML.observable_context, domain=None, range=Optional[str])

slots.observable_cpeid = Slot(uri=UCO_OBSERVABLE.cpeid, name="observable_cpeid", curie=UCO_OBSERVABLE.curie('cpeid'),
                   model_uri=UCO_LINKML.observable_cpeid, domain=None, range=Optional[str])

slots.observable_creator = Slot(uri=UCO_OBSERVABLE.creator, name="observable_creator", curie=UCO_OBSERVABLE.curie('creator'),
                   model_uri=UCO_LINKML.observable_creator, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.observable_endTime = Slot(uri=UCO_OBSERVABLE.endTime, name="observable_endTime", curie=UCO_OBSERVABLE.curie('endTime'),
                   model_uri=UCO_LINKML.observable_endTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.observable_eventType = Slot(uri=UCO_OBSERVABLE.eventType, name="observable_eventType", curie=UCO_OBSERVABLE.curie('eventType'),
                   model_uri=UCO_LINKML.observable_eventType, domain=None, range=Optional[str])

slots.observable_key = Slot(uri=UCO_OBSERVABLE.key, name="observable_key", curie=UCO_OBSERVABLE.curie('key'),
                   model_uri=UCO_LINKML.observable_key, domain=None, range=Optional[str])

slots.observable_location = Slot(uri=UCO_OBSERVABLE.location, name="observable_location", curie=UCO_OBSERVABLE.curie('location'),
                   model_uri=UCO_LINKML.observable_location, domain=None, range=Optional[Union[str, LocationId]])

slots.observable_modifiedTime = Slot(uri=UCO_OBSERVABLE.modifiedTime, name="observable_modifiedTime", curie=UCO_OBSERVABLE.curie('modifiedTime'),
                   model_uri=UCO_LINKML.observable_modifiedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.observable_participant = Slot(uri=UCO_OBSERVABLE.participant, name="observable_participant", curie=UCO_OBSERVABLE.curie('participant'),
                   model_uri=UCO_LINKML.observable_participant, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.observable_references = Slot(uri=UCO_OBSERVABLE.references, name="observable_references", curie=UCO_OBSERVABLE.curie('references'),
                   model_uri=UCO_LINKML.observable_references, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.observable_startTime = Slot(uri=UCO_OBSERVABLE.startTime, name="observable_startTime", curie=UCO_OBSERVABLE.curie('startTime'),
                   model_uri=UCO_LINKML.observable_startTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.observable_swid = Slot(uri=UCO_OBSERVABLE.swid, name="observable_swid", curie=UCO_OBSERVABLE.curie('swid'),
                   model_uri=UCO_LINKML.observable_swid, domain=None, range=Optional[str])

slots.observable_value = Slot(uri=UCO_OBSERVABLE.value, name="observable_value", curie=UCO_OBSERVABLE.curie('value'),
                   model_uri=UCO_LINKML.observable_value, domain=None, range=Optional[str])

slots.observable_version = Slot(uri=UCO_OBSERVABLE.version, name="observable_version", curie=UCO_OBSERVABLE.curie('version'),
                   model_uri=UCO_LINKML.observable_version, domain=None, range=Optional[str])

slots.oldObject = Slot(uri=UCO_OBSERVABLE.oldObject, name="oldObject", curie=UCO_OBSERVABLE.curie('oldObject'),
                   model_uri=UCO_LINKML.oldObject, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.openFileDescriptor = Slot(uri=UCO_OBSERVABLE.openFileDescriptor, name="openFileDescriptor", curie=UCO_OBSERVABLE.curie('openFileDescriptor'),
                   model_uri=UCO_LINKML.openFileDescriptor, domain=None, range=Optional[Union[int, list[int]]])

slots.operatingSystem = Slot(uri=UCO_OBSERVABLE.operatingSystem, name="operatingSystem", curie=UCO_OBSERVABLE.curie('operatingSystem'),
                   model_uri=UCO_LINKML.operatingSystem, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.optionalHeader = Slot(uri=UCO_OBSERVABLE.optionalHeader, name="optionalHeader", curie=UCO_OBSERVABLE.curie('optionalHeader'),
                   model_uri=UCO_LINKML.optionalHeader, domain=None, range=Optional[Union[dict, WindowsPEOptionalHeader]])

slots.options = Slot(uri=UCO_OBSERVABLE.options, name="options", curie=UCO_OBSERVABLE.curie('options'),
                   model_uri=UCO_LINKML.options, domain=None, range=Optional[str])

slots.organizationDepartment = Slot(uri=UCO_OBSERVABLE.organizationDepartment, name="organizationDepartment", curie=UCO_OBSERVABLE.curie('organizationDepartment'),
                   model_uri=UCO_LINKML.organizationDepartment, domain=None, range=Optional[str])

slots.organizationLocation = Slot(uri=UCO_OBSERVABLE.organizationLocation, name="organizationLocation", curie=UCO_OBSERVABLE.curie('organizationLocation'),
                   model_uri=UCO_LINKML.organizationLocation, domain=None, range=Optional[Union[Union[dict, ContactAddress], list[Union[dict, ContactAddress]]]])

slots.organizationPosition = Slot(uri=UCO_OBSERVABLE.organizationPosition, name="organizationPosition", curie=UCO_OBSERVABLE.curie('organizationPosition'),
                   model_uri=UCO_LINKML.organizationPosition, domain=None, range=Optional[str])

slots.osInstallDate = Slot(uri=UCO_OBSERVABLE.osInstallDate, name="osInstallDate", curie=UCO_OBSERVABLE.curie('osInstallDate'),
                   model_uri=UCO_LINKML.osInstallDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.osLastUpgradeDate = Slot(uri=UCO_OBSERVABLE.osLastUpgradeDate, name="osLastUpgradeDate", curie=UCO_OBSERVABLE.curie('osLastUpgradeDate'),
                   model_uri=UCO_LINKML.osLastUpgradeDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.otherHeaders = Slot(uri=UCO_OBSERVABLE.otherHeaders, name="otherHeaders", curie=UCO_OBSERVABLE.curie('otherHeaders'),
                   model_uri=UCO_LINKML.otherHeaders, domain=None, range=Optional[Union[dict, Dictionary]])

slots.owner = Slot(uri=UCO_OBSERVABLE.owner, name="owner", curie=UCO_OBSERVABLE.curie('owner'),
                   model_uri=UCO_LINKML.owner, domain=None, range=Optional[Union[str, UcoObjectId]])

slots.ownerSID = Slot(uri=UCO_OBSERVABLE.ownerSID, name="ownerSID", curie=UCO_OBSERVABLE.curie('ownerSID'),
                   model_uri=UCO_LINKML.ownerSID, domain=None, range=Optional[str])

slots.pageTitle = Slot(uri=UCO_OBSERVABLE.pageTitle, name="pageTitle", curie=UCO_OBSERVABLE.curie('pageTitle'),
                   model_uri=UCO_LINKML.pageTitle, domain=None, range=Optional[str])

slots.parameterAddress = Slot(uri=UCO_OBSERVABLE.parameterAddress, name="parameterAddress", curie=UCO_OBSERVABLE.curie('parameterAddress'),
                   model_uri=UCO_LINKML.parameterAddress, domain=None, range=Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]])

slots.parameters = Slot(uri=UCO_OBSERVABLE.parameters, name="parameters", curie=UCO_OBSERVABLE.curie('parameters'),
                   model_uri=UCO_LINKML.parameters, domain=None, range=Optional[str])

slots.parent = Slot(uri=UCO_OBSERVABLE.parent, name="parent", curie=UCO_OBSERVABLE.curie('parent'),
                   model_uri=UCO_LINKML.parent, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.partition = Slot(uri=UCO_OBSERVABLE.partition, name="partition", curie=UCO_OBSERVABLE.curie('partition'),
                   model_uri=UCO_LINKML.partition, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.partitionID = Slot(uri=UCO_OBSERVABLE.partitionID, name="partitionID", curie=UCO_OBSERVABLE.curie('partitionID'),
                   model_uri=UCO_LINKML.partitionID, domain=None, range=Optional[str])

slots.partitionLength = Slot(uri=UCO_OBSERVABLE.partitionLength, name="partitionLength", curie=UCO_OBSERVABLE.curie('partitionLength'),
                   model_uri=UCO_LINKML.partitionLength, domain=None, range=Optional[int])

slots.partitionOffset = Slot(uri=UCO_OBSERVABLE.partitionOffset, name="partitionOffset", curie=UCO_OBSERVABLE.curie('partitionOffset'),
                   model_uri=UCO_LINKML.partitionOffset, domain=None, range=Optional[int])

slots.password = Slot(uri=UCO_OBSERVABLE.password, name="password", curie=UCO_OBSERVABLE.curie('password'),
                   model_uri=UCO_LINKML.password, domain=None, range=Optional[str])

slots.passwordLastChanged = Slot(uri=UCO_OBSERVABLE.passwordLastChanged, name="passwordLastChanged", curie=UCO_OBSERVABLE.curie('passwordLastChanged'),
                   model_uri=UCO_LINKML.passwordLastChanged, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.passwordType = Slot(uri=UCO_OBSERVABLE.passwordType, name="passwordType", curie=UCO_OBSERVABLE.curie('passwordType'),
                   model_uri=UCO_LINKML.passwordType, domain=None, range=Optional[str])

slots.path = Slot(uri=UCO_OBSERVABLE.path, name="path", curie=UCO_OBSERVABLE.curie('path'),
                   model_uri=UCO_LINKML.path, domain=None, range=Optional[str])

slots.pdfCreationDate = Slot(uri=UCO_OBSERVABLE.pdfCreationDate, name="pdfCreationDate", curie=UCO_OBSERVABLE.curie('pdfCreationDate'),
                   model_uri=UCO_LINKML.pdfCreationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.pdfId0 = Slot(uri=UCO_OBSERVABLE.pdfId0, name="pdfId0", curie=UCO_OBSERVABLE.curie('pdfId0'),
                   model_uri=UCO_LINKML.pdfId0, domain=None, range=Optional[Union[str, list[str]]])

slots.pdfId1 = Slot(uri=UCO_OBSERVABLE.pdfId1, name="pdfId1", curie=UCO_OBSERVABLE.curie('pdfId1'),
                   model_uri=UCO_LINKML.pdfId1, domain=None, range=Optional[str])

slots.pdfModDate = Slot(uri=UCO_OBSERVABLE.pdfModDate, name="pdfModDate", curie=UCO_OBSERVABLE.curie('pdfModDate'),
                   model_uri=UCO_LINKML.pdfModDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.peType = Slot(uri=UCO_OBSERVABLE.peType, name="peType", curie=UCO_OBSERVABLE.curie('peType'),
                   model_uri=UCO_LINKML.peType, domain=None, range=Optional[str])

slots.phoneActivationTime = Slot(uri=UCO_OBSERVABLE.phoneActivationTime, name="phoneActivationTime", curie=UCO_OBSERVABLE.curie('phoneActivationTime'),
                   model_uri=UCO_LINKML.phoneActivationTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.phoneNumber = Slot(uri=UCO_OBSERVABLE.phoneNumber, name="phoneNumber", curie=UCO_OBSERVABLE.curie('phoneNumber'),
                   model_uri=UCO_LINKML.phoneNumber, domain=None, range=Optional[str])

slots.pictureHeight = Slot(uri=UCO_OBSERVABLE.pictureHeight, name="pictureHeight", curie=UCO_OBSERVABLE.curie('pictureHeight'),
                   model_uri=UCO_LINKML.pictureHeight, domain=None, range=Optional[int])

slots.pictureType = Slot(uri=UCO_OBSERVABLE.pictureType, name="pictureType", curie=UCO_OBSERVABLE.curie('pictureType'),
                   model_uri=UCO_LINKML.pictureType, domain=None, range=Optional[str])

slots.pictureWidth = Slot(uri=UCO_OBSERVABLE.pictureWidth, name="pictureWidth", curie=UCO_OBSERVABLE.curie('pictureWidth'),
                   model_uri=UCO_LINKML.pictureWidth, domain=None, range=Optional[int])

slots.pid = Slot(uri=UCO_OBSERVABLE.pid, name="pid", curie=UCO_OBSERVABLE.curie('pid'),
                   model_uri=UCO_LINKML.pid, domain=None, range=Optional[int])

slots.pointerToSymbolTable = Slot(uri=UCO_OBSERVABLE.pointerToSymbolTable, name="pointerToSymbolTable", curie=UCO_OBSERVABLE.curie('pointerToSymbolTable'),
                   model_uri=UCO_LINKML.pointerToSymbolTable, domain=None, range=Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]])

slots.policyConstraints = Slot(uri=UCO_OBSERVABLE.policyConstraints, name="policyConstraints", curie=UCO_OBSERVABLE.curie('policyConstraints'),
                   model_uri=UCO_LINKML.policyConstraints, domain=None, range=Optional[str])

slots.policyMappings = Slot(uri=UCO_OBSERVABLE.policyMappings, name="policyMappings", curie=UCO_OBSERVABLE.curie('policyMappings'),
                   model_uri=UCO_LINKML.policyMappings, domain=None, range=Optional[str])

slots.port = Slot(uri=UCO_OBSERVABLE.port, name="port", curie=UCO_OBSERVABLE.curie('port'),
                   model_uri=UCO_LINKML.port, domain=None, range=Optional[int])

slots.prefetchHash = Slot(uri=UCO_OBSERVABLE.prefetchHash, name="prefetchHash", curie=UCO_OBSERVABLE.curie('prefetchHash'),
                   model_uri=UCO_LINKML.prefetchHash, domain=None, range=Optional[str])

slots.priority = Slot(uri=UCO_OBSERVABLE.priority, name="priority", curie=UCO_OBSERVABLE.curie('priority'),
                   model_uri=UCO_LINKML.priority, domain=None, range=Optional[str])

slots.privateKeyUsagePeriodNotAfter = Slot(uri=UCO_OBSERVABLE.privateKeyUsagePeriodNotAfter, name="privateKeyUsagePeriodNotAfter", curie=UCO_OBSERVABLE.curie('privateKeyUsagePeriodNotAfter'),
                   model_uri=UCO_LINKML.privateKeyUsagePeriodNotAfter, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.privateKeyUsagePeriodNotBefore = Slot(uri=UCO_OBSERVABLE.privateKeyUsagePeriodNotBefore, name="privateKeyUsagePeriodNotBefore", curie=UCO_OBSERVABLE.curie('privateKeyUsagePeriodNotBefore'),
                   model_uri=UCO_LINKML.privateKeyUsagePeriodNotBefore, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.processorArchitecture = Slot(uri=UCO_OBSERVABLE.processorArchitecture, name="processorArchitecture", curie=UCO_OBSERVABLE.curie('processorArchitecture'),
                   model_uri=UCO_LINKML.processorArchitecture, domain=None, range=Optional[str])

slots.profile = Slot(uri=UCO_OBSERVABLE.profile, name="profile", curie=UCO_OBSERVABLE.curie('profile'),
                   model_uri=UCO_LINKML.profile, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.profileAccount = Slot(uri=UCO_OBSERVABLE.profileAccount, name="profileAccount", curie=UCO_OBSERVABLE.curie('profileAccount'),
                   model_uri=UCO_LINKML.profileAccount, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.profileBackgroundHash = Slot(uri=UCO_OBSERVABLE.profileBackgroundHash, name="profileBackgroundHash", curie=UCO_OBSERVABLE.curie('profileBackgroundHash'),
                   model_uri=UCO_LINKML.profileBackgroundHash, domain=None, range=Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]])

slots.profileBackgroundLocation = Slot(uri=UCO_OBSERVABLE.profileBackgroundLocation, name="profileBackgroundLocation", curie=UCO_OBSERVABLE.curie('profileBackgroundLocation'),
                   model_uri=UCO_LINKML.profileBackgroundLocation, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.profileBannerHash = Slot(uri=UCO_OBSERVABLE.profileBannerHash, name="profileBannerHash", curie=UCO_OBSERVABLE.curie('profileBannerHash'),
                   model_uri=UCO_LINKML.profileBannerHash, domain=None, range=Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]])

slots.profileBannerLocation = Slot(uri=UCO_OBSERVABLE.profileBannerLocation, name="profileBannerLocation", curie=UCO_OBSERVABLE.curie('profileBannerLocation'),
                   model_uri=UCO_LINKML.profileBannerLocation, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.profileCreated = Slot(uri=UCO_OBSERVABLE.profileCreated, name="profileCreated", curie=UCO_OBSERVABLE.curie('profileCreated'),
                   model_uri=UCO_LINKML.profileCreated, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.profileIdentity = Slot(uri=UCO_OBSERVABLE.profileIdentity, name="profileIdentity", curie=UCO_OBSERVABLE.curie('profileIdentity'),
                   model_uri=UCO_LINKML.profileIdentity, domain=None, range=Optional[Union[str, IdentityId]])

slots.profileImageHash = Slot(uri=UCO_OBSERVABLE.profileImageHash, name="profileImageHash", curie=UCO_OBSERVABLE.curie('profileImageHash'),
                   model_uri=UCO_LINKML.profileImageHash, domain=None, range=Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]])

slots.profileImageLocation = Slot(uri=UCO_OBSERVABLE.profileImageLocation, name="profileImageLocation", curie=UCO_OBSERVABLE.curie('profileImageLocation'),
                   model_uri=UCO_LINKML.profileImageLocation, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.profileIsProtected = Slot(uri=UCO_OBSERVABLE.profileIsProtected, name="profileIsProtected", curie=UCO_OBSERVABLE.curie('profileIsProtected'),
                   model_uri=UCO_LINKML.profileIsProtected, domain=None, range=Optional[Union[bool, Bool]])

slots.profileIsVerified = Slot(uri=UCO_OBSERVABLE.profileIsVerified, name="profileIsVerified", curie=UCO_OBSERVABLE.curie('profileIsVerified'),
                   model_uri=UCO_LINKML.profileIsVerified, domain=None, range=Optional[Union[bool, Bool]])

slots.profileLanguage = Slot(uri=UCO_OBSERVABLE.profileLanguage, name="profileLanguage", curie=UCO_OBSERVABLE.curie('profileLanguage'),
                   model_uri=UCO_LINKML.profileLanguage, domain=None, range=Optional[Union[str, list[str]]])

slots.profileService = Slot(uri=UCO_OBSERVABLE.profileService, name="profileService", curie=UCO_OBSERVABLE.curie('profileService'),
                   model_uri=UCO_LINKML.profileService, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.profileWebsite = Slot(uri=UCO_OBSERVABLE.profileWebsite, name="profileWebsite", curie=UCO_OBSERVABLE.curie('profileWebsite'),
                   model_uri=UCO_LINKML.profileWebsite, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.properties = Slot(uri=UCO_OBSERVABLE.properties, name="properties", curie=UCO_OBSERVABLE.curie('properties'),
                   model_uri=UCO_LINKML.properties, domain=None, range=Optional[str])

slots.propertyName = Slot(uri=UCO_OBSERVABLE.propertyName, name="propertyName", curie=UCO_OBSERVABLE.curie('propertyName'),
                   model_uri=UCO_LINKML.propertyName, domain=None, range=Optional[str])

slots.protocols = Slot(uri=UCO_OBSERVABLE.protocols, name="protocols", curie=UCO_OBSERVABLE.curie('protocols'),
                   model_uri=UCO_LINKML.protocols, domain=None, range=Optional[Union[dict, ControlledDictionary]])

slots.query = Slot(uri=UCO_OBSERVABLE.query, name="query", curie=UCO_OBSERVABLE.curie('query'),
                   model_uri=UCO_LINKML.query, domain=None, range=Optional[str])

slots.rangeOffset = Slot(uri=UCO_OBSERVABLE.rangeOffset, name="rangeOffset", curie=UCO_OBSERVABLE.curie('rangeOffset'),
                   model_uri=UCO_LINKML.rangeOffset, domain=None, range=Optional[int])

slots.rangeOffsetType = Slot(uri=UCO_OBSERVABLE.rangeOffsetType, name="rangeOffsetType", curie=UCO_OBSERVABLE.curie('rangeOffsetType'),
                   model_uri=UCO_LINKML.rangeOffsetType, domain=None, range=Optional[str])

slots.rangeSize = Slot(uri=UCO_OBSERVABLE.rangeSize, name="rangeSize", curie=UCO_OBSERVABLE.curie('rangeSize'),
                   model_uri=UCO_LINKML.rangeSize, domain=None, range=Optional[int])

slots.receivedLines = Slot(uri=UCO_OBSERVABLE.receivedLines, name="receivedLines", curie=UCO_OBSERVABLE.curie('receivedLines'),
                   model_uri=UCO_LINKML.receivedLines, domain=None, range=Optional[Union[str, list[str]]])

slots.receivedTime = Slot(uri=UCO_OBSERVABLE.receivedTime, name="receivedTime", curie=UCO_OBSERVABLE.curie('receivedTime'),
                   model_uri=UCO_LINKML.receivedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.recordFieldIsNull = Slot(uri=UCO_OBSERVABLE.recordFieldIsNull, name="recordFieldIsNull", curie=UCO_OBSERVABLE.curie('recordFieldIsNull'),
                   model_uri=UCO_LINKML.recordFieldIsNull, domain=None, range=Optional[Union[bool, Bool]])

slots.recordFieldName = Slot(uri=UCO_OBSERVABLE.recordFieldName, name="recordFieldName", curie=UCO_OBSERVABLE.curie('recordFieldName'),
                   model_uri=UCO_LINKML.recordFieldName, domain=None, range=Optional[str])

slots.recordFieldValue = Slot(uri=UCO_OBSERVABLE.recordFieldValue, name="recordFieldValue", curie=UCO_OBSERVABLE.curie('recordFieldValue'),
                   model_uri=UCO_LINKML.recordFieldValue, domain=None, range=Optional[Union[str, UcoBase64Binary, Decimal, int]])

slots.recordRowID = Slot(uri=UCO_OBSERVABLE.recordRowID, name="recordRowID", curie=UCO_OBSERVABLE.curie('recordRowID'),
                   model_uri=UCO_LINKML.recordRowID, domain=None, range=Optional[Union[int, str]])

slots.recurrence = Slot(uri=UCO_OBSERVABLE.recurrence, name="recurrence", curie=UCO_OBSERVABLE.curie('recurrence'),
                   model_uri=UCO_LINKML.recurrence, domain=None, range=Optional[str])

slots.referralURL = Slot(uri=UCO_OBSERVABLE.referralURL, name="referralURL", curie=UCO_OBSERVABLE.curie('referralURL'),
                   model_uri=UCO_LINKML.referralURL, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.referrerUrl = Slot(uri=UCO_OBSERVABLE.referrerUrl, name="referrerUrl", curie=UCO_OBSERVABLE.curie('referrerUrl'),
                   model_uri=UCO_LINKML.referrerUrl, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.regionEndAddress = Slot(uri=UCO_OBSERVABLE.regionEndAddress, name="regionEndAddress", curie=UCO_OBSERVABLE.curie('regionEndAddress'),
                   model_uri=UCO_LINKML.regionEndAddress, domain=None, range=Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]])

slots.regionSize = Slot(uri=UCO_OBSERVABLE.regionSize, name="regionSize", curie=UCO_OBSERVABLE.curie('regionSize'),
                   model_uri=UCO_LINKML.regionSize, domain=None, range=Optional[int])

slots.regionStartAddress = Slot(uri=UCO_OBSERVABLE.regionStartAddress, name="regionStartAddress", curie=UCO_OBSERVABLE.curie('regionStartAddress'),
                   model_uri=UCO_LINKML.regionStartAddress, domain=None, range=Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]])

slots.regionalInternetRegistry = Slot(uri=UCO_OBSERVABLE.regionalInternetRegistry, name="regionalInternetRegistry", curie=UCO_OBSERVABLE.curie('regionalInternetRegistry'),
                   model_uri=UCO_LINKML.regionalInternetRegistry, domain=None, range=Optional[Union[str, "RegionalRegistryTypeVocab"]])

slots.registeredOrganization = Slot(uri=UCO_OBSERVABLE.registeredOrganization, name="registeredOrganization", curie=UCO_OBSERVABLE.curie('registeredOrganization'),
                   model_uri=UCO_LINKML.registeredOrganization, domain=None, range=Optional[Union[str, IdentityId]])

slots.registeredOwner = Slot(uri=UCO_OBSERVABLE.registeredOwner, name="registeredOwner", curie=UCO_OBSERVABLE.curie('registeredOwner'),
                   model_uri=UCO_LINKML.registeredOwner, domain=None, range=Optional[Union[str, IdentityId]])

slots.registrantContactInfo = Slot(uri=UCO_OBSERVABLE.registrantContactInfo, name="registrantContactInfo", curie=UCO_OBSERVABLE.curie('registrantContactInfo'),
                   model_uri=UCO_LINKML.registrantContactInfo, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.registrantIDs = Slot(uri=UCO_OBSERVABLE.registrantIDs, name="registrantIDs", curie=UCO_OBSERVABLE.curie('registrantIDs'),
                   model_uri=UCO_LINKML.registrantIDs, domain=None, range=Optional[Union[str, list[str]]])

slots.registrarGUID = Slot(uri=UCO_OBSERVABLE.registrarGUID, name="registrarGUID", curie=UCO_OBSERVABLE.curie('registrarGUID'),
                   model_uri=UCO_LINKML.registrarGUID, domain=None, range=Optional[str])

slots.registrarID = Slot(uri=UCO_OBSERVABLE.registrarID, name="registrarID", curie=UCO_OBSERVABLE.curie('registrarID'),
                   model_uri=UCO_LINKML.registrarID, domain=None, range=Optional[str])

slots.registrarInfo = Slot(uri=UCO_OBSERVABLE.registrarInfo, name="registrarInfo", curie=UCO_OBSERVABLE.curie('registrarInfo'),
                   model_uri=UCO_LINKML.registrarInfo, domain=None, range=Optional[Union[dict, WhoisRegistrarInfoType]])

slots.registrarName = Slot(uri=UCO_OBSERVABLE.registrarName, name="registrarName", curie=UCO_OBSERVABLE.curie('registrarName'),
                   model_uri=UCO_LINKML.registrarName, domain=None, range=Optional[str])

slots.registryValues = Slot(uri=UCO_OBSERVABLE.registryValues, name="registryValues", curie=UCO_OBSERVABLE.curie('registryValues'),
                   model_uri=UCO_LINKML.registryValues, domain=None, range=Optional[Union[Union[dict, WindowsRegistryValue], list[Union[dict, WindowsRegistryValue]]]])

slots.remarks = Slot(uri=UCO_OBSERVABLE.remarks, name="remarks", curie=UCO_OBSERVABLE.curie('remarks'),
                   model_uri=UCO_LINKML.remarks, domain=None, range=Optional[str])

slots.remindTime = Slot(uri=UCO_OBSERVABLE.remindTime, name="remindTime", curie=UCO_OBSERVABLE.curie('remindTime'),
                   model_uri=UCO_LINKML.remindTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.requestMethod = Slot(uri=UCO_OBSERVABLE.requestMethod, name="requestMethod", curie=UCO_OBSERVABLE.curie('requestMethod'),
                   model_uri=UCO_LINKML.requestMethod, domain=None, range=Optional[str])

slots.requestValue = Slot(uri=UCO_OBSERVABLE.requestValue, name="requestValue", curie=UCO_OBSERVABLE.curie('requestValue'),
                   model_uri=UCO_LINKML.requestValue, domain=None, range=Optional[str])

slots.requestVersion = Slot(uri=UCO_OBSERVABLE.requestVersion, name="requestVersion", curie=UCO_OBSERVABLE.curie('requestVersion'),
                   model_uri=UCO_LINKML.requestVersion, domain=None, range=Optional[str])

slots.rowCondition = Slot(uri=UCO_OBSERVABLE.rowCondition, name="rowCondition", curie=UCO_OBSERVABLE.curie('rowCondition'),
                   model_uri=UCO_LINKML.rowCondition, domain=None, range=Optional[str])

slots.rowIndex = Slot(uri=UCO_OBSERVABLE.rowIndex, name="rowIndex", curie=UCO_OBSERVABLE.curie('rowIndex'),
                   model_uri=UCO_LINKML.rowIndex, domain=None, range=Optional[Union[Union[int, UcoPositiveInteger], list[Union[int, UcoPositiveInteger]]]])

slots.ruid = Slot(uri=UCO_OBSERVABLE.ruid, name="ruid", curie=UCO_OBSERVABLE.curie('ruid'),
                   model_uri=UCO_LINKML.ruid, domain=None, range=Optional[Union[Union[int, UcoNonNegativeInteger], list[Union[int, UcoNonNegativeInteger]]]])

slots.runningStatus = Slot(uri=UCO_OBSERVABLE.runningStatus, name="runningStatus", curie=UCO_OBSERVABLE.curie('runningStatus'),
                   model_uri=UCO_LINKML.runningStatus, domain=None, range=Optional[str])

slots.scheme = Slot(uri=UCO_OBSERVABLE.scheme, name="scheme", curie=UCO_OBSERVABLE.curie('scheme'),
                   model_uri=UCO_LINKML.scheme, domain=None, range=Optional[str])

slots.sectionAlignment = Slot(uri=UCO_OBSERVABLE.sectionAlignment, name="sectionAlignment", curie=UCO_OBSERVABLE.curie('sectionAlignment'),
                   model_uri=UCO_LINKML.sectionAlignment, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.sections = Slot(uri=UCO_OBSERVABLE.sections, name="sections", curie=UCO_OBSERVABLE.curie('sections'),
                   model_uri=UCO_LINKML.sections, domain=None, range=Optional[Union[Union[dict, WindowsPESection], list[Union[dict, WindowsPESection]]]])

slots.sectorSize = Slot(uri=UCO_OBSERVABLE.sectorSize, name="sectorSize", curie=UCO_OBSERVABLE.curie('sectorSize'),
                   model_uri=UCO_LINKML.sectorSize, domain=None, range=Optional[int])

slots.securityAttributes = Slot(uri=UCO_OBSERVABLE.securityAttributes, name="securityAttributes", curie=UCO_OBSERVABLE.curie('securityAttributes'),
                   model_uri=UCO_LINKML.securityAttributes, domain=None, range=Optional[str])

slots.sender = Slot(uri=UCO_OBSERVABLE.sender, name="sender", curie=UCO_OBSERVABLE.curie('sender'),
                   model_uri=UCO_LINKML.sender, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.sentTime = Slot(uri=UCO_OBSERVABLE.sentTime, name="sentTime", curie=UCO_OBSERVABLE.curie('sentTime'),
                   model_uri=UCO_LINKML.sentTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.serialNumber = Slot(uri=UCO_OBSERVABLE.serialNumber, name="serialNumber", curie=UCO_OBSERVABLE.curie('serialNumber'),
                   model_uri=UCO_LINKML.serialNumber, domain=None, range=Optional[str])

slots.serverName = Slot(uri=UCO_OBSERVABLE.serverName, name="serverName", curie=UCO_OBSERVABLE.curie('serverName'),
                   model_uri=UCO_LINKML.serverName, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.serviceName = Slot(uri=UCO_OBSERVABLE.serviceName, name="serviceName", curie=UCO_OBSERVABLE.curie('serviceName'),
                   model_uri=UCO_LINKML.serviceName, domain=None, range=Optional[str])

slots.serviceStatus = Slot(uri=UCO_OBSERVABLE.serviceStatus, name="serviceStatus", curie=UCO_OBSERVABLE.curie('serviceStatus'),
                   model_uri=UCO_LINKML.serviceStatus, domain=None, range=Optional[str])

slots.serviceType = Slot(uri=UCO_OBSERVABLE.serviceType, name="serviceType", curie=UCO_OBSERVABLE.curie('serviceType'),
                   model_uri=UCO_LINKML.serviceType, domain=None, range=Optional[str])

slots.sessionID = Slot(uri=UCO_OBSERVABLE.sessionID, name="sessionID", curie=UCO_OBSERVABLE.curie('sessionID'),
                   model_uri=UCO_LINKML.sessionID, domain=None, range=Optional[str])

slots.shell = Slot(uri=UCO_OBSERVABLE.shell, name="shell", curie=UCO_OBSERVABLE.curie('shell'),
                   model_uri=UCO_LINKML.shell, domain=None, range=Optional[str])

slots.showMessageBody = Slot(uri=UCO_OBSERVABLE.showMessageBody, name="showMessageBody", curie=UCO_OBSERVABLE.curie('showMessageBody'),
                   model_uri=UCO_LINKML.showMessageBody, domain=None, range=Optional[str])

slots.showMessageTitle = Slot(uri=UCO_OBSERVABLE.showMessageTitle, name="showMessageTitle", curie=UCO_OBSERVABLE.curie('showMessageTitle'),
                   model_uri=UCO_LINKML.showMessageTitle, domain=None, range=Optional[str])

slots.sid = Slot(uri=UCO_OBSERVABLE.sid, name="sid", curie=UCO_OBSERVABLE.curie('sid'),
                   model_uri=UCO_LINKML.sid, domain=None, range=Optional[str])

slots.signalStrength = Slot(uri=UCO_OBSERVABLE.signalStrength, name="signalStrength", curie=UCO_OBSERVABLE.curie('signalStrength'),
                   model_uri=UCO_LINKML.signalStrength, domain=None, range=Optional[Decimal])

slots.signature = Slot(uri=UCO_OBSERVABLE.signature, name="signature", curie=UCO_OBSERVABLE.curie('signature'),
                   model_uri=UCO_LINKML.signature, domain=None, range=Optional[str])

slots.signatureAlgorithm = Slot(uri=UCO_OBSERVABLE.signatureAlgorithm, name="signatureAlgorithm", curie=UCO_OBSERVABLE.curie('signatureAlgorithm'),
                   model_uri=UCO_LINKML.signatureAlgorithm, domain=None, range=Optional[str])

slots.signatureDescription = Slot(uri=UCO_OBSERVABLE.signatureDescription, name="signatureDescription", curie=UCO_OBSERVABLE.curie('signatureDescription'),
                   model_uri=UCO_LINKML.signatureDescription, domain=None, range=Optional[str])

slots.signatureExists = Slot(uri=UCO_OBSERVABLE.signatureExists, name="signatureExists", curie=UCO_OBSERVABLE.curie('signatureExists'),
                   model_uri=UCO_LINKML.signatureExists, domain=None, range=Optional[Union[bool, Bool]])

slots.signatureVerified = Slot(uri=UCO_OBSERVABLE.signatureVerified, name="signatureVerified", curie=UCO_OBSERVABLE.curie('signatureVerified'),
                   model_uri=UCO_LINKML.signatureVerified, domain=None, range=Optional[Union[bool, Bool]])

slots.sipAddress = Slot(uri=UCO_OBSERVABLE.sipAddress, name="sipAddress", curie=UCO_OBSERVABLE.curie('sipAddress'),
                   model_uri=UCO_LINKML.sipAddress, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.size = Slot(uri=UCO_OBSERVABLE.size, name="size", curie=UCO_OBSERVABLE.curie('size'),
                   model_uri=UCO_LINKML.size, domain=None, range=Optional[int])

slots.sizeInBytes = Slot(uri=UCO_OBSERVABLE.sizeInBytes, name="sizeInBytes", curie=UCO_OBSERVABLE.curie('sizeInBytes'),
                   model_uri=UCO_LINKML.sizeInBytes, domain=None, range=Optional[int])

slots.sizeOfCode = Slot(uri=UCO_OBSERVABLE.sizeOfCode, name="sizeOfCode", curie=UCO_OBSERVABLE.curie('sizeOfCode'),
                   model_uri=UCO_LINKML.sizeOfCode, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.sizeOfHeaders = Slot(uri=UCO_OBSERVABLE.sizeOfHeaders, name="sizeOfHeaders", curie=UCO_OBSERVABLE.curie('sizeOfHeaders'),
                   model_uri=UCO_LINKML.sizeOfHeaders, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.sizeOfHeapCommit = Slot(uri=UCO_OBSERVABLE.sizeOfHeapCommit, name="sizeOfHeapCommit", curie=UCO_OBSERVABLE.curie('sizeOfHeapCommit'),
                   model_uri=UCO_LINKML.sizeOfHeapCommit, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.sizeOfHeapReserve = Slot(uri=UCO_OBSERVABLE.sizeOfHeapReserve, name="sizeOfHeapReserve", curie=UCO_OBSERVABLE.curie('sizeOfHeapReserve'),
                   model_uri=UCO_LINKML.sizeOfHeapReserve, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.sizeOfImage = Slot(uri=UCO_OBSERVABLE.sizeOfImage, name="sizeOfImage", curie=UCO_OBSERVABLE.curie('sizeOfImage'),
                   model_uri=UCO_LINKML.sizeOfImage, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.sizeOfInitializedData = Slot(uri=UCO_OBSERVABLE.sizeOfInitializedData, name="sizeOfInitializedData", curie=UCO_OBSERVABLE.curie('sizeOfInitializedData'),
                   model_uri=UCO_LINKML.sizeOfInitializedData, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.sizeOfOptionalHeader = Slot(uri=UCO_OBSERVABLE.sizeOfOptionalHeader, name="sizeOfOptionalHeader", curie=UCO_OBSERVABLE.curie('sizeOfOptionalHeader'),
                   model_uri=UCO_LINKML.sizeOfOptionalHeader, domain=None, range=Optional[int])

slots.sizeOfStackCommit = Slot(uri=UCO_OBSERVABLE.sizeOfStackCommit, name="sizeOfStackCommit", curie=UCO_OBSERVABLE.curie('sizeOfStackCommit'),
                   model_uri=UCO_LINKML.sizeOfStackCommit, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.sizeOfStackReserve = Slot(uri=UCO_OBSERVABLE.sizeOfStackReserve, name="sizeOfStackReserve", curie=UCO_OBSERVABLE.curie('sizeOfStackReserve'),
                   model_uri=UCO_LINKML.sizeOfStackReserve, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.sizeOfUninitializedData = Slot(uri=UCO_OBSERVABLE.sizeOfUninitializedData, name="sizeOfUninitializedData", curie=UCO_OBSERVABLE.curie('sizeOfUninitializedData'),
                   model_uri=UCO_LINKML.sizeOfUninitializedData, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.skew = Slot(uri=UCO_OBSERVABLE.skew, name="skew", curie=UCO_OBSERVABLE.curie('skew'),
                   model_uri=UCO_LINKML.skew, domain=None, range=Optional[Decimal])

slots.sourceApplication = Slot(uri=UCO_OBSERVABLE.sourceApplication, name="sourceApplication", curie=UCO_OBSERVABLE.curie('sourceApplication'),
                   model_uri=UCO_LINKML.sourceApplication, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.sourceFlags = Slot(uri=UCO_OBSERVABLE.sourceFlags, name="sourceFlags", curie=UCO_OBSERVABLE.curie('sourceFlags'),
                   model_uri=UCO_LINKML.sourceFlags, domain=None, range=Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]])

slots.sourcePort = Slot(uri=UCO_OBSERVABLE.sourcePort, name="sourcePort", curie=UCO_OBSERVABLE.curie('sourcePort'),
                   model_uri=UCO_LINKML.sourcePort, domain=None, range=Optional[int])

slots.spaceLeft = Slot(uri=UCO_OBSERVABLE.spaceLeft, name="spaceLeft", curie=UCO_OBSERVABLE.curie('spaceLeft'),
                   model_uri=UCO_LINKML.spaceLeft, domain=None, range=Optional[int])

slots.spaceUsed = Slot(uri=UCO_OBSERVABLE.spaceUsed, name="spaceUsed", curie=UCO_OBSERVABLE.curie('spaceUsed'),
                   model_uri=UCO_LINKML.spaceUsed, domain=None, range=Optional[int])

slots.sponsoringRegistrar = Slot(uri=UCO_OBSERVABLE.sponsoringRegistrar, name="sponsoringRegistrar", curie=UCO_OBSERVABLE.curie('sponsoringRegistrar'),
                   model_uri=UCO_LINKML.sponsoringRegistrar, domain=None, range=Optional[str])

slots.src = Slot(uri=UCO_OBSERVABLE.src, name="src", curie=UCO_OBSERVABLE.curie('src'),
                   model_uri=UCO_LINKML.src, domain=None, range=Optional[Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]]])

slots.srcBytes = Slot(uri=UCO_OBSERVABLE.srcBytes, name="srcBytes", curie=UCO_OBSERVABLE.curie('srcBytes'),
                   model_uri=UCO_LINKML.srcBytes, domain=None, range=Optional[int])

slots.srcPackets = Slot(uri=UCO_OBSERVABLE.srcPackets, name="srcPackets", curie=UCO_OBSERVABLE.curie('srcPackets'),
                   model_uri=UCO_LINKML.srcPackets, domain=None, range=Optional[int])

slots.srcPayload = Slot(uri=UCO_OBSERVABLE.srcPayload, name="srcPayload", curie=UCO_OBSERVABLE.curie('srcPayload'),
                   model_uri=UCO_LINKML.srcPayload, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.ssid = Slot(uri=UCO_OBSERVABLE.ssid, name="ssid", curie=UCO_OBSERVABLE.curie('ssid'),
                   model_uri=UCO_LINKML.ssid, domain=None, range=Optional[str])

slots.stackSize = Slot(uri=UCO_OBSERVABLE.stackSize, name="stackSize", curie=UCO_OBSERVABLE.curie('stackSize'),
                   model_uri=UCO_LINKML.stackSize, domain=None, range=Optional[Union[Union[int, UcoNonNegativeInteger], list[Union[int, UcoNonNegativeInteger]]]])

slots.startAddress = Slot(uri=UCO_OBSERVABLE.startAddress, name="startAddress", curie=UCO_OBSERVABLE.curie('startAddress'),
                   model_uri=UCO_LINKML.startAddress, domain=None, range=Optional[Union[Union[str, UcoHexBinary], list[Union[str, UcoHexBinary]]]])

slots.startCommandLine = Slot(uri=UCO_OBSERVABLE.startCommandLine, name="startCommandLine", curie=UCO_OBSERVABLE.curie('startCommandLine'),
                   model_uri=UCO_LINKML.startCommandLine, domain=None, range=Optional[str])

slots.startType = Slot(uri=UCO_OBSERVABLE.startType, name="startType", curie=UCO_OBSERVABLE.curie('startType'),
                   model_uri=UCO_LINKML.startType, domain=None, range=Optional[str])

slots.startupInfo = Slot(uri=UCO_OBSERVABLE.startupInfo, name="startupInfo", curie=UCO_OBSERVABLE.curie('startupInfo'),
                   model_uri=UCO_LINKML.startupInfo, domain=None, range=Optional[Union[dict, Dictionary]])

slots.state = Slot(uri=UCO_OBSERVABLE.state, name="state", curie=UCO_OBSERVABLE.curie('state'),
                   model_uri=UCO_LINKML.state, domain=None, range=Optional[str])

slots.status = Slot(uri=UCO_OBSERVABLE.status, name="status", curie=UCO_OBSERVABLE.curie('status'),
                   model_uri=UCO_LINKML.status, domain=None, range=Optional[str])

slots.statusesCount = Slot(uri=UCO_OBSERVABLE.statusesCount, name="statusesCount", curie=UCO_OBSERVABLE.curie('statusesCount'),
                   model_uri=UCO_LINKML.statusesCount, domain=None, range=Optional[Union[int, UcoNonNegativeInteger]])

slots.storageCapacityInBytes = Slot(uri=UCO_OBSERVABLE.storageCapacityInBytes, name="storageCapacityInBytes", curie=UCO_OBSERVABLE.curie('storageCapacityInBytes'),
                   model_uri=UCO_LINKML.storageCapacityInBytes, domain=None, range=Optional[int])

slots.stringValue = Slot(uri=UCO_OBSERVABLE.stringValue, name="stringValue", curie=UCO_OBSERVABLE.curie('stringValue'),
                   model_uri=UCO_LINKML.stringValue, domain=None, range=Optional[str])

slots.strings = Slot(uri=UCO_OBSERVABLE.strings, name="strings", curie=UCO_OBSERVABLE.curie('strings'),
                   model_uri=UCO_LINKML.strings, domain=None, range=Optional[Union[Union[dict, ExtractedString], list[Union[dict, ExtractedString]]]])

slots.subject = Slot(uri=UCO_OBSERVABLE.subject, name="subject", curie=UCO_OBSERVABLE.curie('subject'),
                   model_uri=UCO_LINKML.subject, domain=None, range=Optional[str])

slots.subjectAlternativeName = Slot(uri=UCO_OBSERVABLE.subjectAlternativeName, name="subjectAlternativeName", curie=UCO_OBSERVABLE.curie('subjectAlternativeName'),
                   model_uri=UCO_LINKML.subjectAlternativeName, domain=None, range=Optional[str])

slots.subjectDirectoryAttributes = Slot(uri=UCO_OBSERVABLE.subjectDirectoryAttributes, name="subjectDirectoryAttributes", curie=UCO_OBSERVABLE.curie('subjectDirectoryAttributes'),
                   model_uri=UCO_LINKML.subjectDirectoryAttributes, domain=None, range=Optional[str])

slots.subjectHash = Slot(uri=UCO_OBSERVABLE.subjectHash, name="subjectHash", curie=UCO_OBSERVABLE.curie('subjectHash'),
                   model_uri=UCO_LINKML.subjectHash, domain=None, range=Optional[Union[dict, Hash]])

slots.subjectKeyIdentifier = Slot(uri=UCO_OBSERVABLE.subjectKeyIdentifier, name="subjectKeyIdentifier", curie=UCO_OBSERVABLE.curie('subjectKeyIdentifier'),
                   model_uri=UCO_LINKML.subjectKeyIdentifier, domain=None, range=Optional[str])

slots.subjectPublicKeyAlgorithm = Slot(uri=UCO_OBSERVABLE.subjectPublicKeyAlgorithm, name="subjectPublicKeyAlgorithm", curie=UCO_OBSERVABLE.curie('subjectPublicKeyAlgorithm'),
                   model_uri=UCO_LINKML.subjectPublicKeyAlgorithm, domain=None, range=Optional[str])

slots.subjectPublicKeyExponent = Slot(uri=UCO_OBSERVABLE.subjectPublicKeyExponent, name="subjectPublicKeyExponent", curie=UCO_OBSERVABLE.curie('subjectPublicKeyExponent'),
                   model_uri=UCO_LINKML.subjectPublicKeyExponent, domain=None, range=Optional[int])

slots.subjectPublicKeyModulus = Slot(uri=UCO_OBSERVABLE.subjectPublicKeyModulus, name="subjectPublicKeyModulus", curie=UCO_OBSERVABLE.curie('subjectPublicKeyModulus'),
                   model_uri=UCO_LINKML.subjectPublicKeyModulus, domain=None, range=Optional[str])

slots.subsystem = Slot(uri=UCO_OBSERVABLE.subsystem, name="subsystem", curie=UCO_OBSERVABLE.curie('subsystem'),
                   model_uri=UCO_LINKML.subsystem, domain=None, range=Optional[Union[Union[int, UcoUnsignedShort], list[Union[int, UcoUnsignedShort]]]])

slots.symbolicName = Slot(uri=UCO_OBSERVABLE.symbolicName, name="symbolicName", curie=UCO_OBSERVABLE.curie('symbolicName'),
                   model_uri=UCO_LINKML.symbolicName, domain=None, range=Optional[str])

slots.systemTime = Slot(uri=UCO_OBSERVABLE.systemTime, name="systemTime", curie=UCO_OBSERVABLE.curie('systemTime'),
                   model_uri=UCO_LINKML.systemTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.tableName = Slot(uri=UCO_OBSERVABLE.tableName, name="tableName", curie=UCO_OBSERVABLE.curie('tableName'),
                   model_uri=UCO_LINKML.tableName, domain=None, range=Optional[str])

slots.tableSchema = Slot(uri=UCO_OBSERVABLE.tableSchema, name="tableSchema", curie=UCO_OBSERVABLE.curie('tableSchema'),
                   model_uri=UCO_LINKML.tableSchema, domain=None, range=Optional[str])

slots.targetFile = Slot(uri=UCO_OBSERVABLE.targetFile, name="targetFile", curie=UCO_OBSERVABLE.curie('targetFile'),
                   model_uri=UCO_LINKML.targetFile, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.taskComment = Slot(uri=UCO_OBSERVABLE.taskComment, name="taskComment", curie=UCO_OBSERVABLE.curie('taskComment'),
                   model_uri=UCO_LINKML.taskComment, domain=None, range=Optional[str])

slots.taskCreator = Slot(uri=UCO_OBSERVABLE.taskCreator, name="taskCreator", curie=UCO_OBSERVABLE.curie('taskCreator'),
                   model_uri=UCO_LINKML.taskCreator, domain=None, range=Optional[str])

slots.text = Slot(uri=UCO_OBSERVABLE.text, name="text", curie=UCO_OBSERVABLE.curie('text'),
                   model_uri=UCO_LINKML.text, domain=None, range=Optional[str])

slots.threadID = Slot(uri=UCO_OBSERVABLE.threadID, name="threadID", curie=UCO_OBSERVABLE.curie('threadID'),
                   model_uri=UCO_LINKML.threadID, domain=None, range=Optional[Union[Union[int, UcoNonNegativeInteger], list[Union[int, UcoNonNegativeInteger]]]])

slots.thumbprintHash = Slot(uri=UCO_OBSERVABLE.thumbprintHash, name="thumbprintHash", curie=UCO_OBSERVABLE.curie('thumbprintHash'),
                   model_uri=UCO_LINKML.thumbprintHash, domain=None, range=Optional[Union[dict, Hash]])

slots.timeDateStamp = Slot(uri=UCO_OBSERVABLE.timeDateStamp, name="timeDateStamp", curie=UCO_OBSERVABLE.curie('timeDateStamp'),
                   model_uri=UCO_LINKML.timeDateStamp, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.timesExecuted = Slot(uri=UCO_OBSERVABLE.timesExecuted, name="timesExecuted", curie=UCO_OBSERVABLE.curie('timesExecuted'),
                   model_uri=UCO_LINKML.timesExecuted, domain=None, range=Optional[int])

slots.timezoneDST = Slot(uri=UCO_OBSERVABLE.timezoneDST, name="timezoneDST", curie=UCO_OBSERVABLE.curie('timezoneDST'),
                   model_uri=UCO_LINKML.timezoneDST, domain=None, range=Optional[str])

slots.timezoneStandard = Slot(uri=UCO_OBSERVABLE.timezoneStandard, name="timezoneStandard", curie=UCO_OBSERVABLE.curie('timezoneStandard'),
                   model_uri=UCO_LINKML.timezoneStandard, domain=None, range=Optional[str])

slots.to = Slot(uri=UCO_OBSERVABLE.to, name="to", curie=UCO_OBSERVABLE.curie('to'),
                   model_uri=UCO_LINKML.to, domain=None, range=Optional[Union[Union[str, ObservableObjectId], list[Union[str, ObservableObjectId]]]])

slots.totalFragments = Slot(uri=UCO_OBSERVABLE.totalFragments, name="totalFragments", curie=UCO_OBSERVABLE.curie('totalFragments'),
                   model_uri=UCO_LINKML.totalFragments, domain=None, range=Optional[Union[int, list[int]]])

slots.totalRam = Slot(uri=UCO_OBSERVABLE.totalRam, name="totalRam", curie=UCO_OBSERVABLE.curie('totalRam'),
                   model_uri=UCO_LINKML.totalRam, domain=None, range=Optional[int])

slots.totalSpace = Slot(uri=UCO_OBSERVABLE.totalSpace, name="totalSpace", curie=UCO_OBSERVABLE.curie('totalSpace'),
                   model_uri=UCO_LINKML.totalSpace, domain=None, range=Optional[int])

slots.totalStorageCapacityInBytes = Slot(uri=UCO_OBSERVABLE.totalStorageCapacityInBytes, name="totalStorageCapacityInBytes", curie=UCO_OBSERVABLE.curie('totalStorageCapacityInBytes'),
                   model_uri=UCO_LINKML.totalStorageCapacityInBytes, domain=None, range=Optional[int])

slots.triggerBeginTime = Slot(uri=UCO_OBSERVABLE.triggerBeginTime, name="triggerBeginTime", curie=UCO_OBSERVABLE.curie('triggerBeginTime'),
                   model_uri=UCO_LINKML.triggerBeginTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.triggerDelay = Slot(uri=UCO_OBSERVABLE.triggerDelay, name="triggerDelay", curie=UCO_OBSERVABLE.curie('triggerDelay'),
                   model_uri=UCO_LINKML.triggerDelay, domain=None, range=Optional[str])

slots.triggerEndTime = Slot(uri=UCO_OBSERVABLE.triggerEndTime, name="triggerEndTime", curie=UCO_OBSERVABLE.curie('triggerEndTime'),
                   model_uri=UCO_LINKML.triggerEndTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.triggerFrequency = Slot(uri=UCO_OBSERVABLE.triggerFrequency, name="triggerFrequency", curie=UCO_OBSERVABLE.curie('triggerFrequency'),
                   model_uri=UCO_LINKML.triggerFrequency, domain=None, range=Optional[Union[str, "TriggerFrequencyVocab"]])

slots.triggerList = Slot(uri=UCO_OBSERVABLE.triggerList, name="triggerList", curie=UCO_OBSERVABLE.curie('triggerList'),
                   model_uri=UCO_LINKML.triggerList, domain=None, range=Optional[Union[Union[dict, TriggerType], list[Union[dict, TriggerType]]]])

slots.triggerMaxRunTime = Slot(uri=UCO_OBSERVABLE.triggerMaxRunTime, name="triggerMaxRunTime", curie=UCO_OBSERVABLE.curie('triggerMaxRunTime'),
                   model_uri=UCO_LINKML.triggerMaxRunTime, domain=None, range=Optional[str])

slots.triggerSessionChangeType = Slot(uri=UCO_OBSERVABLE.triggerSessionChangeType, name="triggerSessionChangeType", curie=UCO_OBSERVABLE.curie('triggerSessionChangeType'),
                   model_uri=UCO_LINKML.triggerSessionChangeType, domain=None, range=Optional[str])

slots.triggerType = Slot(uri=UCO_OBSERVABLE.triggerType, name="triggerType", curie=UCO_OBSERVABLE.curie('triggerType'),
                   model_uri=UCO_LINKML.triggerType, domain=None, range=Optional[Union[str, "TriggerTypeVocab"]])

slots.twitterHandle = Slot(uri=UCO_OBSERVABLE.twitterHandle, name="twitterHandle", curie=UCO_OBSERVABLE.curie('twitterHandle'),
                   model_uri=UCO_LINKML.twitterHandle, domain=None, range=Optional[str])

slots.twitterId = Slot(uri=UCO_OBSERVABLE.twitterId, name="twitterId", curie=UCO_OBSERVABLE.curie('twitterId'),
                   model_uri=UCO_LINKML.twitterId, domain=None, range=Optional[str])

slots.uninstallDate = Slot(uri=UCO_OBSERVABLE.uninstallDate, name="uninstallDate", curie=UCO_OBSERVABLE.curie('uninstallDate'),
                   model_uri=UCO_LINKML.uninstallDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.updatedDate = Slot(uri=UCO_OBSERVABLE.updatedDate, name="updatedDate", curie=UCO_OBSERVABLE.curie('updatedDate'),
                   model_uri=UCO_LINKML.updatedDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.uptime = Slot(uri=UCO_OBSERVABLE.uptime, name="uptime", curie=UCO_OBSERVABLE.curie('uptime'),
                   model_uri=UCO_LINKML.uptime, domain=None, range=Optional[str])

slots.url = Slot(uri=UCO_OBSERVABLE.url, name="url", curie=UCO_OBSERVABLE.curie('url'),
                   model_uri=UCO_LINKML.url, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.urlHistoryEntry = Slot(uri=UCO_OBSERVABLE.urlHistoryEntry, name="urlHistoryEntry", curie=UCO_OBSERVABLE.curie('urlHistoryEntry'),
                   model_uri=UCO_LINKML.urlHistoryEntry, domain=None, range=Optional[Union[Union[dict, URLHistoryEntry], list[Union[dict, URLHistoryEntry]]]])

slots.urlTargeted = Slot(uri=UCO_OBSERVABLE.urlTargeted, name="urlTargeted", curie=UCO_OBSERVABLE.curie('urlTargeted'),
                   model_uri=UCO_LINKML.urlTargeted, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.urlTransitionType = Slot(uri=UCO_OBSERVABLE.urlTransitionType, name="urlTransitionType", curie=UCO_OBSERVABLE.curie('urlTransitionType'),
                   model_uri=UCO_LINKML.urlTransitionType, domain=None, range=Optional[Union[str, "URLTransitionTypeVocab"]])

slots.userLocationString = Slot(uri=UCO_OBSERVABLE.userLocationString, name="userLocationString", curie=UCO_OBSERVABLE.curie('userLocationString'),
                   model_uri=UCO_LINKML.userLocationString, domain=None, range=Optional[str])

slots.userName = Slot(uri=UCO_OBSERVABLE.userName, name="userName", curie=UCO_OBSERVABLE.curie('userName'),
                   model_uri=UCO_LINKML.userName, domain=None, range=Optional[str])

slots.validityNotAfter = Slot(uri=UCO_OBSERVABLE.validityNotAfter, name="validityNotAfter", curie=UCO_OBSERVABLE.curie('validityNotAfter'),
                   model_uri=UCO_LINKML.validityNotAfter, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.validityNotBefore = Slot(uri=UCO_OBSERVABLE.validityNotBefore, name="validityNotBefore", curie=UCO_OBSERVABLE.curie('validityNotBefore'),
                   model_uri=UCO_LINKML.validityNotBefore, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.values = Slot(uri=UCO_OBSERVABLE.values, name="values", curie=UCO_OBSERVABLE.curie('values'),
                   model_uri=UCO_LINKML.values, domain=None, range=Optional[str])

slots.visibility = Slot(uri=UCO_OBSERVABLE.visibility, name="visibility", curie=UCO_OBSERVABLE.curie('visibility'),
                   model_uri=UCO_LINKML.visibility, domain=None, range=Optional[Union[bool, Bool]])

slots.visitCount = Slot(uri=UCO_OBSERVABLE.visitCount, name="visitCount", curie=UCO_OBSERVABLE.curie('visitCount'),
                   model_uri=UCO_LINKML.visitCount, domain=None, range=Optional[int])

slots.visitDuration = Slot(uri=UCO_OBSERVABLE.visitDuration, name="visitDuration", curie=UCO_OBSERVABLE.curie('visitDuration'),
                   model_uri=UCO_LINKML.visitDuration, domain=None, range=Optional[Union[str, UcoDuration]])

slots.visitTime = Slot(uri=UCO_OBSERVABLE.visitTime, name="visitTime", curie=UCO_OBSERVABLE.curie('visitTime'),
                   model_uri=UCO_LINKML.visitTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.volume = Slot(uri=UCO_OBSERVABLE.volume, name="volume", curie=UCO_OBSERVABLE.curie('volume'),
                   model_uri=UCO_LINKML.volume, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.volumeID = Slot(uri=UCO_OBSERVABLE.volumeID, name="volumeID", curie=UCO_OBSERVABLE.curie('volumeID'),
                   model_uri=UCO_LINKML.volumeID, domain=None, range=Optional[str])

slots.whoisContactType = Slot(uri=UCO_OBSERVABLE.whoisContactType, name="whoisContactType", curie=UCO_OBSERVABLE.curie('whoisContactType'),
                   model_uri=UCO_LINKML.whoisContactType, domain=None, range=Optional[Union[str, "WhoisContactTypeVocab"]])

slots.whoisServer = Slot(uri=UCO_OBSERVABLE.whoisServer, name="whoisServer", curie=UCO_OBSERVABLE.curie('whoisServer'),
                   model_uri=UCO_LINKML.whoisServer, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.win32VersionValue = Slot(uri=UCO_OBSERVABLE.win32VersionValue, name="win32VersionValue", curie=UCO_OBSERVABLE.curie('win32VersionValue'),
                   model_uri=UCO_LINKML.win32VersionValue, domain=None, range=Optional[Union[Union[int, UcoUnsignedInt], list[Union[int, UcoUnsignedInt]]]])

slots.windowTitle = Slot(uri=UCO_OBSERVABLE.windowTitle, name="windowTitle", curie=UCO_OBSERVABLE.curie('windowTitle'),
                   model_uri=UCO_LINKML.windowTitle, domain=None, range=Optional[str])

slots.windowsDirectory = Slot(uri=UCO_OBSERVABLE.windowsDirectory, name="windowsDirectory", curie=UCO_OBSERVABLE.curie('windowsDirectory'),
                   model_uri=UCO_LINKML.windowsDirectory, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.windowsSystemDirectory = Slot(uri=UCO_OBSERVABLE.windowsSystemDirectory, name="windowsSystemDirectory", curie=UCO_OBSERVABLE.curie('windowsSystemDirectory'),
                   model_uri=UCO_LINKML.windowsSystemDirectory, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.windowsTempDirectory = Slot(uri=UCO_OBSERVABLE.windowsTempDirectory, name="windowsTempDirectory", curie=UCO_OBSERVABLE.curie('windowsTempDirectory'),
                   model_uri=UCO_LINKML.windowsTempDirectory, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.windowsVolumeAttributes = Slot(uri=UCO_OBSERVABLE.windowsVolumeAttributes, name="windowsVolumeAttributes", curie=UCO_OBSERVABLE.curie('windowsVolumeAttributes'),
                   model_uri=UCO_LINKML.windowsVolumeAttributes, domain=None, range=Optional[Union[Union[str, "WindowsVolumeAttributeVocab"], list[Union[str, "WindowsVolumeAttributeVocab"]]]])

slots.wirelessNetworkSecurityMode = Slot(uri=UCO_OBSERVABLE.wirelessNetworkSecurityMode, name="wirelessNetworkSecurityMode", curie=UCO_OBSERVABLE.curie('wirelessNetworkSecurityMode'),
                   model_uri=UCO_LINKML.wirelessNetworkSecurityMode, domain=None, range=Optional[Union[str, "WirelessNetworkSecurityModeVocab"]])

slots.workItemData = Slot(uri=UCO_OBSERVABLE.workItemData, name="workItemData", curie=UCO_OBSERVABLE.curie('workItemData'),
                   model_uri=UCO_LINKML.workItemData, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.workingDirectory = Slot(uri=UCO_OBSERVABLE.workingDirectory, name="workingDirectory", curie=UCO_OBSERVABLE.curie('workingDirectory'),
                   model_uri=UCO_LINKML.workingDirectory, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.x509v3extensions = Slot(uri=UCO_OBSERVABLE.x509v3extensions, name="x509v3extensions", curie=UCO_OBSERVABLE.curie('x509v3extensions'),
                   model_uri=UCO_LINKML.x509v3extensions, domain=None, range=Optional[Union[dict, X509V3ExtensionsFacet]])

slots.xMailer = Slot(uri=UCO_OBSERVABLE.xMailer, name="xMailer", curie=UCO_OBSERVABLE.curie('xMailer'),
                   model_uri=UCO_LINKML.xMailer, domain=None, range=Optional[str])

slots.xOriginatingIP = Slot(uri=UCO_OBSERVABLE.xOriginatingIP, name="xOriginatingIP", curie=UCO_OBSERVABLE.curie('xOriginatingIP'),
                   model_uri=UCO_LINKML.xOriginatingIP, domain=None, range=Optional[Union[str, ObservableObjectId]])

slots.List_item = Slot(uri=COLL.item, name="List_item", curie=COLL.curie('item'),
                   model_uri=UCO_LINKML.List_item, domain=List, range=Optional[Union[Union[dict, "ListItem"], list[Union[dict, "ListItem"]]]])

slots.Annotation_object = Slot(uri=UCO_CORE.object, name="Annotation_object", curie=UCO_CORE.curie('object'),
                   model_uri=UCO_LINKML.Annotation_object, domain=Annotation, range=Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]])

slots.EnclosingCompilation_object = Slot(uri=UCO_CORE.object, name="EnclosingCompilation_object", curie=UCO_CORE.curie('object'),
                   model_uri=UCO_LINKML.EnclosingCompilation_object, domain=EnclosingCompilation, range=Union[Union[str, UcoObjectId], list[Union[str, UcoObjectId]]])

slots.LicenseMarking_definitionType = Slot(uri=UCO_MARKING.definitionType, name="LicenseMarking_definitionType", curie=UCO_MARKING.curie('definitionType'),
                   model_uri=UCO_LINKML.LicenseMarking_definitionType, domain=LicenseMarking, range=Optional[Union[str, list[str]]])

slots.MarkingDefinition_definitionType = Slot(uri=UCO_MARKING.definitionType, name="MarkingDefinition_definitionType", curie=UCO_MARKING.curie('definitionType'),
                   model_uri=UCO_LINKML.MarkingDefinition_definitionType, domain=MarkingDefinition, range=str)

slots.ReleaseToMarking_definitionType = Slot(uri=UCO_MARKING.definitionType, name="ReleaseToMarking_definitionType", curie=UCO_MARKING.curie('definitionType'),
                   model_uri=UCO_LINKML.ReleaseToMarking_definitionType, domain=ReleaseToMarking, range=Optional[Union[str, list[str]]])

slots.StatementMarking_definitionType = Slot(uri=UCO_MARKING.definitionType, name="StatementMarking_definitionType", curie=UCO_MARKING.curie('definitionType'),
                   model_uri=UCO_LINKML.StatementMarking_definitionType, domain=StatementMarking, range=Optional[Union[str, list[str]]])

slots.TermsOfUseMarking_definitionType = Slot(uri=UCO_MARKING.definitionType, name="TermsOfUseMarking_definitionType", curie=UCO_MARKING.curie('definitionType'),
                   model_uri=UCO_LINKML.TermsOfUseMarking_definitionType, domain=TermsOfUseMarking, range=Optional[Union[str, list[str]]])

slots.ConfiguredTool_isConfigurationOf = Slot(uri=UCO_CONFIGURATION.isConfigurationOf, name="ConfiguredTool_isConfigurationOf", curie=UCO_CONFIGURATION.curie('isConfigurationOf'),
                   model_uri=UCO_LINKML.ConfiguredTool_isConfigurationOf, domain=ConfiguredTool, range=Optional[Union[str, ToolId]])

slots.ControlledDictionary_entry = Slot(uri=UCO_TYPES.entry, name="ControlledDictionary_entry", curie=UCO_TYPES.curie('entry'),
                   model_uri=UCO_LINKML.ControlledDictionary_entry, domain=ControlledDictionary, range=Optional[Union[Union[dict, "ControlledDictionaryEntry"], list[Union[dict, "ControlledDictionaryEntry"]]]])

slots.Thread_item = Slot(uri=COLL.item, name="Thread_item", curie=COLL.curie('item'),
                   model_uri=UCO_LINKML.Thread_item, domain=Thread, range=Optional[Union[Union[str, ThreadItemId], list[Union[str, ThreadItemId]]]])

slots.ThreadItem_itemContent = Slot(uri=COLL.itemContent, name="ThreadItem_itemContent", curie=COLL.curie('itemContent'),
                   model_uri=UCO_LINKML.ThreadItem_itemContent, domain=ThreadItem, range=Optional[Union[str, UcoObjectId]])

slots.ActionLifecycle_phase = Slot(uri=UCO_ACTION.phase, name="ActionLifecycle_phase", curie=UCO_ACTION.curie('phase'),
                   model_uri=UCO_LINKML.ActionLifecycle_phase, domain=ActionLifecycle, range=Union[Union[dict, "ArrayOfAction"], list[Union[dict, "ArrayOfAction"]]])

slots.ConfiguredSoftware_isConfigurationOf = Slot(uri=UCO_CONFIGURATION.isConfigurationOf, name="ConfiguredSoftware_isConfigurationOf", curie=UCO_CONFIGURATION.curie('isConfigurationOf'),
                   model_uri=UCO_LINKML.ConfiguredSoftware_isConfigurationOf, domain=ConfiguredSoftware, range=Optional[Union[str, SoftwareId]])

slots.ContactAffiliation_contactEmail = Slot(uri=UCO_OBSERVABLE.contactEmail, name="ContactAffiliation_contactEmail", curie=UCO_OBSERVABLE.curie('contactEmail'),
                   model_uri=UCO_LINKML.ContactAffiliation_contactEmail, domain=ContactAffiliation, range=Optional[Union[Union[dict, "ContactEmail"], list[Union[dict, "ContactEmail"]]]])

slots.ContactAffiliation_contactMessaging = Slot(uri=UCO_OBSERVABLE.contactMessaging, name="ContactAffiliation_contactMessaging", curie=UCO_OBSERVABLE.curie('contactMessaging'),
                   model_uri=UCO_LINKML.ContactAffiliation_contactMessaging, domain=ContactAffiliation, range=Optional[Union[Union[dict, "ContactMessaging"], list[Union[dict, "ContactMessaging"]]]])

slots.ContactAffiliation_contactPhone = Slot(uri=UCO_OBSERVABLE.contactPhone, name="ContactAffiliation_contactPhone", curie=UCO_OBSERVABLE.curie('contactPhone'),
                   model_uri=UCO_LINKML.ContactAffiliation_contactPhone, domain=ContactAffiliation, range=Optional[Union[Union[dict, "ContactPhone"], list[Union[dict, "ContactPhone"]]]])

slots.ContactAffiliation_contactURL = Slot(uri=UCO_OBSERVABLE.contactURL, name="ContactAffiliation_contactURL", curie=UCO_OBSERVABLE.curie('contactURL'),
                   model_uri=UCO_LINKML.ContactAffiliation_contactURL, domain=ContactAffiliation, range=Optional[Union[Union[dict, "ContactURL"], list[Union[dict, "ContactURL"]]]])

slots.ContactFacet_contactAddress = Slot(uri=UCO_OBSERVABLE.contactAddress, name="ContactFacet_contactAddress", curie=UCO_OBSERVABLE.curie('contactAddress'),
                   model_uri=UCO_LINKML.ContactFacet_contactAddress, domain=ContactFacet, range=Optional[Union[Union[dict, ContactAddress], list[Union[dict, ContactAddress]]]])

slots.ContactFacet_contactEmail = Slot(uri=UCO_OBSERVABLE.contactEmail, name="ContactFacet_contactEmail", curie=UCO_OBSERVABLE.curie('contactEmail'),
                   model_uri=UCO_LINKML.ContactFacet_contactEmail, domain=ContactFacet, range=Optional[Union[Union[dict, ContactEmail], list[Union[dict, ContactEmail]]]])

slots.ContactFacet_contactMessaging = Slot(uri=UCO_OBSERVABLE.contactMessaging, name="ContactFacet_contactMessaging", curie=UCO_OBSERVABLE.curie('contactMessaging'),
                   model_uri=UCO_LINKML.ContactFacet_contactMessaging, domain=ContactFacet, range=Optional[Union[Union[dict, "ContactMessaging"], list[Union[dict, "ContactMessaging"]]]])

slots.ContactFacet_contactPhone = Slot(uri=UCO_OBSERVABLE.contactPhone, name="ContactFacet_contactPhone", curie=UCO_OBSERVABLE.curie('contactPhone'),
                   model_uri=UCO_LINKML.ContactFacet_contactPhone, domain=ContactFacet, range=Optional[Union[Union[dict, "ContactPhone"], list[Union[dict, "ContactPhone"]]]])

slots.ContactFacet_contactURL = Slot(uri=UCO_OBSERVABLE.contactURL, name="ContactFacet_contactURL", curie=UCO_OBSERVABLE.curie('contactURL'),
                   model_uri=UCO_LINKML.ContactFacet_contactURL, domain=ContactFacet, range=Optional[Union[Union[dict, "ContactURL"], list[Union[dict, "ContactURL"]]]])

slots.Observation_name = Slot(uri=UCO_CORE.name, name="Observation_name", curie=UCO_CORE.curie('name'),
                   model_uri=UCO_LINKML.Observation_name, domain=Observation, range=str)

slots.OnlineServiceFacet_observable_location = Slot(uri=UCO_OBSERVABLE.location, name="OnlineServiceFacet_observable_location", curie=UCO_OBSERVABLE.curie('location'),
                   model_uri=UCO_LINKML.OnlineServiceFacet_observable_location, domain=OnlineServiceFacet, range=Optional[Union[Union[str, LocationId], list[Union[str, LocationId]]]])

slots.PathRelationFacet_path = Slot(uri=UCO_OBSERVABLE.path, name="PathRelationFacet_path", curie=UCO_OBSERVABLE.curie('path'),
                   model_uri=UCO_LINKML.PathRelationFacet_path, domain=PathRelationFacet, range=Optional[Union[str, list[str]]])

slots.WhoIsFacet_status = Slot(uri=UCO_OBSERVABLE.status, name="WhoIsFacet_status", curie=UCO_OBSERVABLE.curie('status'),
                   model_uri=UCO_LINKML.WhoIsFacet_status, domain=WhoIsFacet, range=Optional[Union[str, "TaskStatusVocab", "WhoisStatusTypeVocab"]])

slots.WindowsPESection_hashes = Slot(uri=UCO_OBSERVABLE.hashes, name="WindowsPESection_hashes", curie=UCO_OBSERVABLE.curie('hashes'),
                   model_uri=UCO_LINKML.WindowsPESection_hashes, domain=WindowsPESection, range=Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]])

slots.WindowsTaskFacet_priority = Slot(uri=UCO_OBSERVABLE.priority, name="WindowsTaskFacet_priority", curie=UCO_OBSERVABLE.curie('priority'),
                   model_uri=UCO_LINKML.WindowsTaskFacet_priority, domain=WindowsTaskFacet, range=Optional[Union[str, "TaskPriorityVocab", int]])

slots.WindowsTaskFacet_status = Slot(uri=UCO_OBSERVABLE.status, name="WindowsTaskFacet_status", curie=UCO_OBSERVABLE.curie('status'),
                   model_uri=UCO_LINKML.WindowsTaskFacet_status, domain=WindowsTaskFacet, range=Optional[Union[str, "TaskStatusVocab"]])

slots.WindowsThreadFacet_priority = Slot(uri=UCO_OBSERVABLE.priority, name="WindowsThreadFacet_priority", curie=UCO_OBSERVABLE.curie('priority'),
                   model_uri=UCO_LINKML.WindowsThreadFacet_priority, domain=WindowsThreadFacet, range=Optional[int])
