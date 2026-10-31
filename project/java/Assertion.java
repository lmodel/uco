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
  An assertion is a statement declared to be true.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Assertion extends UcoObject {

  private List<String> statement;


}