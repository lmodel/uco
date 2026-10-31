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
  An action frequency facet is a grouping of characteristics unique to the frequency of occurrence for an action.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ActionFrequencyFacet extends Facet {

  private BigDecimal rate;
  private String scale;
  private String trend;
  private String units;


}