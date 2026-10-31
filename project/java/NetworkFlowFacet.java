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
  A network flow facet is a grouping of characteristics unique to a sequence of data transiting one or more digital network (a group of two or more computer systems linked together) connections. [based on https://www.webopedia.com/TERM/N/network.html]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NetworkFlowFacet extends Facet {

  private Integer dstBytes;
  private Integer dstPackets;
  private ObservableObject dstPayload;
  private Dictionary ipfix;
  private Integer srcBytes;
  private Integer srcPackets;
  private ObservableObject srcPayload;


}