# HW2 풀이 - 남건우

---

## Problem 9

**문제:** X의 분포함수(CDF)가 다음과 같이 주어질 때, X의 확률질량함수(PMF)를 구하라.

$$F(b) = \begin{cases} 0, & b < 0 \\ \frac{1}{2}, & 0 \leq b < 1 \\ 1, & 1 \leq b < \infty \end{cases}$$

**풀이:**

이산 확률변수에서 PMF는 CDF의 점프 불연속점(jump discontinuity)에서의 도약량과 같다.

$$p(x) = P\{X = x\} = F(x) - \lim_{b \to x^-} F(b)$$

- **$x = 0$에서의 점프량:**

$$p(0) = F(0) - \lim_{b \to 0^-} F(b) = \frac{1}{2} - 0 = \frac{1}{2}$$

- **$x = 1$에서의 점프량:**

$$p(1) = F(1) - \lim_{b \to 1^-} F(b) = 1 - \frac{1}{2} = \frac{1}{2}$$

그 외 다른 점에서는 CDF가 연속이므로 점프가 없다.

따라서 X의 PMF는:

$$p(x) = \begin{cases} \dfrac{1}{2}, & x = 0 \\ \dfrac{1}{2}, & x = 1 \\ 0, & \text{otherwise} \end{cases}$$

**검증:** $p(0) + p(1) = \frac{1}{2} + \frac{1}{2} = 1$ ✓

---

## Problem 34

**문제:** X의 확률밀도함수(PDF)가 다음과 같이 주어진다.

$$f(x) = \begin{cases} c(4x - 2x^2), & 0 < x < 2 \\ 0, & \text{otherwise} \end{cases}$$

**(a) $c$의 값을 구하라.**

PDF의 정규화 조건(normalization condition)에 의해:

$$\int_{-\infty}^{\infty} f(x)\,dx = 1$$

$$\int_0^2 c(4x - 2x^2)\,dx = 1$$

적분을 계산한다:

$$c \left[ 2x^2 - \frac{2}{3}x^3 \right]_0^2 = 1$$

$$c \left( 2(4) - \frac{2}{3}(8) \right) = 1$$

$$c \left( 8 - \frac{16}{3} \right) = 1$$

$$c \cdot \frac{24 - 16}{3} = 1$$

$$c \cdot \frac{8}{3} = 1$$

$$\boxed{c = \frac{3}{8}}$$

**(b) $P\!\left\{\frac{1}{2} < X < \frac{3}{2}\right\}$를 구하라.**

$$P\!\left\{\frac{1}{2} < X < \frac{3}{2}\right\} = \int_{1/2}^{3/2} \frac{3}{8}(4x - 2x^2)\,dx = \frac{3}{8}\left[2x^2 - \frac{2}{3}x^3\right]_{1/2}^{3/2}$$

각 경계에서의 값을 계산한다:

$$x = \frac{3}{2}: \quad 2\left(\frac{9}{4}\right) - \frac{2}{3}\left(\frac{27}{8}\right) = \frac{9}{2} - \frac{9}{4} = \frac{18}{4} - \frac{9}{4} = \frac{9}{4}$$

$$x = \frac{1}{2}: \quad 2\left(\frac{1}{4}\right) - \frac{2}{3}\left(\frac{1}{8}\right) = \frac{1}{2} - \frac{1}{12} = \frac{6}{12} - \frac{1}{12} = \frac{5}{12}$$

따라서:

$$P\!\left\{\frac{1}{2} < X < \frac{3}{2}\right\} = \frac{3}{8}\left(\frac{9}{4} - \frac{5}{12}\right) = \frac{3}{8}\left(\frac{27}{12} - \frac{5}{12}\right) = \frac{3}{8} \cdot \frac{22}{12} = \frac{3}{8} \cdot \frac{11}{6} = \frac{33}{48}$$

$$\boxed{P\!\left\{\frac{1}{2} < X < \frac{3}{2}\right\} = \frac{11}{16}}$$

---

## Problem 36

**문제:** 반지름 1인 원판 안에서 점이 균등하게 분포한다. 즉 joint density는:

$$f(x, y) = C, \quad 0 \leq x^2 + y^2 \leq 1$$

원점으로부터의 거리가 $x$보다 작을 확률 ($0 \leq x \leq 1$)을 구하라.

**풀이:**

**Step 1: 상수 $C$ 결정**

정규화 조건에 의해:

$$\iint_{x^2 + y^2 \leq 1} C\,dA = 1$$

