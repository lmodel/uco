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
  An artifact classification is a single specific assertion that a particular class of a classification taxonomy applies to something.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ArtifactClassification extends UcoInherentCharacterizationThing {

  private List<String> class_;
  private BigDecimal classificationConfidence;


}