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
  An action estimation facet is a grouping of characteristics unique to decision-focused approximation aspects for an action that may potentially be performed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ActionEstimationFacet extends Facet {

  private String estimatedCost;
  private String estimatedEfficacy;
  private String estimatedImpact;
  private String objective;


}