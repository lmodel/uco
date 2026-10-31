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
  A fragment facet is a grouping of characteristics unique to an individual piece of the content of a file.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FragmentFacet extends Facet {

  private List<Integer> fragmentIndex;
  private List<Integer> totalFragments;


}