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
  A path relation facet is a grouping of characteristics unique to the location of one object within another containing object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PathRelationFacet extends Facet {

  private List<String> path;


}