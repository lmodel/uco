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
  A values enumerated effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a value of the observable object is enumerated. An example of this would be the values of a registry key.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ValuesEnumeratedEffectFacet extends DefinedEffectFacet {

  private String values;


}