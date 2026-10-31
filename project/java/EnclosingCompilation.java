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
  An enclosing compilation is a container for a grouping of things.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EnclosingCompilation extends Compilation {

  private List<UcoObject> object;


}