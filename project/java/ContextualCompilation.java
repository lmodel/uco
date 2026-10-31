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
  A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed on a given day, all accounts associated with a given person).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContextualCompilation extends Compilation {

  private List<UcoObject> object;


}