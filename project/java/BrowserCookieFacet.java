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
  A browser cookie facet is a grouping of characteristics unique to a piece of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing. [based on https://en.wikipedia.org/wiki/HTTP_cookie]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BrowserCookieFacet extends Facet {

  private ZonedDateTime accessedTime;
  private ObservableObject application;
  private ObservableObject cookieDomain;
  private String cookieName;
  private String cookiePath;
  private ZonedDateTime expirationTime;
  private Boolean isSecure;
  private ZonedDateTime observableCreatedTime;


}