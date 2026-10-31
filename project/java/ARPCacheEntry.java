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
  An ARP cache entry is a single Address Resolution Protocol (ARP) response record that is created when an IP address is resolved to a MAC address (so the computer can effectively communicate with the IP address). [based on https://en.wikipedia.org/wiki/ARP_cache]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ARPCacheEntry extends ObservableObject {



}