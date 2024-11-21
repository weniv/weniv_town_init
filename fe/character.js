// character.js
class Character {
    constructor(x, y, id, type = 'licat', name = '') {
        this.x = x;
        this.y = y;
        this.id = id;
        this.name = name;
        this.baseSpritesImages = 'assets/img/characters/';
        this.direction = 'down';
        this.type = type;
        this.element = document.createElement('div');
        this.element.className = 'character';
        this.element.id = `character-${id}`;
        
        // 이름 표시 요소 추가
        this.nameElement = document.createElement('div');
        this.nameElement.className = 'character-name';
        this.nameElement.textContent = name;
        this.element.appendChild(this.nameElement);
        
        this.sprites = {
            down: `${this.baseSpritesImages}${type}-3.webp`,
            up: `${this.baseSpritesImages}${type}-1.webp`,
            left: `${this.baseSpritesImages}${type}-2.webp`,
            right: `${this.baseSpritesImages}${type}-0.webp`
        };
        
        this.gameArea = document.getElementById('gameArea');
        this.gameArea.appendChild(this.element);
        this.updatePosition();
        this.updateSprite();
    }

    move(newX, newY, direction) {
        this.x = newX;
        this.y = newY;
        if (direction) {
            this.direction = direction;
            this.updateSprite();
        }
        this.updatePosition();
    }

    updatePosition() {
        this.element.style.left = `${this.x}px`;
        this.element.style.top = `${this.y}px`;
    }

    updateSprite() {
        this.element.style.backgroundImage = `url(${this.sprites[this.direction]})`;
    }
}