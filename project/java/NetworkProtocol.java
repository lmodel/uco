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
  A network protocol is an established set of structured rules that determine how data is transmitted between different devices in the same network. Essentially, it allows connected devices to communicate with each other, regardless of any differences in their internal processes, structure or design. [based on https://www.comptia.org/content/guides/what-is-a-network-protocol]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NetworkProtocol extends ObservableObject {



}