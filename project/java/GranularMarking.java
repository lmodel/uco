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
  A granular marking is a grouping of characteristics unique to specification of marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) that apply to particular portions of a particular UCO object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GranularMarking extends UcoInherentCharacterizationThing {

  private List<String> contentSelectors;
  private List<MarkingDefinition> marking;


}