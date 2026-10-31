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
  A properties read effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a characteristic is read from an observable object. An example of this would be the current running state of a process.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PropertyReadEffectFacet extends DefinedEffectFacet {

  private String observableValue;
  private String propertyName;


}