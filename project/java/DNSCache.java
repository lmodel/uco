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
  An DNS cache is a temporary locally stored collection of previous Domain Name System (DNS) query results (created when an domain name is resolved to a IP address) for a particular computer.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DNSCache extends ObservableObject {



}