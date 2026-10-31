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
  A TCP connection facet is a grouping of characteristics unique to portions of a network connection that are conformant to the Transmission Control Protocl (TCP) standard.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TCPConnectionFacet extends Facet {

  private List<String> destinationFlags;
  private List<String> sourceFlags;


}