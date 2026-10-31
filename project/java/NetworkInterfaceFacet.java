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
  A network interface facet is a grouping of characteristics unique to a software or hardware interface between two pieces of equipment or protocol layers in a computer network.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NetworkInterfaceFacet extends Facet {

  private String adapterName;
  private ZonedDateTime dhcpLeaseExpires;
  private ZonedDateTime dhcpLeaseObtained;
  private List<ObservableObject> dhcpServer;
  private List<ObservableObject> ip;
  private List<ObservableObject> ipGateway;
  private ObservableObject macAddress;


}