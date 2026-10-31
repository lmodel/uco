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
  A cell site facet contains the metadata surrounding the cell site.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CellSiteFacet extends Facet {

  private String cellSiteCountryCode;
  private String cellSiteIdentifier;
  private String cellSiteLocationAreaCode;
  private String cellSiteNetworkCode;
  private String cellSiteType;


}