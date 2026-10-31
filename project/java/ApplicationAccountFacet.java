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
  An application account facet is a grouping of characteristics unique to an account within a particular software program designed for end users.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ApplicationAccountFacet extends Facet {

  private ObservableObject application;


}