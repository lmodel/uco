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
  An observable object is a grouping of characteristics unique to a distinct article or unit within the digital domain.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ObservableObject extends Observable {

  private Boolean hasChanged;
  private String state;


}