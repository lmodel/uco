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
  A captured telecommunications information facet represents certain information within captured or intercepted telecommunications data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CapturedTelecommunicationsInformationFacet extends Facet {

  private CellSite captureCellSite;
  private String interceptedCallState;
  private ZonedDateTime observableEndTime;
  private ZonedDateTime observableStartTime;


}