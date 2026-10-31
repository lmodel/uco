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
  A state change effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a state of the observable object is changed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StateChangeEffectFacet extends DefinedEffectFacet {

  private ObservableObject newObject;
  private ObservableObject oldObject;


}