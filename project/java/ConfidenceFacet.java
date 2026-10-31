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
  A confidence is a grouping of characteristics unique to an asserted level of certainty in the accuracy of some information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConfidenceFacet extends Facet {

  private Integer confidence;


}