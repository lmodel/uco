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
  Characteristics of a reference to a resource outside of the UCO.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExternalReference extends UcoInherentCharacterizationThing {

  private String definingContext;
  private String externalIdentifier;
  private URI referenceURL;


}