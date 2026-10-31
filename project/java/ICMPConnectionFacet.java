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
  An ICMP connection facet is a grouping of characteristics unique to portions of a network connection that are conformant to the Internet Control Message Protocol (ICMP) standard.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ICMPConnectionFacet extends Facet {

  private List<String> icmpCode;
  private List<String> icmpType;


}