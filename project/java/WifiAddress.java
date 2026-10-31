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
  A Wi-Fi address is a media access control (MAC) standards-conformant identifier assigned to a device network interface to enable routing and management of IEEE 802.11 standards-conformant communications to and from that device.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WifiAddress extends MACAddress {



}