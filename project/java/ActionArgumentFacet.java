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
  An action argument facet is a grouping of characteristics unique to a single parameter of an action.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ActionArgumentFacet extends Facet {

  private String actionValue;
  private String argumentName;


}