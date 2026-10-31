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
  An HTTP connection facet is a grouping of characteristics unique to portions of a network connection that are conformant to the Hypertext Transfer Protocol (HTTP) standard.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HTTPConnectionFacet extends Facet {

  private Integer httpMesageBodyLength;
  private ObservableObject httpMessageBodyData;
  private Dictionary httpRequestHeader;
  private String requestMethod;
  private String requestValue;
  private String requestVersion;


}