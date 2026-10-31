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
  A hostname is a label that is assigned to a device connected to a computer network and that is used to identify the device in various forms of electronic communication, such as the World Wide Web. A hostname may be a domain name, if it is properly organized into the domain name system. A domain name may be a hostname if it has been assigned to an Internet host and associated with the host's IP address. [based on https://en.wikipedia.org/wiki/Hostname]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Hostname extends ObservableObject {



}