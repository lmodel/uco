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
  A URL facet is a grouping of characteristics unique to a uniform resource locator (URL) acting as a resolvable address to a particular WWW (World Wide Web) accessible resource.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class URLFacet extends Facet {

  private String fragment;
  private String fullValue;
  private ObservableObject host;
  private String password;
  private String path;
  private Integer port;
  private String query;
  private String scheme;
  private String userName;


}