적분 영역이 반지름 1인 원판이므로 면적 $= \pi \cdot 1^2 = \pi$:

$$C \cdot \pi = 1 \implies C = \frac{1}{\pi}$$

**Step 2: 거리 $x$ 이내의 확률 계산**

원점으로부터의 거리를 $D = \sqrt{X^2 + Y^2}$라 하면, $0 \leq x \leq 1$에서:

$$P\{D < x\} = \iint_{u^2 + v^2 < x^2} \frac{1}{\pi}\,dA$$

적분 영역은 반지름 $x$인 원판 (면적 $= \pi x^2$)이므로:

$$P\{D < x\} = \frac{1}{\pi} \cdot \pi x^2$$

$$\boxed{P\{D < x\} = x^2, \quad 0 \leq x \leq 1}$$

---

## Problem 54

**문제:** $X$와 $Y$는 각각 $1$ 또는 $-1$의 값을 취하고, $E[X] = E[Y] = 0$이 주어진다.

**(a) $p(1,1) = p(-1,-1)$ 임을 보여라.**

$E[X] = 0$ 조건으로부터:

$$E[X] = 1 \cdot P\{X=1\} + (-1) \cdot P\{X=-1\} = 0 \implies P\{X=1\} = P\{X=-1\} = \frac{1}{2}$$

$E[Y] = 0$ 조건으로부터:

$$P\{Y=1\} = P\{Y=-1\} = \frac{1}{2}$$

주변 확률(marginal probability)을 joint PMF로 표현하면:

$$P\{X = 1\} = p(1,1) + p(1,-1) = \frac{1}{2} \quad \cdots (i)$$

$$P\{Y = -1\} = p(1,-1) + p(-1,-1) = \frac{1}{2} \quad \cdots (ii)$$

$(i) - (ii)$를 계산하면:

$$p(1,1) - p(-1,-1) = 0$$

$$\therefore \boxed{p(1,1) = p(-1,-1)} \quad \blacksquare$$

**(b) $p(1,-1) = p(-1,1)$ 임을 보여라.**

$$P\{X = 1\} = p(1,1) + p(1,-1) = \frac{1}{2} \quad \cdots (i)$$

$$P\{Y = 1\} = p(1,1) + p(-1,1) = \frac{1}{2} \quad \cdots (iii)$$

$(i) - (iii)$를 계산하면:

$$p(1,-1) - p(-1,1) = 0$$

$$\therefore \boxed{p(1,-1) = p(-1,1)} \quad \blacksquare$$

---

$p = 2p(1,1)$으로 정의하면, (a), (b)의 결과를 이용하여:

$$p(1,1) = p(-1,-1) = \frac{p}{2}, \qquad p(1,-1) = p(-1,1) = \frac{1-p}{2}$$

검증: $\frac{p}{2} + \frac{1-p}{2} + \frac{1-p}{2} + \frac{p}{2} = p + (1-p) = 1$ ✓

**(c) $\text{Var}(X)$를 구하라.**

$$E[X] = 0 \quad \text{(주어진 조건)}$$

$$E[X^2] = 1^2 \cdot P\{X=1\} + (-1)^2 \cdot P\{X=-1\} = 1 \cdot \frac{1}{2} + 1 \cdot \frac{1}{2} = 1$$

$$\boxed{\text{Var}(X) = E[X^2] - (E[X])^2 = 1 - 0 = 1}$$

**(d) $\text{Var}(Y)$를 구하라.**

$Y$도 $E[Y] = 0$, $P\{Y=1\} = P\{Y=-1\} = \frac{1}{2}$이므로 (c)와 동일한 방법으로:

$$E[Y^2] = 1 \cdot \frac{1}{2} + 1 \cdot \frac{1}{2} = 1$$

$$\boxed{\text{Var}(Y) = E[Y^2] - (E[Y])^2 = 1 - 0 = 1}$$

**(e) $\text{Cov}(X, Y)$를 구하라.**

$$\text{Cov}(X, Y) = E[XY] - E[X]\,E[Y] = E[XY] - 0 = E[XY]$$

$E[XY]$를 joint PMF를 이용해 계산한다:

$$E[XY] = (1)(1)\,p(1,1) + (1)(-1)\,p(1,-1) + (-1)(1)\,p(-1,1) + (-1)(-1)\,p(-1,-1)$$

$$= \frac{p}{2} - \frac{1-p}{2} - \frac{1-p}{2} + \frac{p}{2}$$

$$= p - (1-p) = 2p - 1$$

