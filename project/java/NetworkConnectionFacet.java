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
  A network connection facet is a grouping of characteristics unique to a connection (complete or attempted) accross a digital network (a group of two or more computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NetworkConnectionFacet extends Facet {

  private Integer destinationPort;
  private List<ObservableObject> dst;
  private Boolean isActive;
  private ZonedDateTime observableEndTime;
  private ZonedDateTime observableStartTime;
  private ControlledDictionary protocols;
  private Integer sourcePort;
  private List<UcoObject> src;


}