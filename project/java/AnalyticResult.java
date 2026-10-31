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
  An analytic result is a characterization of the understanding resulting from an analysis action.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AnalyticResult extends Assertion {

  private Analysis originatingAnalysis;
  private List<UcoObject> resultContent;


}