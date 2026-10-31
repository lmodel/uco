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
  A properties enumerated effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a characteristic of the observable object is enumerated. An example of this would be startup parameters for a process.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PropertiesEnumeratedEffectFacet extends DefinedEffectFacet {

  private String properties;


}