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
  An artifact classification result facet is a grouping of characteristics unique to the results of an artifact classification analysis action.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ArtifactClassificationResultFacet extends AnalyticResultFacet {

  private List<ArtifactClassification> classification;


}