$$\boxed{\text{Cov}(X, Y) = 2p - 1}$$

> **해석:** $p > \frac{1}{2}$이면 양의 공분산(X, Y가 같은 방향으로 움직이는 경향), $p < \frac{1}{2}$이면 음의 공분산, $p = \frac{1}{2}$이면 X와 Y는 uncorrelated.

---

## Problem 62

**문제:** 보험회사의 보험료는 다음과 같이 정의된다.

$$P = \frac{1}{a} \ln\!\left(E[e^{aX}]\right)$$

$X \sim \text{Exponential}(\lambda)$이고 $a = \alpha\lambda$ ($0 < \alpha < 1$)일 때, $P$를 구하라.

**풀이:**

**Step 1: $E[e^{aX}]$ 계산**

연속 확률변수의 기댓값 정의 $E[g(X)] = \int_{-\infty}^{\infty} g(x)f(x)\,dx$에 $g(x) = e^{ax}$, $f(x) = \lambda e^{-\lambda x}$ ($x \geq 0$)를 대입하면:

$$E[e^{aX}] = \int_0^{\infty} e^{ax} \cdot \lambda e^{-\lambda x}\,dx$$

지수 법칙 $e^{ax} \cdot e^{-\lambda x} = e^{-(\lambda-a)x}$으로 합치면:

$$= \lambda \int_0^{\infty} e^{-(\lambda - a)x}\,dx$$

이 적분이 수렴하려면 지수의 계수가 양수여야 한다. $a = \alpha\lambda$이고 $0 < \alpha < 1$이므로:

$$\lambda - a = \lambda - \alpha\lambda = \lambda(1-\alpha) > 0 \quad \checkmark$$

$\int_0^{\infty} e^{-cx}\,dx = \dfrac{1}{c}$ ($c > 0$)를 적용하면:

$$E[e^{aX}] = \lambda \cdot \frac{1}{\lambda - a} = \frac{\lambda}{\lambda(1-\alpha)} = \frac{1}{1-\alpha}$$

**Step 2: 보험료 $P$ 계산**

$$P = \frac{1}{a}\ln\!\left(E[e^{aX}]\right) = \frac{1}{\alpha\lambda}\ln\!\left(\frac{1}{1-\alpha}\right)$$

$$\boxed{P = \frac{-\ln(1-\alpha)}{\alpha\lambda}}$$

> **참고:** $0 < \alpha < 1$에서 $\ln(1-\alpha) < 0$이므로 $P > 0$. 즉 보험료는 항상 양수이다.

---

## Problem 63

**문제:** 기하 확률변수(geometric random variable)의 적률생성함수(MGF)를 구하라.

**풀이:**

기하 확률변수 $X$는 parameter $p$를 가지며, PMF는:

$$p(n) = P\{X = n\} = (1-p)^{n-1}p, \quad n = 1, 2, \ldots$$

MGF의 정의에 의해:

$$M(t) = E[e^{tX}] = \sum_{n=1}^{\infty} e^{tn}(1-p)^{n-1}p$$

$e^t$를 묶어서 정리하면:

$$M(t) = pe^t \sum_{n=1}^{\infty} \left[e^t(1-p)\right]^{n-1}$$

$m = n - 1$로 치환하면 ($n: 1\to\infty$ → $m: 0\to\infty$):

$$M(t) = pe^t \sum_{m=0}^{\infty} \left[(1-p)e^t\right]^{m}$$

이 급수는 $|(1-p)e^t| < 1$, 즉 $t < -\ln(1-p)$일 때 수렴하는 등비급수(geometric series)이다:

$$\sum_{m=0}^{\infty} \left[(1-p)e^t\right]^m = \frac{1}{1-(1-p)e^t}$$

따라서:

$$\boxed{M(t) = \frac{pe^t}{1-(1-p)e^t}, \qquad t < -\ln(1-p)}$$

---

## Problem 71

**문제:** $n$개의 흰 공과 $m$개의 검은 공이 들어있는 항아리에서 $k$개의 공을 무작위로 선택할 때, $X$를 선택된 흰 공의 수라 하자.

**(a) $P\{X = i\}$를 구하라.**

전체 $n+m$개 중 $k$개를 선택하는 방법의 수는 $\binom{n+m}{k}$.

$X = i$이 되려면 흰 공 $n$개 중 $i$개, 검은 공 $m$개 중 $k-i$개를 선택해야 한다:

$$\boxed{P\{X = i\} = \frac{\binom{n}{i}\binom{m}{k-i}}{\binom{n+m}{k}}, \qquad \max(0,\, k-m) \leq i \leq \min(k,\, n)}$$

