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
  A wireless network connection facet is a grouping of characteristics unique to a connection (completed or attempted) across an IEEE 802.11 standards-conformant digital network (a group of two or more computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WirelessNetworkConnectionFacet extends Facet {

  private String baseStation;
  private String password;
  private String ssid;
  private String wirelessNetworkSecurityMode;


}