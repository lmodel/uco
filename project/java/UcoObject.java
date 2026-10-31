package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A UCO object is a representation of a fundamental concept either directly inherent to the cyber domain or indirectly related to the cyber domain and necessary for contextually characterizing cyber domain concepts and relationships. Within the Unified Cyber Ontology (UCO) structure this is the base class acting as a consistent, unifying and interoperable foundation for all explicit and inter-relatable content objects.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UcoObject extends UcoThing {

  private URI id;
  private IdentityAbstraction createdBy;
  private List<String> description;
  private List<ExternalReference> externalReference;
  private List<Facet> hasFacet;
  private List<ZonedDateTime> modifiedTime;
  private String name;
  private ZonedDateTime objectCreatedTime;
  private List<MarkingDefinitionAbstraction> objectMarking;
  private String objectStatus;
  private String specVersion;
  private List<String> tag;


}