이를 **초기하분포(Hypergeometric Distribution)**라 한다.

**(b) $E[X]$를 두 가지 방법으로 구하라.**

---

### 방법 1: $X_i$를 이용 (선택 순서 기준)

indicator 확률변수를 정의한다:

$$X_i = \begin{cases} 1, & \text{$i$번째 선택된 공이 흰 공일 때} \\ 0, & \text{otherwise} \end{cases} \quad i = 1, 2, \ldots, k$$

그러면 $X = X_1 + X_2 + \cdots + X_k$.

대칭성(symmetry)에 의해, $i$번째로 선택된 공이 흰 공일 확률은 선택 순서에 관계없이 동일하다:

$$P\{X_i = 1\} = \frac{n}{n+m}$$

기댓값의 선형성에 의해:

$$E[X] = \sum_{i=1}^{k} E[X_i] = \sum_{i=1}^{k} \frac{n}{n+m} = \frac{kn}{n+m}$$

---

### 방법 2: $Y_j$를 이용 (흰 공 번호 기준)

indicator 확률변수를 정의한다:

$$Y_j = \begin{cases} 1, & \text{$j$번째 흰 공이 선택될 때} \\ 0, & \text{otherwise} \end{cases} \quad j = 1, 2, \ldots, n$$

그러면 $X = Y_1 + Y_2 + \cdots + Y_n$.

특정 흰 공 $j$가 $k$개 선택 중에 포함될 확률은:

$$P\{Y_j = 1\} = \frac{k}{n+m}$$

기댓값의 선형성에 의해:

$$E[X] = \sum_{j=1}^{n} E[Y_j] = \sum_{j=1}^{n} \frac{k}{n+m} = \frac{kn}{n+m}$$

---

**결론:** 두 방법 모두 동일한 결과를 준다.

$$\boxed{E[X] = \frac{kn}{n+m}}$$ 

---

## Problem 58

**문제:** 항아리에 $2n$개의 공이 있으며, 그 중 $r$개는 빨간 공이다. 공들을 $n$쌍으로 무작위 추출할 때, $X$를 두 공 모두 빨간 쌍의 수라 하자.

**(a) $E[X]$를 구하라.**

**Indicator 확률변수 정의:**

$$X_i = \begin{cases} 1, & \text{$i$번째 쌍의 두 공이 모두 빨간 경우} \\ 0, & \text{otherwise} \end{cases} \quad i = 1, 2, \ldots, n$$

그러면 $X = X_1 + X_2 + \cdots + X_n$.

**$P\{X_i = 1\}$ 계산:**

대칭성(symmetry)에 의해, $i$번째 쌍에 어떤 2개의 공이 배정될 확률은 동등하다. 따라서 $i$번째 쌍의 두 공이 모두 빨간 확률은 $2n$개 중 임의의 2개를 뽑았을 때 둘 다 빨간 확률과 같다:

$$P\{X_i = 1\} = \frac{\binom{r}{2}}{\binom{2n}{2}} = \frac{\dfrac{r(r-1)}{2}}{\dfrac{2n(2n-1)}{2}} = \frac{r(r-1)}{2n(2n-1)}$$

**기댓값의 선형성 적용:**

$$E[X] = \sum_{i=1}^{n} E[X_i] = n \cdot \frac{r(r-1)}{2n(2n-1)}$$

$$\boxed{E[X] = \frac{r(r-1)}{2(2n-1)}}$$

---

**(b) $\text{Var}(X)$를 구하라.**

분산의 분해 공식을 사용한다:

$$\text{Var}(X) = \sum_{i=1}^{n} \text{Var}(X_i) + 2\sum_{i < j} \text{Cov}(X_i, X_j)$$

모든 $X_i$가 동일한 분포를 가지고, 모든 $(i,j)$ 쌍도 동일하므로:

$$\text{Var}(X) = n \cdot \text{Var}(X_1) + 2\binom{n}{2}\text{Cov}(X_1, X_2) = n\,\text{Var}(X_1) + n(n-1)\,\text{Cov}(X_1, X_2)$$

**$\text{Var}(X_1)$ 계산:**

$X_i \in \{0, 1\}$이므로 $0^2 = 0$, $1^2 = 1$에서 $X_i^2 = X_i$가 성립한다. 따라서:

$$E[X_i^2] = E[X_i] = p$$

분산의 정의에 대입하면:

