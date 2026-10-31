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
  An annotation is an assertion made in relation to one or more objects.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Annotation extends Assertion {

  private List<UcoObject> object;


}