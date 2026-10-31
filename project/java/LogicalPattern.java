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
  A logical pattern is a grouping of characteristics unique to an informational pattern expressed via a structured pattern expression following the rules of logic.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LogicalPattern extends Pattern {

  private String patternExpression;


}