$$\text{Var}(X_1) = E[X_1^2] - (E[X_1])^2 = p - p^2 = p(1-p), \qquad p = \frac{r(r-1)}{2n(2n-1)}$$

**$\text{Cov}(X_1, X_2)$ 계산:**

$$\text{Cov}(X_1, X_2) = E[X_1 X_2] - E[X_1]\,E[X_2] = E[X_1 X_2] - p^2$$

$E[X_1 X_2] = P\{X_1=1,\, X_2=1\}$: 1번 쌍과 2번 쌍이 모두 빨간 쌍일 확률.

즉, 총 4개의 특정 위치(1번 쌍 2자리, 2번 쌍 2자리)에 모두 빨간 공이 배정될 확률이다. 대칭성에 의해 $2n$개의 위치 중 4개의 특정 위치가 모두 빨간 확률과 같으므로:

$$P\{X_1=1,\, X_2=1\} = \frac{r}{2n} \cdot \frac{r-1}{2n-1} \cdot \frac{r-2}{2n-2} \cdot \frac{r-3}{2n-3} = \frac{r(r-1)(r-2)(r-3)}{2n(2n-1)(2n-2)(2n-3)}$$

$q = \dfrac{r(r-1)(r-2)(r-3)}{2n(2n-1)(2n-2)(2n-3)}$로 정의하면:

$$\text{Cov}(X_1, X_2) = q - p^2$$

**최종 결과:**

$$\boxed{\text{Var}(X) = np(1-p) + n(n-1)(q - p^2)}$$

$$\text{where} \quad p = \frac{r(r-1)}{2n(2n-1)}, \qquad q = \frac{r(r-1)(r-2)(r-3)}{2n(2n-1)(2n-2)(2n-3)}$$

---

## Problem from Lecture Note

**문제:** $X \sim N(\mu, \sigma^2)$일 때, $\text{Var}(X)$를 구하라. (강의노트 Example 2.27 참고, 모든 단계를 상세히 보여라.)

**풀이:**

분산의 정의와 $E[X] = \mu$ (강의노트 Example 2.22)를 이용하면:

$$\text{Var}(X) = E[(X - \mu)^2] = \frac{1}{\sqrt{2\pi}\,\sigma} \int_{-\infty}^{\infty} (x-\mu)^2\, e^{-(x-\mu)^2/2\sigma^2}\,dx$$

**Step 1: 치환 $y = \dfrac{x - \mu}{\sigma}$**

$x - \mu = \sigma y$, $dx = \sigma\,dy$로 치환하면:

$$\text{Var}(X) = \frac{1}{\sqrt{2\pi}\,\sigma} \int_{-\infty}^{\infty} (\sigma y)^2\, e^{-y^2/2}\,\sigma\,dy = \frac{\sigma^2}{\sqrt{2\pi}} \int_{-\infty}^{\infty} y^2 e^{-y^2/2}\,dy$$

**Step 2: $\displaystyle I = \int_{-\infty}^{\infty} y^2 e^{-y^2/2}\,dy$ 계산 (부분적분)**

$y^2 e^{-y^2/2} = y \cdot \left(y e^{-y^2/2}\right)$로 분리하고 부분적분을 적용한다.

$$u = y, \quad dv = y e^{-y^2/2}\,dy \implies du = dy, \quad v = -e^{-y^2/2}$$

$$I = \left[-y e^{-y^2/2}\right]_{-\infty}^{\infty} + \int_{-\infty}^{\infty} e^{-y^2/2}\,dy$$

첫 번째 항: $\displaystyle\lim_{y \to \pm\infty} y e^{-y^2/2} = 0$ (지수 감소가 다항식보다 빠름)이므로:

$$\left[-y e^{-y^2/2}\right]_{-\infty}^{\infty} = 0$$

두 번째 항: 가우시안 적분(Gaussian integral) 공식

$$\int_{-\infty}^{\infty} e^{-y^2/2}\,dy = \sqrt{2\pi}$$

따라서:

$$I = 0 + \sqrt{2\pi} = \sqrt{2\pi}$$

**Step 3: 최종 계산**

$$\text{Var}(X) = \frac{\sigma^2}{\sqrt{2\pi}} \cdot I = \frac{\sigma^2}{\sqrt{2\pi}} \cdot \sqrt{2\pi}$$

$$\boxed{\text{Var}(X) = \sigma^2}$$

> 즉, 정규분포 $N(\mu, \sigma^2)$에서 두 번째 파라미터 $\sigma^2$이 정확히 분산임을 확인했다.