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
  An item of a list, which has a place in the list's order.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListItem extends CoItem {

  private List<CoItem> followedBy;
  private Integer index;


}