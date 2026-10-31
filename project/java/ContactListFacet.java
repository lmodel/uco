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
  A contact list facet is a grouping of characteristics unique to a set of multiple individual contacts such as that found in a digital address book.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContactListFacet extends Facet {

  private List<ObservableObject> contact;
  private ObservableObject sourceApplication;


}