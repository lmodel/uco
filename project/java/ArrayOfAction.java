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
  An array of action is an ordered list of references to things that may be done or performed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ArrayOfAction extends UcoInherentCharacterizationThing {

  private List<Action> action;


}