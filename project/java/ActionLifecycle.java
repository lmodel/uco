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
  An action lifecycle is an action pattern consisting of an ordered set of multiple actions or subordinate action lifecycles.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ActionLifecycle extends Action {

  private List<ArrayOfAction> phase;


}